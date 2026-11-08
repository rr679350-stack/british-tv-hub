#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates 10 new /shows/*.html guide pages for britishtvhub.com, following the
Standard Series Guide Template (see shows/lewis.html as canonical reference,
and /areas/britishtv-hub-website.md for the spec). Built November 2026.
"""
import os

BRITBOX = "https://www.amazon.com/gp/video/channel/c984b526-fff5-46bf-af6d-68abb4a6a5d2?tag=britishtvhub-20"
ACORN = "https://www.amazon.com/gp/video/channel/c8382769-b3fd-49e8-818c-021154583c89?tag=britishtvhub-20"
MASTERPIECE = "https://www.amazon.com/gp/video/channel/cf297d60-2200-420a-b036-5b78d653da5a?tag=britishtvhub-20"

def buy_link(title):
    q = title.replace(" ", "+").replace("&", "%26")
    return f"https://www.amazon.com/s?k={q}+TV+series&tag=britishtvhub-20"

HEAD_STYLE = open(os.path.join(os.path.dirname(__file__), "_shared_head_style.html"), encoding="utf-8").read()
NAV_BLOCK = open(os.path.join(os.path.dirname(__file__), "_shared_nav.html"), encoding="utf-8").read()
FOOTER_BLOCK = open(os.path.join(os.path.dirname(__file__), "_shared_footer.html"), encoding="utf-8").read()

def card(badge_class, badge_text, title_html, desc, tags, aside_label, aside_rows, aside_link=None, aside_link_text=None, aside_link2=None, aside_link2_text=None):
    tags_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
    rows_html = "".join(f'<div class="aside-row"><span class="aside-key">{k}</span><span class="aside-val">{v}</span></div>' for k, v in aside_rows)
    link_html = ""
    if aside_link:
        link_html += f'<a href="{aside_link}" class="aside-link" target="_blank" rel="noopener">{aside_link_text}</a>'
    if aside_link2:
        link_html += f'<a href="{aside_link2}" class="aside-link-secondary" target="_blank" rel="noopener">{aside_link2_text}</a>'
    return f'''  <div class="show-card">
    <div class="show-card-inner">
      <div>
        <div class="show-badge {badge_class}" style=";color:#f0e8d4 !important;opacity:1 !important;">{badge_text}</div>
        <h3 class="show-title">{title_html}</h3>
        <p class="show-desc">{desc}</p>
        <div class="show-tags">{tags_html}</div>
      </div>
      <div class="show-aside">
        <div class="aside-label">{aside_label}</div>
        {rows_html}
        {link_html}
      </div>
    </div>
  </div>
'''

def section_header(title_html):
    return f'  <div class="section-header">\n    <h2>{title_html}</h2>\n  </div>\n\n'

def faq_card(badge, question, answer, qa_rows):
    rows_html = "".join(f'<div class="aside-row"><span class="aside-key">{k}</span><span class="aside-val">{v}</span></div>' for k, v in qa_rows)
    return f'''  <div class="show-card">
    <div class="show-card-inner">
      <div>
        <div class="show-badge badge-classic" style=";color:#f0e8d4 !important;opacity:1 !important;">{badge}</div>
        <h3 class="show-title">{question}</h3>
        <p class="show-desc">{answer}</p>
      </div>
      <div class="show-aside">
        <div class="aside-label">Quick Answer</div>
        {rows_html}
      </div>
    </div>
  </div>
'''

def build_page(show):
    slug = show["slug"]
    title = show["title"]
    meta_desc = show["meta_desc"]
    url = f"https://britishtvhub.com/shows/{slug}.html"
    eyebrow = show["eyebrow"]
    tags = show["tags"]

    head = f'''<!DOCTYPE html>
<html lang="en">
<head>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="shortcut icon" href="/favicon.ico">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-P1L8CVNKS6"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', 'G-P1L8CVNKS6');
</script>

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}: Where to Watch in the US | British TV Hub</title>
  <meta name="description" content="{meta_desc}">
  <link rel="canonical" href="{url}">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "{title}: Where to Watch in the US | British TV Hub",
  "description": "{meta_desc}",
  "url": "{url}",
  "dateModified": "2026-11-07",
  "isPartOf": {{
    "@type": "WebSite",
    "name": "British TV Hub",
    "url": "https://britishtvhub.com/"
  }}
}}
</script>

<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}: Where to Watch in the US | British TV Hub">
<meta property="og:description" content="{meta_desc}">
<meta property="og:image" content="https://britishtvhub.com/BTH_Logo.png">
<meta property="og:image:alt" content="British TV Hub — best British TV dramas and mysteries guide">
<meta property="og:site_name" content="British TV Hub">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{title}: Where to Watch in the US | British TV Hub">
<meta name="twitter:description" content="{meta_desc}">
<meta name="twitter:image" content="https://britishtvhub.com/BTH_Logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Crimson+Text:ital,wght@0,400;0,600;1,400&family=Raleway:wght@400;500;600&display=swap" rel="stylesheet">
{HEAD_STYLE}
{show["tvseries_jsonld"]}
{show["faq_jsonld"]}
<link rel="stylesheet" href="/hub-cards.css">
<link rel="stylesheet" href="/accessibility.css?v=1">
<script src="/accessibility.js?v=1" defer></script>
</head>
<body>
<a class="hub-skip-link" href="#hub-content-start">Skip to content</a>

{NAV_BLOCK}
<div role="main" class="hub-main-landmark">
<script>
function toggleMobileNav(){{
  var nav = document.querySelector('nav.site-nav-std');
  var btn = document.getElementById('nav-hamburger-btn');
  if(!nav || !btn) return;
  var isOpen = nav.classList.toggle('mobile-menu-open');
  btn.classList.toggle('open', isOpen);
  btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
}}
</script>
<script>
function toggleDiscoverMenu(){{
  var m = document.getElementById('nav-discover-menu');
  if(!m) return;
  m.style.display = (m.style.display === 'none' || !m.style.display) ? 'flex' : 'none';
}}
document.addEventListener('click', function(e){{
  var menu = document.getElementById('nav-discover-menu');
  var toggle = document.querySelector('.nav-dropdown-toggle');
  if(menu && toggle && !menu.contains(e.target) && !toggle.contains(e.target)){{
    menu.style.display = 'none';
  }}
}});
</script>

<div class="breadcrumb">
  <a href="https://britishtvhub.com/">Home</a>
  <span>&middot;</span>
  <a href="https://britishtvhub.com/shows-index.html">Browse Shows</a>
  <span>&middot;</span>
  {title}
</div>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://britishtvhub.com/"}},
    {{"@type": "ListItem", "position": 2, "name": "Browse Shows", "item": "https://britishtvhub.com/shows-index.html"}},
    {{"@type": "ListItem", "position": 3, "name": "{title}", "item": "{url}"}}
  ]
}}
</script>

<div style="position:relative;overflow:hidden;min-height:280px;display:flex;align-items:center;background:linear-gradient(135deg,#232b45 0%,#131926 100%);border-bottom:1px solid rgba(201,168,76,0.15);">
  <div style="position:relative;z-index:2;padding:56px 40px 40px;max-width:680px;">
    <p class="show-eyebrow" style="margin-bottom:10px;">{eyebrow}</p>
    <h1 class="show-title" style="margin-bottom:0;" id="hub-content-start" tabindex="-1">{title}</h1>
  </div>
</div>

<div class="page-wrap">

  <div class="show-tags">
    {"".join(f'<span class="tag">{t}</span>' for t in tags)}
  </div>

  <div class="wl-dropdown" data-slug="{slug}">
    <button type="button" class="wl-dd-toggle"><span class="wl-dd-label">Add to Watch List</span> <span class="wl-dd-caret">&#9662;</span></button>
    <div class="wl-dd-menu">
      <button type="button" class="wl-dd-item" data-status="want">Want to Watch</button>
      <button type="button" class="wl-dd-item" data-status="watching">Watching</button>
      <button type="button" class="wl-dd-item" data-status="finished">Finished</button>
    </div>
  </div>

  <div class="hub-card"><p class="show-description">{show["description"]}</p></div>

  <hr class="divider">

{section_header(show["viewer_guide_heading"])}
{show["viewer_guide_card"]}
  <hr class="divider">

{show["watch_block"]}

{section_header("Best Episodes, <em>Ranked</em>")}
{show["episode_cards"]}
  <hr class="divider">

{section_header("Main Characters <em>and Cast</em>")}
{show["cast_cards"]}
  <hr class="divider">

{section_header("What Makes the Series <em>Special</em>")}
{show["special_cards"]}
  <hr class="divider">

{section_header("Setting and <em>Filming Locations</em>")}
{show["setting_card"]}
{show["books_section"]}
{section_header("Frequently Asked <em>Questions</em>")}
{show["faq_cards"]}
  <p style="font-family:'Raleway',sans-serif;font-size:11px;color:var(--text-dim, #b0bcd4);margin:8px 0 2rem;font-style:italic;">Fact-checked and streaming availability checked November 2026. Spot an error or an outdated streaming link? Send a correction via the contact page.</p>

  <hr class="divider">

{section_header("Related <em>Guides</em>")}
  <div class="related-links">
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px;">
    <a href="https://britishtvhub.com/shows-index.html" style="display:flex;flex-direction:column;height:100%;background:#363f58;border:1px solid rgba(201,168,76,0.2);border-radius:12px;overflow:hidden;text-decoration:none;transition:transform .2s ease,border-color .2s ease;padding:22px 24px 26px;">
      <div style="font-family:'Playfair Display',serif;font-size:1.05rem;color:var(--text,#f0e8d4);margin:0 0 10px;line-height:1.3;">Browse All Shows</div>
      <div style="font-family:'Crimson Text',serif;font-size:14.5px;color:var(--text-muted, #c1cadd);line-height:1.55;margin:0 0 16px;">Every British mystery and drama on the site, organized by genre and platform.</div>
      <span style="display:inline-block;align-self:flex-start;margin-top:auto;font-family:'Raleway',sans-serif;font-size:11px;font-weight:600;letter-spacing:1.5px;text-transform:uppercase;color:#1a2135;background:var(--gold,#c9a96e);padding:10px 18px;border-radius:2px;">Read Guide &rarr;</span>
    </a>
    <a href="https://britishtvhub.com/cozy-british-tv-shows-thanksgiving.html" style="display:flex;flex-direction:column;height:100%;background:#363f58;border:1px solid rgba(201,168,76,0.2);border-radius:12px;overflow:hidden;text-decoration:none;transition:transform .2s ease,border-color .2s ease;padding:22px 24px 26px;">
      <div style="font-family:'Playfair Display',serif;font-size:1.05rem;color:var(--text,#f0e8d4);margin:0 0 10px;line-height:1.3;">25 Cozy British TV Shows for Thanksgiving</div>
      <div style="font-family:'Crimson Text',serif;font-size:14.5px;color:var(--text-muted, #c1cadd);line-height:1.55;margin:0 0 16px;">Where this guide belongs on the holiday watchlist.</div>
      <span style="display:inline-block;align-self:flex-start;margin-top:auto;font-family:'Raleway',sans-serif;font-size:11px;font-weight:600;letter-spacing:1.5px;text-transform:uppercase;color:#1a2135;background:var(--gold,#c9a96e);padding:10px 18px;border-radius:2px;">Read Guide &rarr;</span>
    </a>
    <a href="https://britishtvhub.com/streaming.html" style="display:flex;flex-direction:column;height:100%;background:#363f58;border:1px solid rgba(201,168,76,0.2);border-radius:12px;overflow:hidden;text-decoration:none;transition:transform .2s ease,border-color .2s ease;padding:22px 24px 26px;">
      <div style="font-family:'Playfair Display',serif;font-size:1.05rem;color:var(--text,#f0e8d4);margin:0 0 10px;line-height:1.3;">Where to Watch</div>
      <div style="font-family:'Crimson Text',serif;font-size:14.5px;color:var(--text-muted, #c1cadd);line-height:1.55;margin:0 0 16px;">The full guide to which streaming service has what.</div>
      <span style="display:inline-block;align-self:flex-start;margin-top:auto;font-family:'Raleway',sans-serif;font-size:11px;font-weight:600;letter-spacing:1.5px;text-transform:uppercase;color:#1a2135;background:var(--gold,#c9a96e);padding:10px 18px;border-radius:2px;">Read Guide &rarr;</span>
    </a>
  </div>
  </div>

</div>

{FOOTER_BLOCK}
'''
    return head

# Data is defined in build_show_guides_nov7_data.py to keep this file manageable
from build_show_guides_nov7_data import SHOWS

if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(__file__), "..", "shows")
    for show in SHOWS:
        html = build_page(show)
        path = os.path.join(out_dir, f"{show['slug']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", path)
