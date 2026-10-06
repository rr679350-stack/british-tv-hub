#!/usr/bin/env python3
import glob, html, json, os, re, sys, time, urllib.request
from datetime import datetime, timezone
from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API_KEY = os.environ.get("ANTHROPIC_API_KEY")
MODEL = "claude-sonnet-4-6"
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")
OUT = os.path.join(ROOT, "full-fact-audit")
os.makedirs(OUT, exist_ok=True)
SKIP = {"checkout-redirect.html"}
MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
RISK = re.compile(
    rf"(\b(?:19|20)\d{{2}}\b|\b(?:{MONTHS})\b|\b(?:season|series|episode|episodes|premiere|premieres|"
    r"available|stream|streaming|BritBox|Acorn|PBS|Masterpiece|Prime Video|Tubi|Pluto|ITVX|BBC|Channel 4|"
    r"stars?|starring|created by|written by|adapted|based on|filmed|location|renewed|cancelled|canceled|"
    r"returns?|returning|new season|final season|award|BAFTA|Emmy|longest-running|first|debut|released?)\b)", re.I)

def call_model(prompt, max_tokens=7000):
    body = {"model": MODEL, "max_tokens": max_tokens,
            "tools": [{"type": "web_search_20250305", "name": "web_search"}],
            "messages": [{"role": "user", "content": prompt}]}
    req = urllib.request.Request("https://api.anthropic.com/v1/messages",
        data=json.dumps(body).encode(),
        headers={"Content-Type":"application/json","x-api-key":API_KEY,"anthropic-version":"2023-06-01"})
    with urllib.request.urlopen(req, timeout=240) as resp:
        data=json.loads(resp.read())
    return "\n".join(x["text"] for x in data.get("content",[]) if x.get("type")=="text")

def parse_json(text):
    m=re.search(r"(\[.*\])", text, re.S)
    if not m: raise ValueError("No JSON array found")
    return json.loads(m.group(1))

def clean_text(path):
    with open(path, encoding="utf-8") as f: soup=BeautifulSoup(f.read(),"html.parser")
    for tag in soup(["script","style","noscript","svg","nav","footer"]): tag.decompose()
    title=soup.title.get_text(" ",strip=True) if soup.title else os.path.basename(path)
    h1=soup.find("h1"); h1=h1.get_text(" ",strip=True) if h1 else ""
    text=html.unescape(re.sub(r"\s+"," "," ".join(soup.stripped_strings)))
    return title,h1,text

def claim_sentences(text):
    parts=re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])",text)
    seen=set(); claims=[]
    for s in parts:
        s=s.strip()
        if len(s)<25 or len(s)>650 or not RISK.search(s): continue
        key=re.sub(r"\W+"," ",s.lower()).strip()
        if key in seen: continue
        seen.add(key); claims.append(s)
    return claims[:28]

def inventory():
    pages=[]
    for path in sorted(glob.glob(os.path.join(ROOT,"**","*.html"),recursive=True)):
        rel=os.path.relpath(path,ROOT).replace(os.sep,"/")
        if rel.startswith((".git/","node_modules/","accessibility-report/","full-fact-audit/")) or rel in SKIP: continue
        title,h1,text=clean_text(path)
        pages.append({"page":rel,"title":title,"h1":h1,"claims":claim_sentences(text)})
    return pages

