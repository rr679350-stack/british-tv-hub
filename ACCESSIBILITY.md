# Accessibility review — 6 October 2026

## Scope and evidence
Reviewed source for all 202 HTML files and seven existing shared CSS/JavaScript files at commit c89bd016c0746177d44b34113d12f1b7582757bb. This inventory includes newsletter archives/templates, the error page and checkout redirect. The owner reported zero WAVE errors on the homepage before this sitewide update. Other live pages have not been verified with WAVE.

## Corrections
- Static accessible names for repeated search inputs and newsletter anti-spam fields.
- Decorative SVGs hidden from assistive technology; title for the embedded Ask Tilly iframe.
- One main-content landmark per page and skip links on pages with navigation.
- Shared keyboard focus styling, reduced-motion rules and readable footer/metadata text.
- Increased faint text contrast on dark page/card backgrounds; scroll-reveal content stays visible.
- Quiz focus moves to each question and the result; repeated activation during transitions is ignored.
- Show finder combobox exposes options, current selection, expanded state and Escape dismissal.
- Watch-list disclosures expose expanded/selected states and return focus after selection or Escape.
- Shared treatment of the dynamically inserted decorative Chatbase loading spinner.

## Validation performed
- Parsed all 202 HTML files: one main landmark per page; no missing image alt attributes, form names or iframe titles; skip targets resolve; no nested main landmarks.
- Preserved existing form/image counts and external script references.
- JavaScript syntax checks and simulated DOM tests for all four quizzes, the show finder and watch-list disclosures.
- Muted text #c1cadd against card background #363f58: 6.35:1.

## Live rendered pass — 11 October 2026
A headless Chromium could be installed this session, so the pages below were rendered and scanned with axe-core (WCAG 2.0/2.1 A & AA rules) against the exact commit live at the time (`594776c`), served locally since this sandbox can't reach the public internet. `meet-tilly.html` was dropped from the original list — the page no longer exists (Tilly was retired in favor of quiz.html, see /areas/tilly-chatbot notes).

**Result: 0 confirmed violations** on all 16 pages checked:
/shows/vera.html, /shows/ludwig.html, /shows-index.html, /watch-list.html, /which-subscription.html, /streaming.html, /books.html, /gift-guide-hub.html, /quiz.html, /village-quiz.html, /british-tv-personality-quiz.html, /halloween-mystery-builder.html, /community-snug.html, /what-are-you-watching.html, /dark-october-night-mysteries.html, /newsletters/sunday-picks-ludwig-returns.html.

(An initial pass before the page had finished painting returned false contrast failures — near-white-on-near-white — caused by reading computed styles mid-render in headless Chromium, not a real defect. Resolved by waiting for the page to settle before scanning; confirmed against a screenshot.)

Two items axe flags as "incomplete" (can't auto-resolve, not failures) on every page and are fine as-is:
- `color-contrast` on text sitting over a CSS gradient card background — axe can't compute contrast against a gradient automatically; spot-checked visually and the text always lands on the gradient's dark end.
- `label-content-name-mismatch` on icon-only links (☕ support link, Facebook/Pinterest/Email icons) — visible content is an emoji/icon, not text, so axe can't auto-compare it to the aria-label; this is standard, compliant practice for icon buttons.

Also checked: mobile reflow at 375px width on all 16 pages — no horizontal overflow on any of them.

## Still outstanding
- Keyboard-only operation and screen-reader announcement testing (needs a human with real AT, not just DOM/axe checks).
- Video captions on embedded trailers.
- The third-party Chatbase widget and any payment flow — out of scope for this repo's source/render review (cross-origin content).
- The remaining ~186 pages not in the sample above haven't had a live render pass, only the Oct 6 source review.
