#!/usr/bin/env python3
"""
British TV Hub — automated fact-checker.

Runs on a schedule via .github/workflows/fact-check.yml.
Re-verifies a rotating batch of show-database entries, the full
acorn-new.json / britbox-new.json content, AND a rotating batch of the
schema.org TVSeries claims embedded in the site's HTML pages (episode
counts, air dates, season counts, and the short factual description text)
using the Anthropic API with web search, then:
  - for show-database entries: if a region's platform list is wrong, applies
    the model's confident replacement directly (structured data, safe to
    auto-apply); if it's only "uncertain" or no confident replacement was
    found, leaves the data untouched and flags it for a human instead
  - for acorn-new.json / britbox-new.json and the embedded editorial claims
    (richer prose/dates, riskier to auto-edit unreviewed): only flags issues,
    never rewrites them automatically
  - updates "verified" / "sources" metadata for anything checked
  - appends a run summary (including any auto-applied fixes) to fact-check-log.json
  - opens a GitHub Issue listing what was auto-fixed and what still needs a
    human look, if anything came back as an issue or uncertain

Editorial HTML claims are tracked separately in editorial-verified.json,
keyed by "page::show name", with a content hash so that editing a claim
resets its verification (an edited claim is treated as unverified again,
not silently carried forward as still-confirmed). This only covers claims
inside <script type="application/ld+json"> blocks — free-form prose
elsewhere on a page (anecdotes, quotes, comparisons) is not scanned, since
there's no structured way to isolate individual factual claims from it.

Requires the ANTHROPIC_API_KEY secret to be set on the repo.
"""

