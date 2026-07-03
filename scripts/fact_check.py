#!/usr/bin/env python3
"""
British TV Hub — automated fact-checker.

Runs on a schedule via .github/workflows/fact-check.yml.
Re-verifies a rotating batch of show-database entries plus the full
acorn-new.json / britbox-new.json content using the Anthropic API with
web search, then:
  - updates "verified" / "sources" metadata for anything confirmed
  - appends a run summary to fact-check-log.json
  - opens a GitHub Issue if anything looks wrong or out of date

Requires the ANTHROPIC_API_KEY secret to be set on the repo.
"""

import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "")  # "owner/repo"
MODEL = "claude-sonnet-4-6"
SHOWS_PER_RUN = 10  # rotate through the 30-show database ~3 runs per full pass

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")


def load_json(name):
    path = os.path.join(REPO_ROOT, name)
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_json(name, data):
    path = os.path.join(REPO_ROOT, name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def call_claude(prompt, max_tokens=4000):
    """Call the Anthropic API with web search enabled, return final text."""
    body = {
        "model": MODEL,
        "max_tokens": max_tokens,
        "tools": [{"type": "web_search_20250305", "name": "web_search"}],
        "messages": [{"role": "user", "content": prompt}],
    }
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=json.dumps(body).encode(),
        headers={
            "Content-Type": "application/json",
            "x-api-key": ANTHROPIC_API_KEY,
            "anthropic-version": "2023-06-01",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        # Surface Anthropic's actual error message instead of a generic one,
        # so failures are diagnosable from the Action log without guessing.
        detail = e.read().decode(errors="replace")
        raise RuntimeError(f"Anthropic API error {e.code}: {detail}") from None
    texts = [b["text"] for b in data.get("content", []) if b.get("type") == "text"]
    return "\n".join(texts)


def extract_json_block(text):
    """Pull the last {...} or [...] JSON block out of a model response."""
    matches = re.findall(r"(\[.*\]|\{.*\})", text, re.S)
    for candidate in reversed(matches):
        try:
            return json.loads(candidate)
        except json.JSONDecodeError:
            continue
    raise ValueError("No parseable JSON found in model response")


def build_shows_prompt(batch):
    items = "\n".join(
        f'- "{s["title"]}" ({s["years"]}, {s["genre"]}): currently claimed streaming — '
        f'US: {", ".join(x["name"] for x in s.get("us", []))} | '
        f'UK: {", ".join(x["name"] for x in s.get("uk", []))} | '
        f'AU: {", ".join(x["name"] for x in s.get("au", []))}'
        for s in batch
    )
    return f"""You are fact-checking a British TV streaming guide. For each show below,
verify using web search whether the CURRENT streaming platforms listed for each
region (US/UK/AU) are still accurate today, and whether the year range is correct.

Shows to check:
{items}

Respond with ONLY a JSON array, one object per show, in this exact shape:
[
  {{
    "title": "...",
    "status": "confirmed" | "issue" | "uncertain",
    "notes": "short explanation, only needed if status is not confirmed",
    "sources": ["https://...", "..."]
  }}
]
"confirmed" = everything listed checks out. "issue" = something is wrong or has
changed. "uncertain" = couldn't verify either way. No prose outside the JSON."""


def build_britbox_acorn_prompt(acorn, britbox):
    def summarize(label, data):
        lines = [f"{label} highlight: \"{data['highlight']['title']}\" — {data['highlight']['badge']}"]
        for a in data.get("new_arrivals", []):
            lines.append(f'{label} arrival: "{a["title"]}" ({a.get("season","")}) — available {a.get("available","")}')
        return "\n".join(lines)

    content = summarize("Acorn TV", acorn) + "\n\n" + summarize("BritBox", britbox)
    return f"""You are fact-checking the "What's New" sections of a British TV
streaming guide (British TV Hub). Verify using web search whether these claims
about current/upcoming premieres are still accurate as of today ({TODAY}).

{content}

Respond with ONLY a JSON array, one object per title, in this exact shape:
[
  {{
    "title": "...",
    "status": "confirmed" | "issue" | "uncertain",
    "notes": "short explanation, only needed if status is not confirmed",
    "sources": ["https://...", "..."]
  }}
]
No prose outside the JSON."""


def github_api(method, path, data=None):
    url = f"https://api.github.com/repos/{GITHUB_REPOSITORY}/{path}"
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", f"token {GITHUB_TOKEN}")
    req.add_header("Accept", "application/vnd.github+json")
    body = json.dumps(data).encode() if data is not None else None
    if body:
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, data=body, timeout=60) as resp:
        return json.loads(resp.read())


def open_issue(title, body):
    if not GITHUB_TOKEN or not GITHUB_REPOSITORY:
        print("No GITHUB_TOKEN/GITHUB_REPOSITORY available, skipping issue creation.")
        print(body)
        return
    github_api("POST", "issues", {"title": title, "body": body, "labels": ["fact-check"]})


def main():
    if not ANTHROPIC_API_KEY:
        print("ANTHROPIC_API_KEY not set — add it under repo Settings > Secrets and "
              "variables > Actions, then re-run this workflow.", file=sys.stderr)
        sys.exit(1)

    shows = load_json("shows-database.json")
    acorn = load_json("acorn-new.json")
    britbox = load_json("britbox-new.json")

    # Rotate: check the shows with the oldest "verified" date first
    shows_sorted = sorted(shows, key=lambda s: s.get("verified", "1970-01-01"))
    batch = shows_sorted[:SHOWS_PER_RUN]
    batch_titles = {s["title"] for s in batch}

    all_issues = []
    all_confirmed = []

    print(f"Checking {len(batch)} show-database entries: {', '.join(batch_titles)}")
    try:
        shows_result = extract_json_block(call_claude(build_shows_prompt(batch)))
    except Exception as e:
        shows_result = []
        print(f"Shows batch check failed: {e}", file=sys.stderr)

    for r in shows_result:
        if r.get("status") == "confirmed":
            all_confirmed.append(r)
        else:
            all_issues.append({**r, "source_file": "shows-database.json"})

    print("Checking acorn-new.json and britbox-new.json...")
    try:
        arrivals_result = extract_json_block(call_claude(build_britbox_acorn_prompt(acorn, britbox)))
    except Exception as e:
        arrivals_result = []
        print(f"Arrivals check failed: {e}", file=sys.stderr)

    for r in arrivals_result:
        if r.get("status") == "confirmed":
            all_confirmed.append(r)
        else:
            all_issues.append({**r, "source_file": "acorn-new.json / britbox-new.json"})

    # Update verified dates + sources for confirmed shows, and bump the whole
    # batch's date regardless (so the rotation keeps moving even on "issue"/
    # "uncertain" results — those get flagged in the issue instead).
    confirmed_titles = {r["title"] for r in all_confirmed}
    for s in shows:
        if s["title"] in batch_titles:
            s["verified"] = TODAY
            match = next((r for r in shows_result if r["title"] == s["title"]), None)
            if match:
                s["sources"] = match.get("sources", [])
    save_json("shows-database.json", shows)

    # Log this run
    log_path = os.path.join(REPO_ROOT, "fact-check-log.json")
    log = []
    if os.path.exists(log_path):
        with open(log_path, encoding="utf-8") as f:
            log = json.load(f)
    log.append({
        "date": TODAY,
        "shows_checked": sorted(batch_titles),
        "arrivals_checked": [r["title"] for r in shows_result + arrivals_result],
        "confirmed_count": len(all_confirmed),
        "issue_count": len(all_issues),
        "issues": all_issues,
    })
    save_json("fact-check-log.json", log)

    if all_issues:
        body_lines = [
            f"Automated fact-check run on {TODAY} found {len(all_issues)} item(s) "
            "that may need a human look:\n"
        ]
        for issue in all_issues:
            body_lines.append(f"### {issue.get('title', 'Unknown')} ({issue.get('source_file','')})")
            body_lines.append(f"**Status:** {issue.get('status')}")
            if issue.get("notes"):
                body_lines.append(f"**Notes:** {issue['notes']}")
            if issue.get("sources"):
                body_lines.append("**Sources:** " + ", ".join(issue["sources"]))
            body_lines.append("")
        body_lines.append(
            "\n_This issue was opened automatically by `.github/workflows/fact-check.yml`. "
            "Check the flagged item(s) and update the site content directly (or ask Claude "
            "to do it), then close this issue._"
        )
        open_issue(f"Fact-check: {len(all_issues)} item(s) flagged ({TODAY})", "\n".join(body_lines))
        print(f"Opened issue for {len(all_issues)} flagged item(s).")
    else:
        print("No issues found this run.")


if __name__ == "__main__":
    main()
