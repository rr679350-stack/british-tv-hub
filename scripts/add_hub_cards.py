import re

CARD_TMPL = '''  <a href="/{href}" style="display:flex;flex-direction:column;height:100%;background:#363f58;border:1px solid rgba(201,168,76,0.2);border-radius:12px;overflow:hidden;text-decoration:none;transition:transform .2s ease,border-color .2s ease;">
    <img loading="lazy" src="/{img}" alt="{alt}" style="width:100%;height:170px;object-fit:cover;display:block;">
    <div style="padding:24px;display:flex;flex-direction:column;flex:1;">
      <div style="font-family:'Playfair Display',serif;font-size:24px;color:var(--cream);margin-bottom:10px;">{title}</div>
      <p style="font-size:16px;color:var(--text-light);line-height:1.6;margin:0 0 16px;">{desc}</p>
      <span style="display:inline-block;align-self:flex-start;margin-top:auto;font-family:'Raleway',sans-serif;font-size:12px;font-weight:600;letter-spacing:1.5px;text-transform:uppercase;color:#1a2135;background:var(--gold);padding:9px 18px;border-radius:2px;">Explore &rarr;</span>
    </div>
  </a>
'''

CARDS = [
    dict(href="shows-like-silent-witness-tv.html", img="tense-british-crime-drama-hero.webp",
         alt="A forensic pathology lab with evidence under examination",
         title="Shows Like Silent Witness", desc="Meticulous forensic crime drama for fans of evidence-led investigation."),
    dict(href="shows-like-sherwood-tv.html", img="modern-crime-procedurals-hero.webp",
         alt="An unmarked police car with blue lights on, parked on a wet city street at night",
         title="Shows Like Sherwood", desc="Place-driven British crime dramas rooted in real community and history."),
    dict(href="shows-like-the-gold-tv.html", img="the-gold-s2-boyce.webp",
         alt="A detective reviewing case files from The Gold, based on the Brink's-Mat robbery",
         title="Shows Like The Gold", desc="True-crime ensemble dramas for fans of sprawling, fact-based heists."),
    dict(href="shows-like-dalgliesh-tv.html", img="dark-october-night-hero.webp",
         alt="A moody, lamplit English street at night evoking a literary detective mystery",
         title="Shows Like Dalgliesh", desc="Literary, unhurried detective drama for fans of P.D. James's poet-policeman."),
    dict(href="shows-like-victoria-tv.html", img="shows-like-downton-abbey-hero.webp",
         alt="A grand English country manor house at sunset",
         title="Shows Like Victoria", desc="Lavish period romance for fans of a young monarch balancing duty and love."),
    dict(href="shows-like-poldark-tv.html", img="shows-like-downton-abbey-hero.webp",
         alt="A grand English country manor house at sunset",
         title="Shows Like Poldark", desc="Sweeping costume drama for fans of Cornish landscapes and family sagas."),
    dict(href="shows-like-the-chelsea-detective-tv.html", img="best-british-mystery-shows-2026-hero.webp",
         alt="A houseboat moored on the Thames at dusk, evoking a London-set detective mystery",
         title="Shows Like The Chelsea Detective", desc="Gentle, character-led mysteries for fans of a houseboat-dwelling detective."),
    dict(href="shows-like-trigger-point-tv.html", img="modern-crime-procedurals-hero.webp",
         alt="An unmarked police car with blue lights on, parked on a wet city street at night",
         title="Shows Like Trigger Point", desc="High-tension British thrillers for fans of life-or-death pressure."),
    dict(href="shows-like-madame-blanc-mysteries-tv.html", img="fall-preview-madame-blanc-s5-keyart.webp",
         alt="An antiques shop on a sun-soaked French Riviera street",
         title="Shows Like The Madame Blanc Mysteries", desc="Sun-soaked, cozy amateur-sleuth mysteries for fans of a well-trained eye for detail."),
    dict(href="shows-like-lynley-tv.html", img="best-british-mystery-shows-2026-hero.webp",
         alt="A case file and magnifying glass on an antique desk, evoking a classic detective partnership",
         title="Shows Like Lynley", desc="Class-contrast detective partnerships for fans of mismatched investigators."),
]

path = "shows-like.html"
html = open(path, encoding="utf-8").read()

new_cards = "\n" + "\n".join(CARD_TMPL.format(**c) for c in CARDS)

marker = '  <a href="/hidden-dramas.html"'
idx = html.index(marker)
end_marker = "</a>\n"
end_idx = html.index(end_marker, idx) + len(end_marker)

html = html[:end_idx] + new_cards + html[end_idx:]

open(path, "w", encoding="utf-8").write(html)
print("inserted", len(CARDS), "cards")