def prompt_for(batch):
    blocks=[]
    for p in batch:
        claims="\n".join("  - "+c for c in p["claims"]) or "  - No high-risk factual sentences detected by the extractor."
        blocks.append("PAGE: "+p["page"]+"\nTITLE: "+p["title"]+"\nH1: "+p["h1"]+"\nCLAIMS:\n"+claims)
    return f"""You are conducting a rigorous fact audit of BritishTVHub.com as of {TODAY}.
Verify EVERY supplied claim with web search. Prioritize primary and authoritative sources:
official broadcaster/streamer pages, production companies, PBS, BBC, ITV, Channel 4,
BritBox, Acorn TV, official press releases, BFI, BAFTA, Emmys, publishers and authors.
Use reputable secondary sources only when necessary.

Pay special attention to streaming availability in the US, premiere dates, current/upcoming
status, renewals/final seasons, season/episode counts, cast/character/creator/writer/adaptation
attribution, filming/location claims, awards and superlatives, and anything that could have
gone stale by {TODAY}. Do not treat opinions or recommendations as factual errors.

Return ONLY a JSON array, one object per page:
[
  {{
    "page":"...",
    "status":"confirmed"|"issue"|"uncertain",
    "issues":[{{"claim":"...","status":"issue"|"uncertain","correction":"...","reason":"...","sources":["https://..."]}}],
    "notes":"brief overall note"
  }}
]
Use confirmed only if all supplied claims check out.

""" + "\n\n".join(blocks)

def run():
    if not API_KEY:
        print("ANTHROPIC_API_KEY is missing",file=sys.stderr); sys.exit(1)
    pages=inventory()
    with open(os.path.join(OUT,"inventory.json"),"w",encoding="utf-8") as f: json.dump(pages,f,indent=2,ensure_ascii=False)
    results=[]; errors=[]; batch_size=3
    total=(len(pages)+batch_size-1)//batch_size
    for n,start in enumerate(range(0,len(pages),batch_size),1):
        batch=pages[start:start+batch_size]
        print(f"Batch {n}/{total}: "+", ".join(p["page"] for p in batch),flush=True)
        try:
            parsed=parse_json(call_model(prompt_for(batch)))
            got={x.get("page"):x for x in parsed if isinstance(x,dict)}
            for p in batch:
                results.append(got.get(p["page"],{"page":p["page"],"status":"uncertain","issues":[],"notes":"No page result returned."}))
        except Exception as e:
            errors.append({"pages":[p["page"] for p in batch],"error":str(e)})
            for p in batch:
                results.append({"page":p["page"],"status":"uncertain","issues":[],"notes":"Audit batch failed: "+str(e)})
        time.sleep(1)
    summary={"date":TODAY,"pages_inventory":len(pages),"pages_audited":len(results),
             "confirmed_pages":sum(r.get("status")=="confirmed" for r in results),
             "issue_pages":sum(r.get("status")=="issue" for r in results),
             "uncertain_pages":sum(r.get("status")=="uncertain" for r in results),
             "issue_items":sum(len(r.get("issues") or []) for r in results),"batch_errors":len(errors)}
    with open(os.path.join(OUT,"report.json"),"w",encoding="utf-8") as f:
        json.dump({"summary":summary,"results":results,"errors":errors},f,indent=2,ensure_ascii=False)
    lines=["# British TV Hub — Full Sitewide Fact Audit","",f"Date: {TODAY}","","## Summary",""]
    for k,v in summary.items(): lines.append(f"- **{k.replace('_',' ').title()}:** {v}")
    lines+=["","## Pages needing review",""]
    review=[r for r in results if r.get("status")!="confirmed"]
    if not review: lines.append("No issues or uncertainties found.")
    for r in review:
        lines.append(f"### {r.get('page')} — {r.get('status')}")
        if r.get("notes"): lines.append(r["notes"])
        for issue in r.get("issues") or []:
            lines.append(f"- **{issue.get('status','review').upper()}** — {issue.get('claim','')}")
            if issue.get("correction"): lines.append("  - Suggested correction: "+issue["correction"])
            if issue.get("reason"): lines.append("  - Reason: "+issue["reason"])
            if issue.get("sources"): lines.append("  - Sources: "+", ".join(issue["sources"]))
        lines.append("")
    if errors:
        lines+=["## Batch errors","",json.dumps(errors,indent=2)]
    with open(os.path.join(OUT,"report.md"),"w",encoding="utf-8") as f: f.write("\n".join(lines)+"\n")
    print(json.dumps(summary),flush=True)

if __name__=="__main__":
    run()
