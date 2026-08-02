# British TV Hub — Master Accuracy & Quality Audit Checklist

This is the official British TV Hub Editorial Accuracy Standard. Every
audit — weekly (Sundays) or ad hoc — runs this full checklist, not a spot
check of recent changes. Where a section below has a runnable check, run
it; where it doesn't, review manually against the criteria listed.

Run checks from the repo root. All the runnable checks are read-only —
nothing here writes files, so it's safe to run anytime.

## Editorial Rule #1 and #2 (apply above everything else)

**Editorial Rule #1:** Accuracy takes priority over everything else. If a
statement cannot be confidently verified using authoritative sources, it
should be revised or removed. When in doubt, remove or soften the claim
rather than stretching the evidence — rewrite to be more precise, or omit
it until it can be verified.

**Editorial Rule #2:** British TV Hub uses 100% original editorial copy.
The site should never include quotations from books, television programs,
publishers, broadcasters, reviews, interviews, or other copyrighted
sources. All descriptions are independently written summaries in British
TV Hub's own voice (see the absolute no-quotations rule and Part 15
below).

## Severity labels

Every issue found gets one of these labels:

- Confirmed Factual Error (red) — the information is incorrect; correct it.
- Needs Updating (orange) — was accurate but has since changed (new season,
  price change, cast change, premiere passed, etc.).
- Unsupported Claim (yellow) — too broad, or lacks reliable evidence
  (includes every superlative/banned-word hit from Part 9).
- Conflicting Sources (purple) — reliable sources disagree; note the
  uncertainty or revise to the more authoritative source.
- Verified Accurate (green) — confirmed against an authoritative source.

## Absolute site rule: no direct quotations, ever

British TV Hub never reproduces a direct quotation from any person, book,
review, interview, script, or article — not a single line, not even
attributed and under normal fair-use length. This applies everywhere:
show descriptions, book descriptions, blurbs, testimonials, "critics say"
style callouts, everywhere. Always paraphrase in the site's own voice
instead. This is a zero-tolerance rule, not a soften-if-possible one —
if content can't be paraphrased without losing its meaning, cut it rather
than quote it.

Audit check (manual + regex assist — a regex can't fully distinguish real
quotes from HTML attribute values, so treat hits as a worklist to eyeball,
not an automatic pass/fail):

```bash
# Curly/typographic quotes are the strongest signal of an actual quotation
grep -rno '"[^"]\{8,200\}"' *.html shows/*.html

# Straight-quote sentences in visible text (excludes common attribute noise)
grep -rnoE '"[A-Z][^"<>]{15,150}[.!?]"' *.html shows/*.html \
  | grep -viE 'support british tv hub|footer-brand|alt=|title=|href=|class=|style=|content=|name=|id=|type=|src='
```

Anything that reads like an actual quoted line from a person or published
work — not UI copy, meta description, or placeholder text — gets removed
or rewritten as paraphrase.

## PART 1 — Books (every book on the site)

- Title correct
- Subtitle correct
- Author name correct
- Publication year correct
- Correct series
- Correct book order within series
- Standalone vs. series correctly labeled
- Publisher correct (if stated)
- Character names correct
- Plot description accurate and spoiler-light
- TV/film adaptation statement accurate
- Cover image present and correct (if used)
- Amazon link resolves
- Affiliate tag (britishtvhub-20) intact
- No direct quotations from the book, a review, or the author

## PART 2 — Television shows (every show on the site)

- Title correct
- Original broadcaster correct
- Current streaming service(s) correct (US-facing, per site scope)
- Country of origin correct — flag anything non-British/non-Commonwealth
  that isn't clearly labeled "Beyond Britain" or similar
- Premiere year correct
- End year correct (or "present" if ongoing)
- Number of series/seasons correct
- Number of episodes correct (if stated)
- Main cast correct and current (accounts for recast/departed leads)
- Character names correct
- Show description accurate, no unsupported claims
- Adaptation details correct (if based on a book)
- Creator credited correctly (if mentioned)
- Production company correct (if mentioned)
- Awards correct and specific (never a bare "award-winning" — name the
  actual award)
- No direct quotations from reviews, interviews, or dialogue

## PART 3 — Streaming services (every streaming statement)

BritBox:
- Current monthly price (if stated)
- Current annual price (if stated)
- Free-trial language is non-absolute (eligibility varies by
  account/promo — never a bare guarantee)
