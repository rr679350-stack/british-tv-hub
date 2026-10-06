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

## Remaining verification
A browser executable could not be installed because its download was blocked. Therefore this is a source review and logic-test pass, not a rendered sitewide WCAG conformance finding.

Run live WAVE checks on the following distinct layouts, then inspect all flagged elements:
- /shows/vera.html and /shows/ludwig.html
- /shows-index.html, /watch-list.html and /which-subscription.html
- /streaming.html, /books.html and /gift-guide-hub.html
- /quiz.html, /village-quiz.html, /british-tv-personality-quiz.html and /halloween-mystery-builder.html
- /community-snug.html, /what-are-you-watching.html and /meet-tilly.html
- /dark-october-night-mysteries.html and a newsletter archive

Also verify keyboard-only operation, screen-reader announcements, mobile/zoom reflow, video captions and the cross-origin chat contents. Third-party chat/payment contents are outside the repository's source review.
