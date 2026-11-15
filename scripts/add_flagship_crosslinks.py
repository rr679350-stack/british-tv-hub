import os

CARD_TMPL = '''
    <a href="https://britishtvhub.com/shows-like-{slug}-tv.html" style="display:flex;flex-direction:column;height:100%;background:#363f58;border:1px solid rgba(201,168,76,0.2);border-radius:12px;overflow:hidden;text-decoration:none;transition:transform .2s ease,border-color .2s ease;">
      <img src="/{img}" alt="{alt}" loading="lazy" style="width:100%;height:130px;object-fit:cover;display:block;">
      <div style="padding:22px 24px 26px;display:flex;flex-direction:column;flex:1;">
        <div style="font-family:'Playfair Display',serif;font-size:1.05rem;color:var(--text,#f0e8d4);margin:0 0 10px;line-height:1.3;">Shows Like {flagship}</div>
        <div style="font-family:'Crimson Text',serif;font-size:14.5px;color:var(--text-muted, #c1cadd);line-height:1.55;margin:0 0 16px;">{desc}</div>
        <span style="display:inline-block;align-self:flex-start;margin-top:auto;font-family:'Raleway',sans-serif;font-size:11px;font-weight:600;letter-spacing:1.5px;text-transform:uppercase;color:#1a2135;background:var(--gold,#c9a96e);padding:10px 18px;border-radius:2px;">Read Guide &rarr;</span>
      </div>
    </a>'''

TARGETS = [
    dict(file="silent-witness", slug="silent-witness", flagship="Silent Witness",
         img="tense-british-crime-drama-hero.webp", alt="A forensic pathology lab with evidence under examination",
         desc="More forensic and investigative crime drama to watch next."),
    dict(file="sherwood", slug="sherwood", flagship="Sherwood",
         img="modern-crime-procedurals-hero.webp", alt="An unmarked police car with blue lights on, parked on a wet city street at night",
         desc="More place-driven British crime drama rooted in real community."),
    dict(file="dalgliesh", slug="dalgliesh", flagship="Dalgliesh",
         img="dark-october-night-hero.webp", alt="A moody, lamplit English street at night evoking a literary detective mystery",
         desc="More literary, unhurried detective drama to watch next."),
    dict(file="the-chelsea-detective", slug="the-chelsea-detective", flagship="The Chelsea Detective",
         img="best-british-mystery-shows-2026-hero.webp", alt="A houseboat moored on the Thames at dusk, evoking a London-set detective mystery",
         desc="More gentle, character-led detective mysteries to watch next."),
    dict(file="trigger-point", slug="trigger-point", flagship="Trigger Point",
         img="modern-crime-procedurals-hero.webp", alt="An unmarked police car with blue lights on, parked on a wet city street at night",
         desc="More high-tension British thrillers to watch next."),
    dict(file="lynley", slug="lynley", flagship="Lynley",
         img="best-british-mystery-shows-2026-hero.webp", alt="A case file and magnifying glass on an antique desk, evoking a classic detective partnership",
         desc="More mismatched detective partnerships to watch next."),
    dict(file="victoria", slug="victoria", flagship="Victoria",
         img="shows-like-downton-abbey-hero.webp", alt="A grand English country manor house at sunset",
         desc="More lavish period romance to watch next."),
    dict(file="poldark", slug="poldark", flagship="Poldark",
         img="shows-like-downton-abbey-hero.webp", alt="A grand English country manor house at sunset",
         desc="More sweeping costume drama to watch next."),
]

os.chdir(os.path.join(os.path.dirname(__file__), "..", "shows"))

marker = "<!-- Sunday Picks signup (Mailchimp) -->"

for t in TARGETS:
    path = f"{t['file']}.html"
    html = open(path, encoding="utf-8").read()
    idx_marker = html.index(marker)
    idx_last_a = html.rfind("</a>", 0, idx_marker)
    insert_at = idx_last_a + len("</a>")
    card = CARD_TMPL.format(slug=t["slug"], flagship=t["flagship"], img=t["img"], alt=t["alt"], desc=t["desc"])
    html = html[:insert_at] + card + html[insert_at:]
    open(path, "w", encoding="utf-8").write(html)
    print("updated", path)