- Affiliate link correct: c984b526-fff5-46bf-af6d-68abb4a6a5d2?tag=britishtvhub-20
- Featured titles list is current

Acorn TV:
- Monthly price (if stated)
- Annual price (if stated)
- Trial-availability language is non-absolute
- Affiliate link correct: c8382769-b3fd-49e8-818c-021154583c89?tag=britishtvhub-20

PBS:
- Passport information accurate (what it unlocks, not a specific price
  unless verified same-day)
- Membership wording accurate, not overstated

Netflix: never listed as a platform anywhere (standing rule)

Prime Video: current availability accurate (channel vs. included)

Tubi: current availability accurate; flag anything not re-verified in the
last month

Pluto TV: current availability accurate; every claim carries an
"availability checked [month/year]" note since FAST-channel catalogs
change often

## PART 4 — Geography

- Counties named correctly
- Cities named correctly
- Villages named correctly
- Regions named correctly
- Islands named correctly
- Countries named correctly
- Filming locations accurate and sourced (not guessed)

## PART 5 — Quotations

Per the absolute site rule above: there should be zero direct quotations
anywhere on the site. This section exists only to catch violations, not to
police wording, punctuation, or sourcing of a quote that should never have
been added.

- Confirm zero direct quotations found (see regex checks above)
- Any hit gets removed or paraphrased in the same edit that finds it —
  don't leave a flagged quote live pending a later pass

## PART 6 — Historical facts

- Dates correct
- Historical events described accurately
- Awards correct and specific
- Broadcasting history correct (original network, revivals, etc.)
- Novel publication history correct

## PART 7 — Homepage

- Featured show accurate and current
- Featured book accurate and current
- Monthly recommendations rotated this month
- "Updated [Month Year]" marker matches the actual current month
- Release/premiere dates current (swap to evergreen copy once a premiere
  or finale has passed — see standing rule on temporary cards)
- Prices, if shown, current
- All homepage links resolve

## PART 8 — Affiliate audit