import glob
import hashlib
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
EDITORIAL_PER_RUN = 10  # rotate through embedded TVSeries claims across all pages

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
    "sources": ["https://...", "..."],
    "corrected": {{
      "us": [{{"name": "...", "tag": "stream|free", "url": "..."}}],
      "uk": [{{"name": "...", "tag": "stream|free", "url": "..."}}],
      "au": [{{"name": "...", "tag": "stream|free", "url": "..."}}]
    }}
  }}
]
"confirmed" = everything listed checks out — omit "corrected" entirely.
"issue" = something is wrong or has changed — include "corrected" with the FULL
replacement platform list for every region you have a confident answer for
(carry forward any region you didn't find a problem with unchanged; omit a
region from "corrected" entirely if you're not confident enough to replace it,
rather than guessing). Use real working URLs: for BritBox use
https://www.amazon.com/gp/video/channel/c984b526-fff5-46bf-af6d-68abb4a6a5d2?tag=britishtvhub-20,
for Acorn TV use https://www.amazon.com/gp/video/channel/c8382769-b3fd-49e8-818c-021154583c89?tag=britishtvhub-20,
otherwise the platform's real official watch/show page. "uncertain" = couldn't
verify either way — omit "corrected". No prose outside the JSON."""


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


def claim_hash(claim):
    """Hash the factual fields of a claim so an edit invalidates prior verification."""
    fields = {k: claim.get(k) for k in
              ("description", "startDate", "endDate", "numberOfSeasons", "numberOfEpisodes")}
    return hashlib.sha256(json.dumps(fields, sort_keys=True).encode()).hexdigest()[:16]


def extract_editorial_claims():
    """Scan every HTML page for schema.org TVSeries entries inside ItemList JSON-LD
    blocks. Returns a list of dicts: page, name, description, startDate, endDate,
    numberOfSeasons, numberOfEpisodes (fields present depend on what's in the page)."""
    claims = []
    for path in sorted(glob.glob(os.path.join(REPO_ROOT, "*.html"))):
        page = os.path.basename(path)
        with open(path, encoding="utf-8") as f:
            content = f.read()
        for match in re.finditer(
                r'<script type="application/ld\+json">(.*?)</script>', content, re.S):
            try:
                data = json.loads(match.group(1))
            except json.JSONDecodeError:
                continue
            if data.get("@type") != "ItemList":
                continue
            for item in data.get("itemListElement", []):
                show = item.get("item", {})
                if show.get("@type") != "TVSeries":
                    continue
                claims.append({
                    "page": page,
                    "name": show.get("name"),
                    "description": show.get("description"),
                    "startDate": show.get("startDate"),
                    "endDate": show.get("endDate"),
                    "numberOfSeasons": show.get("numberOfSeasons"),
                    "numberOfEpisodes": show.get("numberOfEpisodes"),
                })
    return claims


def build_editorial_prompt(batch):
    items = "\n".join(
        f'- [{c["page"]}] "{c["name"]}": "{c["description"]}"'
        + (f' (aired {c["startDate"]}\u2013{c["endDate"]})' if c.get("startDate") else "")
        + (f' ({c["numberOfSeasons"]} seasons)' if c.get("numberOfSeasons") else "")
        + (f' ({c["numberOfEpisodes"]} episodes)' if c.get("numberOfEpisodes") else "")
        for c in batch
    )
    return f"""You are fact-checking factual claims about British TV shows published
on a fan site. For each claim below, verify using web search whether the
description text and any stated air dates / season count / episode count are
ACCURATE. Flag anything that is wrong, outdated, or unverifiable — including
misattributed quotes, incorrect production details, or wrong counts.

Claims to check:
{items}

Respond with ONLY a JSON array, one object per claim, in this exact shape:
[
  {{
    "page": "...",
    "name": "...",
    "status": "confirmed" | "issue" | "uncertain",
    "notes": "short explanation, only needed if status is not confirmed",
    "sources": ["https://...", "..."]
  }}
]
"confirmed" = everything stated checks out. "issue" = something is wrong,
outdated, or misattributed. "uncertain" = couldn't verify either way.
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
    shows_check_failed = False
    try:
        shows_result = extract_json_block(call_claude(build_shows_prompt(batch)))
    except Exception as e:
        shows_result = []
        shows_check_failed = True
        print(f"Shows batch check failed: {e}", file=sys.stderr)

    for r in shows_result:
        if r.get("status") == "confirmed":
            all_confirmed.append(r)
        else:
            all_issues.append({**r, "source_file": "shows-database.json"})

    print("Checking acorn-new.json and britbox-new.json...")
    arrivals_check_failed = False
    try:
        arrivals_result = extract_json_block(call_claude(build_britbox_acorn_prompt(acorn, britbox)))
    except Exception as e:
        arrivals_result = []
        arrivals_check_failed = True
        print(f"Arrivals check failed: {e}", file=sys.stderr)

    for r in arrivals_result:
        if r.get("status") == "confirmed":
            all_confirmed.append(r)
        else:
            all_issues.append({**r, "source_file": "acorn-new.json / britbox-new.json"})

    # Only bump "verified" for shows we actually got a real answer for — never
    # mark something as freshly checked when the API call itself failed, or
    # the rotation would skip it for weeks having never really been checked.
    # When the model flagged an issue AND gave us a confident replacement
    # ("corrected"), apply it region-by-region so the database actually gets
    # fixed — not just annotated as checked while the wrong data stays live.
    checked_titles = {r["title"] for r in shows_result}
    applied_fixes = []
    for s in shows:
        if s["title"] in checked_titles:
            s["verified"] = TODAY
            match = next((r for r in shows_result if r["title"] == s["title"]), None)
            if match:
                s["sources"] = match.get("sources", [])
                corrected = match.get("corrected") or {}
                changed_regions = []
                for region in ("us", "uk", "au"):
                    if region in corrected and corrected[region]:
                        if corrected[region] != s.get(region):
                            changed_regions.append(region)
                        s[region] = corrected[region]
                if changed_regions:
                    applied_fixes.append({
                        "title": s["title"],
                        "regions": changed_regions,
                        "notes": match.get("notes", ""),
                    })
    save_json("shows-database.json", shows)

    # --- Editorial HTML claims (schema.org TVSeries entries embedded in pages) ---
    editorial_path = os.path.join(REPO_ROOT, "editorial-verified.json")
    editorial_state = {}
    if os.path.exists(editorial_path):
        with open(editorial_path, encoding="utf-8") as f:
            editorial_state = json.load(f)

    all_claims = extract_editorial_claims()
    print(f"Found {len(all_claims)} TVSeries claims across all pages.")

    def claim_key(c):
        return f"{c['page']}::{c['name']}"

    # Prioritize: never-verified or edited-since-last-verification claims first,
    # then the ones with the oldest verification date.
    def priority(c):
        key = claim_key(c)
        entry = editorial_state.get(key)
        if entry is None or entry.get("hash") != claim_hash(c):
            return ("0", "")  # unverified or changed — always first
        return ("1", entry.get("verified", "1970-01-01"))

    claims_sorted = sorted(all_claims, key=priority)
    editorial_batch = claims_sorted[:EDITORIAL_PER_RUN]

    editorial_check_failed = False
    editorial_result = []
    if editorial_batch:
        print(f"Checking {len(editorial_batch)} editorial claims: "
              + ", ".join(f"{c['page']}/{c['name']}" for c in editorial_batch))
        try:
            editorial_result = extract_json_block(call_claude(build_editorial_prompt(editorial_batch)))
        except Exception as e:
            editorial_check_failed = True
            print(f"Editorial batch check failed: {e}", file=sys.stderr)
    else:
        print("No TVSeries claims found to check.")

    editorial_checked_keys = set()
    for r in editorial_result:
        key = f"{r.get('page')}::{r.get('name')}"
        editorial_checked_keys.add(key)
        source_claim = next(
            (c for c in editorial_batch if claim_key(c) == key), None)
        if r.get("status") == "confirmed":
            all_confirmed.append(r)
            editorial_state[key] = {
                "hash": claim_hash(source_claim) if source_claim else None,
                "verified": TODAY,
                "status": "confirmed",
            }
        else:
            all_issues.append({**r, "title": r.get("name"),
                                "source_file": f"{r.get('page')} (schema.org TVSeries)"})
            # Still record that it was checked (with today's date) so a
            # flagged-but-unfixed claim doesn't get re-checked every single
            # run — it'll surface again once the rotation cycles back, or
            # immediately once someone edits the description (hash changes).
            editorial_state[key] = {
                "hash": claim_hash(source_claim) if source_claim else None,
                "verified": TODAY,
                "status": "issue",
            }

    with open(editorial_path, "w", encoding="utf-8") as f:
        json.dump(editorial_state, f, indent=2, ensure_ascii=False, sort_keys=True)
        f.write("\n")

    # Log this run
    log_path = os.path.join(REPO_ROOT, "fact-check-log.json")
    log = []
    if os.path.exists(log_path):
        with open(log_path, encoding="utf-8") as f:
            log = json.load(f)
    log.append({
        "date": TODAY,
        "shows_checked": sorted(checked_titles),
        "arrivals_checked": [r["title"] for r in arrivals_result],
        "editorial_checked": sorted(editorial_checked_keys),
        "confirmed_count": len(all_confirmed),
        "issue_count": len(all_issues),
        "issues": all_issues,
        "applied_fixes": applied_fixes,
        "shows_check_failed": shows_check_failed,
        "arrivals_check_failed": arrivals_check_failed,
        "editorial_check_failed": editorial_check_failed,
    })
    save_json("fact-check-log.json", log)

    if applied_fixes or all_issues:
        body_lines = []
        if applied_fixes:
            body_lines.append(
                f"Automated fact-check run on {TODAY} auto-corrected "
                f"{len(applied_fixes)} show(s) in shows-database.json:\n"
            )
            for fix in applied_fixes:
                body_lines.append(f"### {fix['title']} — updated {', '.join(r.upper() for r in fix['regions'])}")
                if fix.get("notes"):
                    body_lines.append(fix["notes"])
                body_lines.append("")
        applied_titles = {f["title"] for f in applied_fixes}
        remaining = [
            issue for issue in all_issues
            if not (issue.get("source_file") == "shows-database.json"
                    and issue.get("title") in applied_titles)
        ]
        if remaining:
            body_lines.append(f"\n{len(remaining)} item(s) still need a human look "
                               "(uncertain, or no confident replacement was found):\n")
            for issue in remaining:
                body_lines.append(f"### {issue.get('title', 'Unknown')} ({issue.get('source_file','')})")
                body_lines.append(f"**Status:** {issue.get('status')}")
                if issue.get("notes"):
                    body_lines.append(f"**Notes:** {issue['notes']}")
                if issue.get("sources"):
                    body_lines.append("**Sources:** " + ", ".join(issue["sources"]))
                body_lines.append("")
        body_lines.append(
            "\n_This issue was opened automatically by `.github/workflows/fact-check.yml`. "
            "Auto-corrected items are already live — spot-check them if you like. Remaining "
            "items need the site content updated directly (or ask Claude to do it), then close "
            "this issue._"
        )
        open_issue(
            f"Fact-check: {len(applied_fixes)} auto-fixed, {len(remaining)} flagged ({TODAY})",
            "\n".join(body_lines),
        )
        print(f"Applied {len(applied_fixes)} fix(es); {len(remaining)} item(s) still flagged.")
    else:
        print("No issues found this run.")

    # Fail the run loudly if ALL THREE checks errored out — a green checkmark
    # should mean verification actually happened, not that it silently no-op'd.
    if shows_check_failed and arrivals_check_failed and editorial_check_failed:
        print("All checks failed to produce results — see errors above.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
