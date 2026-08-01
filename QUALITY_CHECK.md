# British TV Hub — Sitewide Quality Check Checklist

Reference doc for running a full sitewide quality check (not just a spot check
of recent changes). Covers: affiliate links, broken links, old/dead code,
fact-check accuracy, mobile compatibility, unverifiable claims, spelling, and
nav/footer consistency. Pairs with the standing biweekly quality-audit cadence
and the monthly "What's New" / streaming-availability review.

Run these from the repo root. All are read-only checks — nothing here writes
files, so it's safe to run anytime.

## 1. Broken internal links & missing assets

Checks every `href`/`src` across all `.html` files (including `/shows/`)
resolves to a real file.

```python
import re, os, glob

pages = glob.glob('**/*.html', recursive=True)
all_files = set()
for root, dirs, files in os.walk('.'):
    if '.git' in root: continue
    for f in files:
        all_files.add(os.path.relpath(os.path.join(root, f), '.').replace('\\', '/'))

for p in pages:
    content = open(p, encoding='utf-8').read()
    for m in re.finditer(r'href="([^"]+)"', content):
        href = m.group(1)
        if href.startswith(('http', '//', '#', 'mailto', 'tel:', '${')) or "' +" in href:
            continue
        path = href.lstrip('/').split('#')[0].split('?')[0]
        if not path: continue
        candidate = path if os.path.splitext(path)[1] else path + '.html'
        if candidate not in all_files and path not in all_files:
            print(f"BROKEN: {p}: {href}")
```

Do the same with `src="..."` for images/scripts.

**Known non-issues:** JS template literals (`${show.url}`, `' + show.url + '`)
inside `<script>` blocks will false-positive on a naive regex — exclude
anything containing `${` or `' +`.

## 2. Affiliate link consistency

```bash
grep -rn 'amazon\.com/channels/[a-f0-9-]\+' *.html shows/*.html   # old broken channel URL format — should be zero
grep -c "c984b526-fff5-46bf-af6d-68abb4a6a5d2" *.html shows/*.html   # BritBox — every hit should include ?tag=britishtvhub-20
grep -c "c8382769-b3fd-49e8-818c-021154583c89" *.html shows/*.html   # Acorn TV — same
grep -roh "nordvpn.com/special[^\"]*" *.html shows/*.html | sort -u  # should be exactly one URL sitewide
```

**Known non-issue:** `amazon.com/shop/influencer-*` URLs (the Amazon
Influencer Storefront, used on gift-ideas.html) don't use `?tag=`— that's a
different affiliate program tied to the URL path itself, not a missing tag.

## 3. Fact accuracy (streaming platforms, season counts)

- The automated pipeline (`scripts/fact_check.py`, runs via GitHub Actions on
  the 1st and 15th) checks a rotating batch of `shows-database.json` entries,
  `britbox-new.json`/`acorn-new.json`, and embedded schema.org claims. As of
  August 2026 it auto-applies confident streaming-platform corrections and
  opens a GitHub Issue listing what was auto-fixed vs. what still needs a
  human look.
- Check `fact-check-log.json`'s most recent entry for `applied_fixes` and
  `issues` before assuming the database is current — only ~10 shows get
  checked per run, so full coverage of all 150 shows takes months.
- **Recurring error to watch for:** "BritBox" listed as a UK platform.
  BritBox UK stopped existing as a standalone service in April 2024 (absorbed
  into ITVX Premium) — this has turned up repeatedly across the show
  database. Quick check:
  ```python
  import json
  d = json.load(open('shows-database.json'))
  print([s['title'] for s in d if any(x['name']=='BritBox' for x in s.get('uk',[]))])
  ```
  Should return an empty list. If a show's UK region would end up with zero
  platforms after removing it, verify a real replacement via JustWatch UK
  before removing — don't leave it empty on a guess.

## 4. Stale dates

```bash
grep -rl "July 2026" *.html shows/*.html   # swap the month for whatever the previous month was
```
**Known non-issue:** `privacy.html`'s "Last Updated: [month]" is a legal date
— only bump it when the policy text actually changes, not automatically.

## 5. American spellings

Brand content should use British spelling. A naive word-list regex produces
massive false-positive noise — filter these out before trusting results:

- **`center`, `color`, `behavior` and variants**: these are CSS property
  values / JS Web API option names (`text-align: center`, `transition: color`,
  `scroll-behavior: smooth`, `{behavior: 'smooth'}`) — the American spelling
  is the *only valid* keyword here. Do not "fix" these; it will break styling.
- **`"Organization"` inside `<script type="application/ld+json">`**: this is
  a fixed schema.org vocabulary term (`@type": "Organization"`), not free
  text — changing it to "Organisation" breaks the structured data.
- **Known accepted exception:** `footer-brand.webp`'s alt text says "...their
  favorite television series" — this is baked into the image file itself and
  was reviewed/accepted already; the American spelling there is intentional
  (matches the image), not a bug.

After excluding those, check what's left — that's the real signal.

## 6. Superlatives / unverifiable claims

```bash
grep -rniE "trusted by|guaranteed|industry.leading|world.class|unmatched|unparalleled|fastest.growing" *.html
```
Most hits are legitimate editorial voice ("the best cozy mysteries," a
curated recommendation) — only flag ones that pair a superlative with a
**specific unverifiable number or unbacked factual claim** (e.g., a follower
count, "#1 rated," an award not actually verified). The sitewide "5,000+
fans" issue (fixed August 2026, see git log) is the template for what a real
issue looks like: specific number + unverifiable claim = fix it. Vague
opinion language ("the best," "always a good time") = leave it.

## 7. Nav/footer consistency

```bash
for f in *.html shows/*.html; do grep -q "watch-list.html" "$f" || echo "MISSING watch-list nav: $f"; done
for f in *.html shows/*.html; do grep -q "gift-ideas.html" "$f" || echo "MISSING gift-ideas nav: $f"; done
for f in *.html shows/*.html; do grep -q "footer-brand.webp" "$f" || echo "MISSING standard footer: $f"; done
```
All three should return nothing. Also spot-check the GA tag is identical
everywhere: `grep -roh "G-[A-Z0-9]*" *.html shows/*.html | sort -u` should
return exactly one ID (`G-P1L8CVNKS6`).

## 8. Old/dead code

```bash
grep -l 'class="footer-links"' *.html shows/*.html   # leftover pre-standard-footer markup — should be empty
```
Also worth an occasional look: orphaned files in the repo root not referenced
by any page (check `git log` for recently-removed-from-nav pages like the old
`beginners.html` pattern), and duplicate/stray script blocks left over from
before a redesign.

## 9. Mobile compatibility

```bash
for f in *.html shows/*.html; do grep -q 'name="viewport"' "$f" || echo "MISSING viewport: $f"; done
```
Should return nothing. Deeper mobile QA (actual responsive rendering) isn't
covered by this text-based checklist — that needs a browser/device check.

---

**Last full sitewide run:** August 1, 2026 — no issues found beyond what's
listed as "known non-issue" above; the BritBox-UK sweep and follower-count
sweep from that session are reflected as the worked examples in sections 3
and 6.