Amazon:
- Link resolves
- Affiliate tag britishtvhub-20 present (or Influencer Storefront path
  format, which doesn't use ?tag= — not a bug, see known non-issue below)
- Product still available/listed (not discontinued)

BritBox: link resolves
Acorn TV: link resolves
Audible: link resolves (if any Audible links exist on the site)
Kindle: link resolves (if any Kindle-specific links exist)

## PART 9 — Editorial accuracy: banned/superlative language

Remove or replace unsupported superlatives. Only flag when a superlative
pairs with a specific unverifiable number or unbacked factual claim —
vague, clearly-opinion editorial voice ("one of our favourites") is fine
and should be left alone.

Words/phrases to remove when used as unsupported absolute claims:
- Best / The Best
- Greatest
- Everyone loves / Everyone's favourite
- Perfect / Completely safe / Zero darkness (absolute suitability claims)
- Most popular
- Finest
- Largest
- Only (as in "the only show that…")
- Trusted by [specific number]
- Guaranteed
- Industry-leading / world-class / unmatched / unparalleled /
  fastest-growing

Replace with (attributed-opinion framing):
- One of our favourites
- Widely regarded
- Popular
- Acclaimed
- Recommended
- British TV Hub's pick / British TV Hub's top recommendation for X

```bash
grep -rniE "trusted by|guaranteed|industry.leading|world.class|unmatched|unparalleled|fastest.growing" *.html shows/*.html
grep -rniE "\bthe best\b|\bgreatest\b|\beveryone loves\b|\bperfect\b|\bmost popular\b|\bfinest\b|\blargest\b|\bonly show\b" *.html shows/*.html
```

## PART 10 — SEO (every page)

- H1 present and accurate
- Meta title present and accurate
- Meta description present and accurate
- Internal links relevant and working
- No broken links (see Part 11 runnable check)
- Image ALT text present and descriptive

## PART 11 — Navigation & links

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
Do the same with src="..." for images/scripts.

Known non-issue: JS template literals (${show.url}, ' + show.url + ')
inside script blocks false-positive on a naive regex — exclude anything
containing ${ or ' +.

```bash
for f in *.html shows/*.html; do grep -q "watch-list.html" "$f" || echo "MISSING watch-list nav: $f"; done
for f in *.html shows/*.html; do grep -q "gift-ideas.html" "$f" || echo "MISSING gift-ideas nav: $f"; done
for f in *.html shows/*.html; do grep -q "footer-brand.webp" "$f" || echo "MISSING standard footer: $f"; done
grep -roh "G-[A-Z0-9]*" *.html shows/*.html | sort -u   # should return exactly one GA ID: G-P1L8CVNKS6
```

- Navigation consistent sitewide
- Footer consistent sitewide
- Related-guides / cross-link modules present where expected
- CTA button styling and wording consistent (gold pill style; no bare
  "Start Free Trial" — see Part 3)

## PART 12 — Visual audit

- No missing images (broken img src)
- Image quality acceptable (no obviously stretched/low-res assets)
- No broken formatting (unclosed tags, stray inline styles)
- Mobile layout reviewed (see viewport check below; deeper responsive QA
  needs an actual browser/device check, not just text)
- Desktop layout reviewed
- Card styling consistent sitewide ("Go Deeper" card shape: 12px rounded
  corners + hover-lift)

```bash
for f in *.html shows/*.html; do grep -q 'name="viewport"' "$f" || echo "MISSING viewport: $f"; done
```

## PART 13 — Monthly freshness

- Current month shown correctly wherever a month is referenced
- "New this month" / featured recommendations reflect the actual current
  month
- Release/premiere dates current
- Prices current (if shown)
- Affiliate offers current (no expired promo language)

```bash
grep -rl "July 2026" *.html shows/*.html   # swap for the actual previous month; adjust the search term each cycle
```
Known non-issue: privacy.html's "Last Updated: [month]" is a legal date —
only bump it when the policy text actually changes, not automatically.

## PART 14 — Triple verification

Every factual statement that matters should be checked against, in this
order of preference:

1. Official broadcaster
2. Official streaming service
3. Official publisher or author

If those aren't available:

4. Production company
5. Official press release

Only if still needed:

6. One high-quality secondary source, used to confirm or resolve a
   disagreement between sources — not as a first-choice source

## PART 15 — Copyright & Editorial Compliance

Quotations — British TV Hub Editorial Standard:

- No quotations anywhere on the site.
- Do not quote books.
- Do not quote television dialogue.
- Do not quote publishers' descriptions.
- Do not quote streaming-service marketing copy.
- Do not quote reviews.
- Do not quote interviews.
- Do not quote author websites.
- Do not use epigraphs.
- Do not use "famous lines" from television shows.

Required approach:

- Write every description in original British TV Hub editorial voice.
- Summarize rather than quote.
- Attribute facts, never copy wording.
- Keep all copy unique and independently written.

Add this section to every Monthly Audit Summary — Copyright & Editorial
Review:

- No quotations found anywhere on the site.
- No copied publisher descriptions.
- No copied streaming-service descriptions.
- No copied Amazon descriptions.
- No copyright concerns identified.
- Editorial copy remains original throughout.

## PART 16 — Naming & Styling Consistency

Ensure every page follows the same editorial conventions.

- Show titles are styled consistently.
- Book titles are styled consistently.
- Streaming service names are consistent (BritBox, Acorn TV, PBS Passport,
  etc.).
- Character names use the same spelling everywhere.
- Author names are identical across all pages.

## PART 17 — Evergreen Content Audit

Avoid language that becomes outdated.

Remove or update:

- "Coming soon"
- "New this month"
- "Next week"
- "Recently added"
- "Currently available"
- "Premieres today"

If time-sensitive wording is necessary:

- Include an "Updated [Month Year]" date.
- Add a reminder to revisit the page after the relevant event.

## PART 18 — Internal Consistency Audit

The same show should never be described differently on different pages
unless there is a reason. Example: if Vera is described on one page as "A
Northumberland detective drama," it should not appear elsewhere as "A
crime series set in Newcastle" unless the difference is intentional and
accurate.

Audit:

- Show descriptions
- Book descriptions
- Author biographies
- Streaming recommendations

## PART 19 — Link Integrity Audit

Every link.

Internal:
- No 404s
- No redirects
- HTTPS
- Correct anchor text

External:
- Publisher links
- Streaming links
- Affiliate links
- Amazon links

## PART 20 — Grammar & Style Audit

Every page:

- No spelling mistakes.
- No punctuation errors.
- No repeated wording.
- No awkward sentences.
- No inconsistent capitalization.
- Oxford comma usage is consistent (or consistently omitted — choose one
  style).
- Headings follow a consistent capitalization style.

## PART 21 — Reader Trust Audit

Review every page from a visitor's perspective. Ask:

- Would a reader trust this statement?
- Is there any exaggeration?
- Does anything sound like marketing instead of editorial?
- Is the wording clear about opinion versus fact?
- Would an expert agree with this description?

## PART 22 — AI Hallucination Check

Because some content may have originated from AI-assisted drafting, check
for:

- Invented awards.
- Invented cast members.
- Invented filming locations.
- Invented episode counts.
- Invented publication dates.
- Invented streaming availability.
- Invented trivia.
- Composite or merged plots from different series.
- Unsourced "fun facts."

## PART 23 — Editorial Voice Audit

Every page should sound like British TV Hub.

- Friendly but authoritative.
- Informative, not promotional.
- Original wording throughout.
- Consistent tone across pages.
- No clickbait headlines.
- No sensational language.

## PART 24 — Accessibility Audit

- Images have descriptive alt text.
- Headings follow a logical order (H1 → H2 → H3).
- Link text is descriptive (avoid "Click here").
- Colour contrast meets accessibility guidelines.
- Keyboard navigation works where applicable.

## PART 25 — Final Editorial Sign-Off

Before any page is published or updated:

- Facts verified.
- Internal links checked.
- External links checked.
- Affiliate links tested.
- Copyright review completed.
- Original copy confirmed.
- Grammar checked.
- Formatting reviewed.
- Accessibility reviewed.
- Editorial voice confirmed.
- Page reviewed on desktop.
- Page reviewed on mobile.
- Ready to publish.

## Known false-positive traps (don't "fix" these)

- American spellings that are actually code, not copy: center, color,
  behavior in CSS/JS (text-align: center, scroll-behavior: smooth) are the
  only valid keyword form — leave them.
- "Organization" inside script type="application/ld+json" is a fixed
  schema.org vocabulary term — leave it.
- footer-brand.webp's alt text ("...their favorite television series") is
  baked into the image file and was reviewed/accepted — leave the
  American spelling there.
- Amazon Influencer Storefront links (amazon.com/shop/influencer-*) don't
  use ?tag= — that's a different affiliate program tied to the URL path
  itself, not a missing tag.
- BritBox listed as a UK platform is a recurring real error (BritBox UK
  stopped existing as a standalone service in April 2024, absorbed into
  ITVX Premium) — this is NOT a false positive, always flag and fix it:
  ```python
  import json
  d = json.load(open('shows-database.json'))
  print([s['title'] for s in d if any(x['name']=='BritBox' for x in s.get('uk',[]))])
  ```
  Should return an empty list. If removing it leaves a show's UK region
  with zero platforms, verify a real replacement via JustWatch UK before
  removing — don't leave it empty on a guess.

## Automated pipeline context

scripts/fact_check.py runs via GitHub Actions on the 1st and 15th of each
month, checking a rotating batch of shows-database.json entries,
britbox-new.json / acorn-new.json, and embedded schema.org claims. It
auto-applies confident streaming-platform corrections and opens a GitHub
Issue listing what was auto-fixed vs. what still needs a human look. Check
fact-check-log.json's most recent entry for applied_fixes and issues
before assuming the database is current — only ~10 shows get checked per
run, so full coverage of all ~340+ shows takes months. This automated
pipeline is a supplement to the manual weekly audit, not a replacement for
it.

## Audit report format

Every audit concludes with a short report using this structure:

- Overall Accuracy Score (rough %, or a qualitative read if a number isn't
  meaningful)
- Pages Audited
- Number of Statements Verified
- Confirmed Factual Errors
- Needs Updating
- Unsupported Claims
- Conflicting Sources
- Affiliate-Link Issues
- Quick Fixes (under 30 minutes to resolve)
- Fix First (highest-priority corrections — usually the Confirmed Factual
  Errors and any Needs-Updating item that's already past its trigger date)

Copyright & Editorial Review (Part 15 summary — include every audit):

- No quotations found anywhere on the site.
- No copied publisher descriptions.
- No copied streaming-service descriptions.
- No copied Amazon descriptions.
- No copyright concerns identified.
- Editorial copy remains original throughout.

---

Last full sitewide run: August 2, 2026 (accuracy audit covering
Unforgotten platform/cast, homepage overreach claim, cozy-mystery absolute
claims, Murdoch/Brokenwood classification, Pluto TV caveats, and sitewide
"Start Free Trial" wording — see git log commit 97c42e2).
