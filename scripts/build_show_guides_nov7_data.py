# -*- coding: utf-8 -*-
"""Per-show structured data for build_show_guides_nov7.py. Built November 2026."""

BRITBOX = "https://www.amazon.com/gp/video/channel/c984b526-fff5-46bf-af6d-68abb4a6a5d2?tag=britishtvhub-20"
ACORN = "https://www.amazon.com/gp/video/channel/c8382769-b3fd-49e8-818c-021154583c89?tag=britishtvhub-20"
MASTERPIECE = "https://www.amazon.com/gp/video/channel/cf297d60-2200-420a-b036-5b78d653da5a?tag=britishtvhub-20"

def buy_link(title):
    q = title.replace(" ", "+").replace("&", "%26")
    return f"https://www.amazon.com/s?k={q}+TV+series&tag=britishtvhub-20"

def watch_block(service_name, service_link, detail, also=None, buy_title=None, checked="November 2026"):
    also_html = f'<div class="watch-free"><strong>Also available:</strong> {also}</div>' if also else ""
    buy_html = ""
    if buy_title:
        buy_html = f'''  <div class="watch-card">
    <p class="watch-label">Prefer to own it?</p>
    <p class="watch-service">Buy the Series</p>
    <p class="watch-detail">Individual/complete-series options available &middot; Check current sellers and formats</p>
    <a href="{buy_link(buy_title)}" class="watch-btn" target="_blank" rel="noopener">Shop {buy_title} &rarr;</a>
  </div>
'''
    return f'''  <div class="watch-card">
    <p class="watch-label">Where to watch in the US</p>
    <p class="watch-service">{service_name}</p>
    <p class="watch-detail">{detail}</p>
    <a href="{service_link}" class="watch-btn" target="_blank" rel="noopener">Watch via {service_name} on Prime Video &rarr;</a>
    {also_html}
    <p style="font-family:'Raleway',sans-serif;font-size:11px;color:var(--text-dim, #b0bcd4);margin:10px 0 0;font-style:italic;">Streaming availability in the US can change. Check the linked service for the current season and episode selection. Checked {checked}.</p>
  </div>
{buy_html}'''

def card(badge_class, badge_text, title_html, desc, tags, aside_label, aside_rows, aside_link=None, aside_link_text=None):
    tags_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
    rows_html = "".join(f'<div class="aside-row"><span class="aside-key">{k}</span><span class="aside-val">{v}</span></div>' for k, v in aside_rows)
    link_html = f'<a href="{aside_link}" class="aside-link" target="_blank" rel="noopener">{aside_link_text}</a>' if aside_link else ""
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

def faq_jsonld(show_name, qa_pairs):
    import json
    entities = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa_pairs]
    data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities}
    return f'<script type="application/ld+json">\n{json.dumps(data, indent=2)}\n</script>'

def tvseries_jsonld(name, alt_name, description, genre, num_seasons, start, end, actors, url, creator_org="ITV Studios"):
    import json
    data = {
        "@context": "https://schema.org",
        "@type": "TVSeries",
        "name": name,
        "description": description,
        "genre": genre,
        "numberOfSeasons": num_seasons,
        "startDate": start,
        "actor": [{"@type": "Person", "name": a} for a in actors],
        "countryOfOrigin": {"@type": "Country", "name": "United Kingdom"},
        "url": url,
    }
    if alt_name:
        data["alternateName"] = alt_name
    if end:
        data["endDate"] = end
    return f'<script type="application/ld+json">\n{json.dumps(data, indent=2)}\n</script>'

SHOWS = []

# ============================================================ 1. DCI BANKS
SHOWS.append({
    "slug": "dci-banks",
    "title": "DCI Banks",
    "meta_desc": "Where to watch DCI Banks in the US. The complete guide to Stephen Tompkinson's adaptation of Peter Robinson's Inspector Banks novels, all five series.",
    "eyebrow": "British Crime Drama &middot; ITV &middot; 2010&ndash;2016 &middot; Complete Series",
    "tags": ["5 Series", "32 Episodes", "Stars Stephen Tompkinson", "Yorkshire", "Based on the Novels"],
    "description": "Stephen Tompkinson stars as DCI Alan Banks, a Yorkshire detective investigating murders across the fictional county of Eastvale, in this adaptation of Peter Robinson's long-running Inspector Banks novels. Andrea Lowe plays DS (later DI) Annie Cabbot, Banks's closest colleague, with Caroline Catz as DI Helen Morton. The series ran for a pilot plus five numbered series between 2010 and 2016, 32 episodes in total, before concluding as a planned final run. DCI Banks streams on BritBox in the US.",
    "viewer_guide_heading": "New Viewer's <em>Guide</em>",
    "viewer_guide_card": card("badge-new", "Where to Start", "Series 1, Episode 1, <em>Aftermath</em> (2010)",
        "The opening episode introduces DCI Banks as he investigates a case with disturbing links to a serial killer, establishing the partnership with DS Annie Cabbot that anchors the series.",
        ["Series 1", "2010"],
        "At a Glance", [("Watch Order", "Broadly case-of-the-week"), ("Cast Change", "DI Helen Morton joins later series")]),
    "watch_block": watch_block("BritBox", BRITBOX, "All 5 series &middot; Subscription required", buy_title="DCI Banks"),
    "episode_cards": (
        card("badge-essential", "1 &middot; Series 1 &middot; 2010", "<em>Aftermath</em>",
             "The series premiere, built around a disturbing serial-killer case that sets the tone for Banks's Yorkshire investigations and introduces his partnership with Annie Cabbot.",
             ["Series Premiere"], "At a Glance", [("Position", "Series 1, 2010"), ("Best For", "First-time viewers")],
             BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "2 &middot; Series 2", "<em>Friend of the Devil</em>",
               "A British TV Hub pick for its two-track investigation structure, pairing Banks's murder case with a separate inquiry led by Annie Cabbot.",
               ["Dual Investigation"], "At a Glance", [("Best For", "Fans of parallel plotting")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "3 &middot; Series 3", "<em>Playing with Fire</em>",
               "A British TV Hub pick notable for its fire-investigation plot and the way it widens the show's scope beyond a single Eastvale community.",
               ["Arson Investigation"], "At a Glance", [("Best For", "Procedural-minded viewers")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "4", "<em>Innocent Graves</em>",
               "A British TV Hub pick for its emotionally difficult case involving a local family, typical of the show's willingness to sit with the aftermath of a crime.",
               ["Character-Driven"], "At a Glance", [("Best For", "Viewers who prefer emotional weight to pure puzzle")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "5 &middot; Series 5 &middot; 2016", "<em>Wednesday's Child</em>",
               "A British TV Hub pick from the final series, showing the show's confident handling of its Yorkshire setting right through to the end of its run.",
               ["Final Series"], "At a Glance", [("Best For", "Viewers finishing the series")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
    ),
    "cast_cards": (
        card("badge-essential", "Lead", "Stephen Tompkinson", 'DCI Alan Banks &mdash; a Yorkshire detective balancing a demanding caseload with a complicated personal life, carried across all five series.', ["Lead Detective"], "At a Glance", [("Role", "DCI Alan Banks"), ("Appears", "Pilot and all 5 series")])
        + card("badge-essential", "Lead", "Andrea Lowe", 'DS, later DI, Annie Cabbot &mdash; Banks\'s closest colleague and frequent partner on investigations throughout the run.', ["Detective Sergeant/Inspector"], "At a Glance", [("Role", "DS/DI Annie Cabbot"), ("Appears", "All 5 series")])
        + card("badge-classic", "Joins Later Series", "Caroline Catz", "DI Helen Morton, joining the investigative team in the show's later series.", ["Detective Inspector"], "At a Glance", [("Role", "DI Helen Morton")])
    ),
    "special_cards": (
        card("badge-classic", "Setting as Character", "Yorkshire's Fictional Eastvale", "The series builds its own corner of Yorkshire around the fictional town of Eastvale, giving the investigations a consistent sense of place across five series.", ["Fictional Setting"], "At a Glance", [("Region", "Yorkshire")])
        + card("badge-classic", "Source Material", "Grounded in a Long-Running Novel Series", "Peter Robinson's Inspector Banks novels had already run for two decades by the time the show adapted them, giving the series a deep well of plots and characters to draw from.", ["Novel Adaptation"], "At a Glance", [("Novels", "20+ by 2010")])
        + card("badge-classic", "Planned Ending", "A Deliberate Final Series", "ITV confirmed Series 5 as the show's last outing in December 2015, giving the writers room to close out Banks's story on their own terms rather than being cut short.", ["Planned Conclusion"], "At a Glance", [("Confirmed", "December 2015")])
    ),
    "setting_card": card("badge-classic", "Setting &amp; Filming", "Yorkshire, England", "DCI Banks is set in the fictional Yorkshire town of Eastvale and was filmed on location around Leeds and Otley, giving the series a consistent regional identity distinct from the capital-set procedurals common elsewhere on British television.", ["Yorkshire, England"], "At a Glance", [("Region", "Yorkshire"), ("Filmed In", "Leeds, Otley")]),
    "books_section": "  " + f'''<div class="section-header">
    <h2>Books Behind the <em>Series</em></h2>
  </div>

''' + card("badge-classic", "Source Novels", "Peter Robinson's Inspector Banks Novels", "DCI Banks adapts Peter Robinson's long-running series of Inspector Banks crime novels, with screenwriter Robert Murphy adapting individual books and storylines for television across the show's run.", ["Novel Series"], "At a Glance", [("Author", "Peter Robinson"), ("Adapted By", "Robert Murphy")]) + "\n  <hr class=\"divider\">\n\n",
    "faq_cards": (
        faq_card("Status", "Is DCI Banks finished?", "Yes. DCI Banks concluded after a pilot and five numbered series in 2016, with ITV having confirmed Series 5 as a planned final run the previous December.", [("Status", "Complete"), ("Ended", "2016")])
        + faq_card("Episode Count", "How many episodes of DCI Banks are there?", "There are 32 episodes across the pilot and five numbered series, broadcast between 2010 and 2016.", [("Episodes", "32"), ("Series", "5 + pilot")])
        + faq_card("Source Material", "Is DCI Banks based on books?", "Yes. The series adapts Peter Robinson's Inspector Banks novels, with individual episodes and storylines drawn from specific books in the series.", [("Author", "Peter Robinson")])
        + faq_card("Streaming", "Where can I watch DCI Banks in the US?", "BritBox is DCI Banks's primary US streaming home, with all five series available to subscribers.", [("Primary", "BritBox")])
        + faq_card("Filming Location", "Where is DCI Banks filmed?", "DCI Banks was filmed on location in Yorkshire, primarily around Leeds and Otley, standing in for the fictional town of Eastvale.", [("Region", "Yorkshire"), ("Towns", "Leeds, Otley")])
        + faq_card("Cast", "Who plays DCI Banks?", "Stephen Tompkinson plays DCI Alan Banks throughout the series, with Andrea Lowe as DS/DI Annie Cabbot and Caroline Catz joining later as DI Helen Morton.", [("Lead", "Stephen Tompkinson")])
    ),
    "tvseries_jsonld": tvseries_jsonld("DCI Banks", None, "Stephen Tompkinson stars as DCI Alan Banks, a Yorkshire detective investigating murders across the fictional county of Eastvale, in this adaptation of Peter Robinson's Inspector Banks novels. A pilot and five numbered series broadcast from 2010 to 2016, 32 episodes in total.", "British Crime Drama", 5, "2010", "2016", ["Stephen Tompkinson", "Andrea Lowe"], "https://britishtvhub.com/shows/dci-banks.html"),
    "faq_jsonld": faq_jsonld("DCI Banks", [
        ("Is DCI Banks finished?", "Yes. DCI Banks concluded after a pilot and five numbered series in 2016, with ITV having confirmed Series 5 as a planned final run the previous December."),
        ("How many episodes of DCI Banks are there?", "There are 32 episodes across the pilot and five numbered series, broadcast between 2010 and 2016."),
        ("Is DCI Banks based on books?", "Yes. The series adapts Peter Robinson's Inspector Banks novels, with individual episodes and storylines drawn from specific books in the series."),
        ("Where can I watch DCI Banks in the US?", "BritBox is DCI Banks's primary US streaming home, with all five series available to subscribers."),
        ("Where is DCI Banks filmed?", "DCI Banks was filmed on location in Yorkshire, primarily around Leeds and Otley, standing in for the fictional town of Eastvale."),
        ("Who plays DCI Banks?", "Stephen Tompkinson plays DCI Alan Banks throughout the series, with Andrea Lowe as DS/DI Annie Cabbot and Caroline Catz joining later as DI Helen Morton."),
    ]),
})

# ============================================================ 2. THE RESPONDER
SHOWS.append({
    "slug": "the-responder",
    "title": "The Responder",
    "meta_desc": "Where to watch The Responder in the US. The guide to Martin Freeman's BBC drama about a Liverpool night-shift police officer, both series.",
    "eyebrow": "British Crime Drama &middot; BBC One &middot; 2022&ndash;2024 &middot; 2 Series",
    "tags": ["2 Series", "10 Episodes", "Stars Martin Freeman", "Liverpool", "Written by a Former Officer"],
    "description": "Martin Freeman stars as PC Chris Carson, a burnt-out Liverpool police officer working nights, in this tense drama written by former Merseyside Police officer Tony Schumacher. Adelayo Adedayo plays his new, idealistic partner PC Rachel Hargreaves, with MyAnna Buring as Chris's wife Kate. Two series have aired, five episodes each, broadcast on BBC One in 2022 and 2024. The Responder streams on BritBox in the US.",
    "viewer_guide_heading": "New Viewer's <em>Guide</em>",
    "viewer_guide_card": card("badge-new", "Where to Start", "Series 1, Episode 1 (2022)",
        "Chris Carson, already unraveling under the pressure of night-shift policing, is partnered with newcomer Rachel Hargreaves, setting up the mismatched partnership at the heart of the series.",
        ["Series 1", "2022"],
        "At a Glance", [("Watch Order", "Watch in order"), ("Tone", "Tense, morally grey")]),
    "watch_block": watch_block("BritBox", BRITBOX, "Both series &middot; Subscription required", buy_title="The Responder"),
    "episode_cards": (
        card("badge-essential", "1 &middot; Series 1 &middot; 2022", "Episode 1",
             "The series premiere, introducing Chris Carson's night shift and his new partnership with Rachel Hargreaves, establishing the show's pressure-cooker tone from its opening minutes.",
             ["Series Premiere"], "At a Glance", [("Position", "Series 1, 2022"), ("Best For", "First-time viewers")],
             BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "2 &middot; Series 1", "Episode 3",
               "A British TV Hub pick for the way it deepens Chris's home life alongside the case of the night, showing the toll the job takes outside working hours.",
               ["Character-Driven"], "At a Glance", [("Best For", "Viewers invested in Chris's home life")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "3 &middot; Series 1", "Episode 5",
               "The Series 1 finale, pulling together the series' threads with the tension the show built across its first run.",
               ["Series Finale"], "At a Glance", [("Best For", "Closing out Series 1")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "4 &middot; Series 2 &middot; 2024", "Episode 1",
               "The Series 2 premiere, picking up Chris's story two years on and widening the show's view of the people around him.",
               ["Series 2 Premiere"], "At a Glance", [("Best For", "Returning viewers")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "5 &middot; Series 2", "Episode 5",
               "The Series 2 finale, closing out the second run's storylines with the same unflinching tone as the rest of the series.",
               ["Series Finale"], "At a Glance", [("Best For", "Viewers finishing Series 2")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
    ),
    "cast_cards": (
        card("badge-essential", "Lead", "Martin Freeman", "PC Chris Carson &mdash; a Liverpool night-shift officer whose personal and professional lives are both close to collapse.", ["Lead Officer"], "At a Glance", [("Role", "PC Chris Carson"), ("Appears", "Both series")])
        + card("badge-essential", "Lead", "Adelayo Adedayo", "PC Rachel Hargreaves &mdash; Chris's new, more idealistic partner, whose own moral compass is tested across the series.", ["Patrol Officer"], "At a Glance", [("Role", "PC Rachel Hargreaves")])
        + card("badge-classic", "Recurring", "MyAnna Buring", "Kate Carson, Chris's wife, navigating the strain his job puts on their marriage and family.", ["Chris's Wife"], "At a Glance", [("Role", "Kate Carson")])
        + card("badge-classic", "Recurring", "Warren Brown", "Raymond Mullen, a local figure entangled in the Liverpool underworld Chris moves through on his shifts.", ["Recurring Role"], "At a Glance", [("Role", "Raymond Mullen")])
    ),
    "special_cards": (
        card("badge-classic", "Authenticity", "Written by a Former Police Officer", "Creator Tony Schumacher spent years as a Merseyside Police officer before writing the series, lending its depiction of night-shift policing an unusually grounded, unglamorous feel.", ["Lived Experience"], "At a Glance", [("Writer", "Tony Schumacher")])
        + card("badge-classic", "Lead Performance", "Martin Freeman Against Type", "Freeman's performance as a frayed, morally compromised officer marked a deliberate departure from his more comic or straightforwardly sympathetic earlier roles.", ["Against Type"], "At a Glance", [("Lead", "Martin Freeman")])
        + card("badge-classic", "Setting as Character", "Liverpool at Night", "The series is shot through with a specific, unromanticized Liverpool atmosphere, using the city's night shift as both backdrop and pressure chamber for its characters.", ["Liverpool"], "At a Glance", [("City", "Liverpool")])
    ),
    "setting_card": card("badge-classic", "Setting &amp; Filming", "Liverpool, England", "The Responder follows a fictional police constabulary covering Liverpool, with its night-shift structure built around the city's streets and neighbourhoods after dark.", ["Liverpool, England"], "At a Glance", [("City", "Liverpool")]),
    "books_section": "",
    "faq_cards": (
        faq_card("Status", "Will there be a Series 3 of The Responder?", "As of November 2026, the BBC has not announced a third series, though it has also not been officially cancelled. Series 2 ended without a confirmed renewal.", [("Status", "Unconfirmed"), ("Series 2 Aired", "2024")])
        + faq_card("Episode Count", "How many episodes of The Responder are there?", "There are 10 episodes across two series, five episodes each, broadcast in 2022 and 2024.", [("Episodes", "10"), ("Series", "2")])
        + faq_card("Cast", "Who stars in The Responder?", "Martin Freeman stars as PC Chris Carson, with Adelayo Adedayo as his partner PC Rachel Hargreaves and MyAnna Buring as his wife, Kate Carson.", [("Lead", "Martin Freeman")])
        + faq_card("Streaming", "Where can I watch The Responder in the US?", "BritBox is The Responder's US streaming home, with both series available to subscribers.", [("Primary", "BritBox")])
        + faq_card("Filming Location", "Where is The Responder filmed?", "The Responder is set and filmed around Liverpool, following a fictional police constabulary covering the city.", [("City", "Liverpool")])
    ),
    "tvseries_jsonld": tvseries_jsonld("The Responder", None, "Martin Freeman stars as PC Chris Carson, a burnt-out Liverpool police officer working nights, in this BBC drama written by former Merseyside Police officer Tony Schumacher. Two series have aired, five episodes each, broadcast in 2022 and 2024.", "British Crime Drama", 2, "2022", None, ["Martin Freeman", "Adelayo Adedayo"], "https://britishtvhub.com/shows/the-responder.html"),
    "faq_jsonld": faq_jsonld("The Responder", [
        ("Will there be a Series 3 of The Responder?", "As of November 2026, the BBC has not announced a third series, though it has also not been officially cancelled. Series 2 ended without a confirmed renewal."),
        ("How many episodes of The Responder are there?", "There are 10 episodes across two series, five episodes each, broadcast in 2022 and 2024."),
        ("Who stars in The Responder?", "Martin Freeman stars as PC Chris Carson, with Adelayo Adedayo as his partner PC Rachel Hargreaves and MyAnna Buring as his wife, Kate Carson."),
        ("Where can I watch The Responder in the US?", "BritBox is The Responder's US streaming home, with both series available to subscribers."),
        ("Where is The Responder filmed?", "The Responder is set and filmed around Liverpool, following a fictional police constabulary covering the city."),
    ]),
})

# ============================================================ 3. McDONALD & DODDS
SHOWS.append({
    "slug": "mcdonald-and-dodds",
    "title": "McDonald &amp; Dodds",
    "meta_desc": "Where to watch McDonald & Dodds in the US. The complete guide to ITV's Bath-set odd-couple detective drama, all four series, now concluded.",
    "eyebrow": "British Crime Drama &middot; ITV &middot; 2020&ndash;2024 &middot; Complete Series",
    "tags": ["4 Series", "11 Episodes", "Stars Tala Gouveia &amp; Jason Watkins", "Bath", "Odd-Couple Detectives"],
    "description": "Tala Gouveia stars as DCI Lauren McDonald, newly transferred to Bath, paired with Jason Watkins's unassuming DS Dodds in this odd-couple detective drama. Over four series and eleven feature-length episodes, the mismatched pair investigate murders set against Bath's Georgian architecture, with the show's gentle humour and McDonald's culture shock providing a lighter counterpoint to the central mysteries. ITV cancelled the series in January 2025 after four series. McDonald &amp; Dodds streams on BritBox in the US.",
    "viewer_guide_heading": "New Viewer's <em>Guide</em>",
    "viewer_guide_card": card("badge-new", "Where to Start", "Series 1, Episode 1 (2020)",
        "DCI Lauren McDonald arrives in Bath from London and is paired with the self-effacing DS Dodds, setting up the fish-out-of-water dynamic that runs through the series.",
        ["Series 1", "2020"],
        "At a Glance", [("Watch Order", "Case-of-the-week, watch in order for cast changes"), ("Cast Change", "New Chief Superintendent from Series 3")]),
    "watch_block": watch_block("BritBox", BRITBOX, "All 4 series &middot; Subscription required", buy_title="McDonald and Dodds"),
    "episode_cards": (
        card("badge-essential", "1 &middot; Series 1 &middot; 2020", "Series 1, Episode 1",
             "The series premiere, introducing McDonald's move to Bath and her pairing with the quietly perceptive Dodds.",
             ["Series Premiere"], "At a Glance", [("Position", "Series 1, 2020"), ("Best For", "First-time viewers")],
             BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "2 &middot; Series 2", "A British TV Hub Pick",
               "A British TV Hub selection from the show's extended second series, which gave the McDonald-Dodds partnership more room to develop.",
               ["Series 2"], "At a Glance", [("Best For", "Established fans")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "3 &middot; Series 3", "A British TV Hub Pick",
               "A British TV Hub selection introducing Claire Skinner's Chief Superintendent Mary Ormond, who adds a new dynamic to the Bath police station.",
               ["New Chief Superintendent"], "At a Glance", [("Best For", "Fans of the supporting cast")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "4 &middot; Series 4 &middot; 2024", "Series Finale",
               "The final episode of the show's run, broadcast 4 August 2024, closing out McDonald and Dodds's Bath investigations.",
               ["Series Finale"], "At a Glance", [("Best For", "Viewers finishing the series")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
    ),
    "cast_cards": (
        card("badge-essential", "Lead", "Tala Gouveia", "DCI Lauren McDonald &mdash; a sharp, ambitious detective adjusting to life and work outside London.", ["Lead Detective"], "At a Glance", [("Role", "DCI Lauren McDonald"), ("Appears", "All 4 series")])
        + card("badge-essential", "Lead", "Jason Watkins", "DS Dodds &mdash; an unassuming, methodical detective sergeant whose quiet observations often crack the case.", ["Detective Sergeant"], "At a Glance", [("Role", "DS Dodds"), ("Appears", "All 4 series")])
        + card("badge-classic", "Series 1&ndash;2", "James Murray", "Chief Superintendent John Houseman, McDonald and Dodds's commanding officer in the show's earlier series.", ["Chief Superintendent"], "At a Glance", [("Role", "Supt. John Houseman"), ("Appears", "Series 1&ndash;2")])
        + card("badge-new", "Joins Series 3", "Claire Skinner", "Chief Superintendent Mary Ormond, taking over as the Bath station's commanding officer from Series 3 onward.", ["Chief Superintendent"], "At a Glance", [("Role", "Supt. Mary Ormond"), ("Appears", "Series 3&ndash;4")])
    ),
    "special_cards": (
        card("badge-classic", "Partnership", "An Unlikely, Warm Pairing", "Gouveia's confident, impatient McDonald and Watkins's self-deprecating, meticulous Dodds give the series a gentler double act than many British procedurals.", ["Mismatched Pair"], "At a Glance", [("McDonald", "Confident, impatient"), ("Dodds", "Self-deprecating, meticulous")])
        + card("badge-classic", "Setting as Character", "Bath's Georgian Backdrop", "The series makes consistent use of Bath's distinctive Georgian architecture, giving it a visual identity distinct from London-set procedurals.", ["Bath"], "At a Glance", [("Setting", "Bath, Somerset")])
        + card("badge-classic", "Tone", "Gentle Humour Alongside Murder", "The show leans on McDonald's culture shock and the station's office dynamics for lighter moments, without undercutting the seriousness of its cases.", ["Light Procedural"], "At a Glance", [("Tone", "Warm, understated")])
    ),
    "setting_card": card("badge-classic", "Setting &amp; Filming", "Bath, Somerset, England", "McDonald &amp; Dodds is both set and filmed in Bath, Somerset, using the city's Georgian streets and buildings as a consistent backdrop across all four series.", ["Bath, Somerset"], "At a Glance", [("City", "Bath")]),
    "books_section": "",
    "faq_cards": (
        faq_card("Status", "Is McDonald & Dodds finished?", "Yes. ITV cancelled the series on 16 January 2025 after four series, citing a decline in ratings. The show's run ended with 11 episodes.", [("Status", "Cancelled"), ("Cancelled", "January 2025")])
        + faq_card("Episode Count", "How many episodes of McDonald & Dodds are there?", "There are 11 feature-length episodes across four series: two in Series 1, two in Series 2, four in Series 3, and three in Series 4.", [("Episodes", "11"), ("Series", "4")])
        + faq_card("Cast", "Who stars in McDonald & Dodds?", "Tala Gouveia plays DCI Lauren McDonald and Jason Watkins plays DS Dodds across all four series.", [("Leads", "Tala Gouveia, Jason Watkins")])
        + faq_card("Streaming", "Where can I watch McDonald & Dodds in the US?", "BritBox is McDonald & Dodds's US streaming home, with all four series available to subscribers.", [("Primary", "BritBox")])
        + faq_card("Filming Location", "Where is McDonald & Dodds filmed?", "The series is filmed in Bath, Somerset, where it is also set.", [("City", "Bath")])
        + faq_card("Renewal", "Will there be a Series 5 of McDonald & Dodds?", "No. ITV confirmed the cancellation in January 2025, and no further series has been announced.", [("Status", "Cancelled, no Series 5")])
    ),
    "tvseries_jsonld": tvseries_jsonld("McDonald & Dodds", None, "Tala Gouveia stars as DCI Lauren McDonald, paired with Jason Watkins's DS Dodds, in this Bath-set detective drama. Four series and eleven episodes aired between 2020 and 2024, before ITV cancelled the series in January 2025.", "British Crime Drama", 4, "2020", "2024", ["Tala Gouveia", "Jason Watkins"], "https://britishtvhub.com/shows/mcdonald-and-dodds.html"),
    "faq_jsonld": faq_jsonld("McDonald & Dodds", [
        ("Is McDonald & Dodds finished?", "Yes. ITV cancelled the series on 16 January 2025 after four series, citing a decline in ratings. The show's run ended with 11 episodes."),
        ("How many episodes of McDonald & Dodds are there?", "There are 11 feature-length episodes across four series: two in Series 1, two in Series 2, four in Series 3, and three in Series 4."),
        ("Who stars in McDonald & Dodds?", "Tala Gouveia plays DCI Lauren McDonald and Jason Watkins plays DS Dodds across all four series."),
        ("Where can I watch McDonald & Dodds in the US?", "BritBox is McDonald & Dodds's US streaming home, with all four series available to subscribers."),
        ("Where is McDonald & Dodds filmed?", "The series is filmed in Bath, Somerset, where it is also set."),
        ("Will there be a Series 5 of McDonald & Dodds?", "No. ITV confirmed the cancellation in January 2025, and no further series has been announced."),
    ]),
})

# ============================================================ 4. A WOMAN OF SUBSTANCE
SHOWS.append({
    "slug": "a-woman-of-substance",
    "title": "A Woman of Substance",
    "meta_desc": "Where to watch A Woman of Substance in the US. The guide to Channel 4's 2026 adaptation of Barbara Taylor Bradford's novel, starring Brenda Blethyn.",
    "eyebrow": "British Period Drama &middot; Channel 4 &middot; 2026&ndash;present &middot; Renewed for Series 2",
    "tags": ["8 Episodes", "Stars Brenda Blethyn", "Yorkshire", "Based on the Novel", "New for 2026"],
    "description": "Brenda Blethyn and Jessica Reynolds share the role of Emma Harte, a Yorkshire servant girl who rises to become a department-store magnate, in this new eight-part adaptation of Barbara Taylor Bradford's 1979 bestseller. This is the second screen adaptation of the novel, following the 1985 miniseries starring Deborah Kerr and Jenny Seagrove. The story spans from early-1900s Yorkshire to 1970s business life in New York, with Channel 4 renewing the series for a second season. A Woman of Substance streams on BritBox in the US.",
    "viewer_guide_heading": "New Viewer's <em>Guide</em>",
    "viewer_guide_card": card("badge-new", "Where to Start", "Episode 1 (2026)",
        "The series opens in early-1900s Yorkshire with the young Emma Harte, played by Jessica Reynolds, working as a servant in the Fairley household, setting in motion the rise that Brenda Blethyn's older Emma narrates from decades later.",
        ["Episode 1", "2026"],
        "At a Glance", [("Watch Order", "Watch in order; dual timelines"), ("Not", "A remake of the 1985 miniseries")]),
    "watch_block": watch_block("BritBox", BRITBOX, "Series 1, 8 episodes &middot; Subscription required", buy_title="A Woman of Substance"),
    "episode_cards": (
        card("badge-essential", "1 &middot; Episode 1 &middot; 2026", "Series Premiere",
             "The opening episode, establishing young Emma Harte's life in service to the Fairley family and the dual-timeline structure that carries through the series.",
             ["Series Premiere"], "At a Glance", [("Position", "Episode 1, 2026"), ("Best For", "First-time viewers")],
             BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "2 &middot; Mid-Series", "A British TV Hub Pick",
               "A British TV Hub selection from the middle of the run, as Emma's ambitions begin to take concrete shape beyond the Fairley household.",
               ["Rising Fortunes"], "At a Glance", [("Best For", "Fans of rags-to-riches sagas")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "3 &middot; Episode 8", "Series Finale",
               "The final episode of Series 1, closing out the opening chapter of Emma Harte's story ahead of the confirmed second series.",
               ["Series Finale"], "At a Glance", [("Best For", "Viewers finishing Series 1")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
    ),
    "cast_cards": (
        card("badge-essential", "Lead", "Brenda Blethyn", "The older Emma Harte, narrating and living out the later chapters of her rise from servant to business magnate.", ["Lead, Later Timeline"], "At a Glance", [("Role", "Older Emma Harte")])
        + card("badge-essential", "Lead", "Jessica Reynolds", "The younger Emma Harte, shown in flashback as a Yorkshire servant girl beginning her ascent.", ["Lead, Earlier Timeline"], "At a Glance", [("Role", "Younger Emma Harte")])
        + card("badge-classic", "Supporting", "Emmett J. Scanlan", "Adam Fairley, a member of the Yorkshire family Emma serves and whose fortunes become entangled with her own.", ["Supporting"], "At a Glance", [("Role", "Adam Fairley")])
        + card("badge-classic", "Supporting", "Will Mellor", "Jack Harte, a figure from Emma's own family circle.", ["Supporting"], "At a Glance", [("Role", "Jack Harte")])
    ),
    "special_cards": (
        card("badge-classic", "Dual Casting", "Two Actors, One Emma Harte", "Casting Brenda Blethyn and Jessica Reynolds as the same character at different life stages lets the series move fluidly between Emma's beginnings and the business magnate she becomes.", ["Dual Timeline"], "At a Glance", [("Older Emma", "Brenda Blethyn"), ("Younger Emma", "Jessica Reynolds")])
        + card("badge-classic", "Scope", "A Rags-to-Riches Saga Across Decades", "The story spans from early-1900s Yorkshire service to 1970s international business, giving the series an unusually wide historical and geographic canvas for a British period drama.", ["Multi-Decade Saga"], "At a Glance", [("Span", "1900s&ndash;1970s")])
        + card("badge-classic", "Second Adaptation", "A New Take on a Familiar Story", "This is the second screen version of Barbara Taylor Bradford's novel, following the 1985 miniseries, giving a new generation of viewers a fresh adaptation of Emma Harte's story.", ["Second Adaptation"], "At a Glance", [("Earlier Version", "1985 miniseries")])
    ),
    "setting_card": card("badge-classic", "Setting &amp; Filming", "Yorkshire, With Scenes in New York", "The story is set primarily in Yorkshire, with later chapters moving into international business life, including scenes set in New York. Filming took place mainly in Yorkshire, with Broughton Hall heavily featured, alongside Liverpool's waterfront standing in for New York, Beamish open-air museum in County Durham, and Brodsworth Hall in Doncaster.", ["Yorkshire, England"], "At a Glance", [("Primary Region", "Yorkshire"), ("Key Location", "Broughton Hall")]),
    "books_section": "  " + f'''<div class="section-header">
    <h2>Books Behind the <em>Series</em></h2>
  </div>

''' + card("badge-classic", "Source Novel", "Barbara Taylor Bradford's 1979 Bestseller", "A Woman of Substance adapts Barbara Taylor Bradford's bestselling 1979 novel of the same name, the first in her Emma Harte saga. This is the second screen adaptation, following a 1985 miniseries starring Deborah Kerr and Jenny Seagrove.", ["Novel Adaptation"], "At a Glance", [("Author", "Barbara Taylor Bradford"), ("Published", "1979")]) + "\n  <hr class=\"divider\">\n\n",
    "faq_cards": (
        faq_card("Status", "Is A Woman of Substance the same as the 1985 version?", "No. This is a new 2026 adaptation of Barbara Taylor Bradford's novel, distinct from the 1985 miniseries that starred Deborah Kerr and Jenny Seagrove, with its own cast and creative team.", [("New Version", "2026"), ("Earlier Version", "1985")])
        + faq_card("Renewal", "Will there be a Series 2 of A Woman of Substance?", "Yes. Channel 4 confirmed a second series in June 2026, with Brenda Blethyn and Jessica Reynolds both set to return.", [("Status", "Renewed"), ("Confirmed", "June 2026")])
        + faq_card("Episode Count", "How many episodes are in A Woman of Substance Series 1?", "Series 1 has eight episodes, each running approximately 47 minutes.", [("Episodes", "8")])
        + faq_card("Cast", "Who plays Emma Harte in A Woman of Substance?", "Brenda Blethyn plays the older Emma Harte, with Jessica Reynolds playing the character as a young woman in earlier timeline scenes.", [("Older Emma", "Brenda Blethyn"), ("Younger Emma", "Jessica Reynolds")])
        + faq_card("Streaming", "Where can I watch A Woman of Substance in the US?", "BritBox secured the US streaming rights, confirmed in February 2026, making it the primary way to watch the series in the US.", [("Primary", "BritBox")])
        + faq_card("Source Material", "Is A Woman of Substance based on a book?", "Yes. It adapts Barbara Taylor Bradford's 1979 novel of the same name, the first book in her Emma Harte saga.", [("Author", "Barbara Taylor Bradford")])
    ),
    "tvseries_jsonld": tvseries_jsonld("A Woman of Substance", None, "Brenda Blethyn and Jessica Reynolds share the role of Emma Harte, a Yorkshire servant girl who rises to become a department-store magnate, in this 2026 eight-part adaptation of Barbara Taylor Bradford's novel.", "British Period Drama", 1, "2026", None, ["Brenda Blethyn", "Jessica Reynolds"], "https://britishtvhub.com/shows/a-woman-of-substance.html"),
    "faq_jsonld": faq_jsonld("A Woman of Substance", [
        ("Is A Woman of Substance the same as the 1985 version?", "No. This is a new 2026 adaptation of Barbara Taylor Bradford's novel, distinct from the 1985 miniseries that starred Deborah Kerr and Jenny Seagrove, with its own cast and creative team."),
        ("Will there be a Series 2 of A Woman of Substance?", "Yes. Channel 4 confirmed a second series in June 2026, with Brenda Blethyn and Jessica Reynolds both set to return."),
        ("How many episodes are in A Woman of Substance Series 1?", "Series 1 has eight episodes, each running approximately 47 minutes."),
        ("Who plays Emma Harte in A Woman of Substance?", "Brenda Blethyn plays the older Emma Harte, with Jessica Reynolds playing the character as a young woman in earlier timeline scenes."),
        ("Where can I watch A Woman of Substance in the US?", "BritBox secured the US streaming rights, confirmed in February 2026, making it the primary way to watch the series in the US."),
        ("Is A Woman of Substance based on a book?", "Yes. It adapts Barbara Taylor Bradford's 1979 novel of the same name, the first book in her Emma Harte saga."),
    ]),
})

# ============================================================ 5. THE TOWER
SHOWS.append({
    "slug": "the-tower",
    "title": "The Tower",
    "meta_desc": "Where to watch The Tower in the US. The complete guide to Gemma Whelan's ITV crime drama based on Kate London's Metropolitan novels, all three series.",
    "eyebrow": "British Crime Drama &middot; ITV &middot; 2021&ndash;2024 &middot; Complete Series",
    "tags": ["3 Series", "11 Episodes", "Stars Gemma Whelan", "London", "Based on the Novels"],
    "description": "Gemma Whelan stars as DS Sarah Collins, investigating a death linked to a London tower block, in this crime drama based on Kate London's Metropolitan series of novels. Tahirah Sharif plays probationary officer Lizzie Adama, whose fall from the same tower opens the story. Three series aired between 2021 and 2024, 11 episodes in total, before ITV cancelled the show amid a decline in viewing figures. The Tower streams on BritBox in the US.",
    "viewer_guide_heading": "New Viewer's <em>Guide</em>",
    "viewer_guide_card": card("badge-new", "Where to Start", "Series 1, Episode 1 (2021)",
        "A teenage girl and a police officer fall to their deaths from a London tower block, and DS Sarah Collins is brought in to investigate what really happened, in a premiere based on Kate London's novel Post Mortem.",
        ["Series 1", "2021"],
        "At a Glance", [("Watch Order", "Watch in order"), ("Based On", "Post Mortem, by Kate London")]),
    "watch_block": watch_block("BritBox", BRITBOX, "All 3 series &middot; Subscription required", buy_title="The Tower TV series"),
    "episode_cards": (
        card("badge-essential", "1 &middot; Series 1 &middot; 2021", "Episode 1",
             "The series premiere, built around the dual fall of a teenage girl and a police officer from a London tower block, based on Kate London's novel Post Mortem.",
             ["Series Premiere"], "At a Glance", [("Position", "Series 1, 2021"), ("Best For", "First-time viewers")],
             BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "2 &middot; Series 2 &middot; 2023", "A British TV Hub Pick",
               "A British TV Hub selection from Series 2, Death Message, which premiered exclusively on BritBox before any UK ITV broadcast.",
               ["BritBox Exclusive"], "At a Glance", [("Best For", "Fans of the first series")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "3 &middot; Series 3 &middot; 2024", "A British TV Hub Pick",
               "A British TV Hub selection from the show's final series, Gallowstree Lane, based on Kate London's novel of the same name.",
               ["Final Series"], "At a Glance", [("Based On", "Gallowstree Lane")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
    ),
    "cast_cards": (
        card("badge-essential", "Lead", "Gemma Whelan", "DS Sarah Collins &mdash; the detective sergeant leading the investigation across all three series.", ["Lead Detective"], "At a Glance", [("Role", "DS Sarah Collins"), ("Appears", "All 3 series")])
        + card("badge-essential", "Lead", "Tahirah Sharif", "Lizzie Adama, a probationary police officer whose fall from the tower sets the first series in motion.", ["Probationary Officer"], "At a Glance", [("Role", "Lizzie Adama")])
        + card("badge-classic", "Recurring", "Jimmy Akingbola", "DC Steve Bradshaw, part of the investigative team working alongside Collins.", ["Detective Constable"], "At a Glance", [("Role", "DC Steve Bradshaw")])
        + card("badge-classic", "Recurring", "Emmett J. Scanlan", "Inspector Kieran Shaw, a senior officer connected to the events under investigation.", ["Inspector"], "At a Glance", [("Role", "Insp. Kieran Shaw")])
    ),
    "special_cards": (
        card("badge-classic", "Source Material", "Grounded in Kate London's Novels", "The series draws its plots directly from Kate London's Metropolitan series of crime novels, with specific books, including Post Mortem and Gallowstree Lane, forming the basis of individual series.", ["Novel Adaptation"], "At a Glance", [("Author", "Kate London")])
        + card("badge-classic", "Structure", "A Slow-Burn Institutional Mystery", "Rather than a straightforward case-of-the-week format, each series takes its time unpacking what really happened on the night of the opening tragedy, with the Metropolitan Police's own institutional failings often as much a subject as the crime itself.", ["Slow-Burn Mystery"], "At a Glance", [("Pace", "Deliberate")])
        + card("badge-classic", "US Distribution", "A BritBox North American Exclusive", "BritBox holds North American rights to the series, and Series 2 premiered exclusively on the platform before any UK ITV broadcast.", ["BritBox Exclusive"], "At a Glance", [("US Home", "BritBox")])
    ),
    "setting_card": card("badge-classic", "Setting &amp; Filming", "Southeast London (Filmed in the Northwest)", "The Tower is set in southeast London, but it was filmed mostly in northwest England, including Liverpool, Manchester, Runcorn, Warrington, and Tatton Park in Knutsford, with some post-production pick-up shots of the City of London skyline filmed in London itself.", ["London (Setting)"], "At a Glance", [("Set In", "Southeast London"), ("Filmed In", "Northwest England")]),
    "books_section": "  " + f'''<div class="section-header">
    <h2>Books Behind the <em>Series</em></h2>
  </div>

''' + card("badge-classic", "Source Novels", "Kate London's Metropolitan Series", "The Tower is based on Kate London's Metropolitan series of crime novels. Series 1 draws on the novel Post Mortem, and Series 3 adapts Gallowstree Lane.", ["Novel Series"], "At a Glance", [("Author", "Kate London"), ("Key Titles", "Post Mortem, Gallowstree Lane")]) + "\n  <hr class=\"divider\">\n\n",
    "faq_cards": (
        faq_card("Status", "Is The Tower finished?", "Yes. ITV cancelled the series after three series due to a decline in viewing figures, with the final series, Gallowstree Lane, airing in September 2024.", [("Status", "Cancelled"), ("Final Series", "2024")])
        + faq_card("Episode Count", "How many episodes of The Tower are there?", "There are 11 episodes across three series: three in Series 1, four in Series 2, and four in Series 3.", [("Episodes", "11"), ("Series", "3")])
        + faq_card("Source Material", "Is The Tower based on a book?", "Yes. It adapts Kate London's Metropolitan series of crime novels, including Post Mortem and Gallowstree Lane.", [("Author", "Kate London")])
        + faq_card("Streaming", "Where can I watch The Tower in the US?", "BritBox holds North American rights and is The Tower's primary US streaming home for all three series.", [("Primary", "BritBox")])
        + faq_card("Filming Location", "Where is The Tower filmed?", "Although set in southeast London, The Tower was filmed mostly in northwest England, including Liverpool, Manchester, and Tatton Park.", [("Set In", "Southeast London"), ("Filmed In", "Northwest England")])
        + faq_card("Cast", "Who stars in The Tower?", "Gemma Whelan stars as DS Sarah Collins, with Tahirah Sharif as Lizzie Adama, the officer whose fall opens the first series.", [("Lead", "Gemma Whelan")])
    ),
    "tvseries_jsonld": tvseries_jsonld("The Tower", None, "Gemma Whelan stars as DS Sarah Collins, investigating a death linked to a London tower block, in this crime drama based on Kate London's Metropolitan novels. Three series aired between 2021 and 2024, 11 episodes in total.", "British Crime Drama", 3, "2021", "2024", ["Gemma Whelan", "Tahirah Sharif"], "https://britishtvhub.com/shows/the-tower.html"),
    "faq_jsonld": faq_jsonld("The Tower", [
        ("Is The Tower finished?", "Yes. ITV cancelled the series after three series due to a decline in viewing figures, with the final series, Gallowstree Lane, airing in September 2024."),
        ("How many episodes of The Tower are there?", "There are 11 episodes across three series: three in Series 1, four in Series 2, and four in Series 3."),
        ("Is The Tower based on a book?", "Yes. It adapts Kate London's Metropolitan series of crime novels, including Post Mortem and Gallowstree Lane."),
        ("Where can I watch The Tower in the US?", "BritBox holds North American rights and is The Tower's primary US streaming home for all three series."),
        ("Where is The Tower filmed?", "Although set in southeast London, The Tower was filmed mostly in northwest England, including Liverpool, Manchester, and Tatton Park."),
        ("Who stars in The Tower?", "Gemma Whelan stars as DS Sarah Collins, with Tahirah Sharif as Lizzie Adama, the officer whose fall opens the first series."),
    ]),
})

# ============================================================ 6. LONDON KILLS
SHOWS.append({
    "slug": "london-kills",
    "title": "London Kills",
    "meta_desc": "Where to watch London Kills in the US. The guide to Acorn TV's Metropolitan Police drama starring Hugo Speer and Sharon Small.",
    "eyebrow": "British Crime Drama &middot; Acorn TV &middot; 2019&ndash;present &middot; 4 Series",
    "tags": ["4 Series", "20 Episodes", "Stars Hugo Speer &amp; Sharon Small", "London", "Acorn TV Original"],
    "description": "Hugo Speer leads an elite Metropolitan Police Murder Investigation Team as DI David Bradford in London Kills, an Acorn TV original procedural following a different London murder each series. Sharon Small plays DS Vivienne Cole, with Bailey Patrick and Tori Allen-Martin rounding out the core team across the show's run. Four series have aired, 20 episodes in total, between 2019 and 2023, and the show was renewed for a fifth series in 2024. London Kills streams on Acorn TV in the US.",
    "viewer_guide_heading": "New Viewer's <em>Guide</em>",
    "viewer_guide_card": card("badge-new", "Where to Start", "Series 1, Episode 1 (2019)",
        "The Murder Investigation Team, led by DI David Bradford, takes on its first case, introducing the team dynamics that carry through the series' run.",
        ["Series 1", "2019"],
        "At a Glance", [("Watch Order", "Watch in order; cast shifts each series"), ("Renewed", "For Series 5")]),
    "watch_block": watch_block("Acorn TV", ACORN, "Series 1&ndash;4, 20 episodes &middot; Subscription required", buy_title="London Kills TV series"),
    "episode_cards": (
        card("badge-essential", "1 &middot; Series 1 &middot; 2019", "Episode 1",
             "The series premiere, introducing DI David Bradford's Murder Investigation Team as they take on the first of the show's London-set cases.",
             ["Series Premiere"], "At a Glance", [("Position", "Series 1, 2019"), ("Best For", "First-time viewers")],
             ACORN, "Watch via Acorn TV on Prime Video &rarr;")
        + card("badge-classic", "2 &middot; Series 2", "A British TV Hub Pick",
               "A British TV Hub selection from Series 2, introducing Maimie McCoy's Grace Harper to the team.",
               ["New Team Member"], "At a Glance", [("Best For", "Established fans")],
               ACORN, "Watch via Acorn TV on Prime Video &rarr;")
        + card("badge-classic", "3 &middot; Series 3 &middot; 2022", "A British TV Hub Pick",
               "A British TV Hub selection from Series 3, which introduced John Michie's DCS Jack Mulgrew to the station.",
               ["New Commanding Officer"], "At a Glance", [("Best For", "Fans of shifting team dynamics")],
               ACORN, "Watch via Acorn TV on Prime Video &rarr;")
        + card("badge-classic", "4 &middot; Series 4 &middot; 2023", "A British TV Hub Pick",
               "A British TV Hub selection from the most recently aired series, continuing the team's rotating caseload of London murders.",
               ["Most Recently Aired"], "At a Glance", [("Best For", "Viewers caught up through Series 4")],
               ACORN, "Watch via Acorn TV on Prime Video &rarr;")
    ),
    "cast_cards": (
        card("badge-essential", "Lead", "Hugo Speer", "DI David Bradford &mdash; the team's lead investigator across all four series.", ["Lead Detective Inspector"], "At a Glance", [("Role", "DI David Bradford"), ("Appears", "All 4 series")])
        + card("badge-essential", "Lead", "Sharon Small", "DS Vivienne Cole &mdash; Bradford's longtime detective sergeant and investigative partner.", ["Detective Sergeant"], "At a Glance", [("Role", "DS Vivienne Cole")])
        + card("badge-classic", "Recurring", "Bailey Patrick", "DC Rob Brady, a core member of the Murder Investigation Team.", ["Detective Constable"], "At a Glance", [("Role", "DC Rob Brady")])
        + card("badge-classic", "Recurring", "Tori Allen-Martin", "DC Billie Fitzgerald, rounding out the team's regular roster.", ["Detective Constable"], "At a Glance", [("Role", "DC Billie Fitzgerald")])
    ),
    "special_cards": (
        card("badge-classic", "Format", "A New Murder Each Series", "Rather than splitting each series into separate case-of-the-week episodes, London Kills generally follows one central murder investigation across its five-episode run, giving the mystery room to breathe.", ["Serialized Mystery"], "At a Glance", [("Format", "One case per series")])
        + card("badge-classic", "Team Dynamics", "A Rotating Supporting Cast", "While Bradford and Cole anchor every series, the wider team has shifted gradually, with new detectives and commanding officers joining as the show has progressed.", ["Evolving Cast"], "At a Glance", [("Constant", "Bradford, Cole")])
        + card("badge-classic", "Acorn TV Original", "Built for Acorn TV's US Audience", "London Kills premiered on Acorn TV in the US before its UK broadcast, reflecting the platform's role in developing original British mystery programming.", ["Acorn TV Original"], "At a Glance", [("US Premiere", "February 2019")])
    ),
    "setting_card": card("badge-classic", "Setting &amp; Filming", "London, England", "London Kills is set in London, following an elite Metropolitan Police Murder Investigation Team as it investigates a fresh case each series across the city.", ["London, England"], "At a Glance", [("City", "London")]),
    "books_section": "",
    "faq_cards": (
        faq_card("Status", "Is London Kills coming back for a fifth series?", "Yes. Acorn TV renewed London Kills for a fifth series in 2024. As of November 2026, no confirmed air date for Series 5 has been announced.", [("Status", "Renewed"), ("Renewed", "2024")])
        + faq_card("Episode Count", "How many episodes of London Kills are there?", "There are 20 episodes across four aired series, five episodes per series, from 2019 to 2023.", [("Episodes", "20"), ("Series", "4 aired")])
        + faq_card("Cast", "Who stars in London Kills?", "Hugo Speer stars as DI David Bradford, with Sharon Small as DS Vivienne Cole, leading the Murder Investigation Team across the series.", [("Leads", "Hugo Speer, Sharon Small")])
        + faq_card("Streaming", "Where can I watch London Kills in the US?", "Acorn TV is London Kills's US streaming home, where the series has premiered since Series 1.", [("Primary", "Acorn TV")])
        + faq_card("Filming Location", "Where is London Kills filmed?", "The series is set and filmed in London, following the Metropolitan Police's murder investigations across the city.", [("City", "London")])
    ),
    "tvseries_jsonld": tvseries_jsonld("London Kills", None, "Hugo Speer leads an elite Metropolitan Police Murder Investigation Team in this Acorn TV original procedural. Four series have aired, 20 episodes in total, between 2019 and 2023, with a fifth series renewed.", "British Crime Drama", 4, "2019", None, ["Hugo Speer", "Sharon Small"], "https://britishtvhub.com/shows/london-kills.html"),
    "faq_jsonld": faq_jsonld("London Kills", [
        ("Is London Kills coming back for a fifth series?", "Yes. Acorn TV renewed London Kills for a fifth series in 2024. As of November 2026, no confirmed air date for Series 5 has been announced."),
        ("How many episodes of London Kills are there?", "There are 20 episodes across four aired series, five episodes per series, from 2019 to 2023."),
        ("Who stars in London Kills?", "Hugo Speer stars as DI David Bradford, with Sharon Small as DS Vivienne Cole, leading the Murder Investigation Team across the series."),
        ("Where can I watch London Kills in the US?", "Acorn TV is London Kills's US streaming home, where the series has premiered since Series 1."),
        ("Where is London Kills filmed?", "The series is set and filmed in London, following the Metropolitan Police's murder investigations across the city."),
    ]),
})

# ============================================================ 7. SUSPECTS
SHOWS.append({
    "slug": "suspects",
    "title": "Suspects",
    "meta_desc": "Where to watch Suspects in the US. The complete guide to Channel 5's largely improvised police procedural, all five series, now concluded.",
    "eyebrow": "British Crime Drama &middot; Channel 5 &middot; 2014&ndash;2016 &middot; Complete Series",
    "tags": ["5 Series", "23 Episodes", "Largely Improvised", "London", "Complete Series"],
    "description": "Suspects follows a Metropolitan Police team investigating crimes across London, with most of the dialogue improvised from character notes and plot outlines rather than a fully scripted script, giving the show an unusually naturalistic, fly-on-the-wall feel. The cast, including Damien Molony, Clare-Hope Ashitey, and Fay Ripley, ran through five series and 23 episodes between 2014 and 2016, with Series 5 confirmed as the show's final run. Suspects streams on BritBox, Acorn TV, and PBS in the US.",
    "viewer_guide_heading": "New Viewer's <em>Guide</em>",
    "viewer_guide_card": card("badge-new", "Where to Start", "Series 1, Episode 1 (2014)",
        "The first case introduces the Metropolitan Police team and the show's distinctive improvised, documentary-style approach to procedural storytelling.",
        ["Series 1", "2014"],
        "At a Glance", [("Watch Order", "Watch in order"), ("Format", "Largely improvised dialogue")]),
    "watch_block": watch_block("BritBox", BRITBOX, "All 5 series &middot; Subscription required",
        also="Also available via Acorn TV and PBS, including PBS Masterpiece Amazon Channel and participating PBS stations.",
        buy_title="Suspects TV series"),
    "episode_cards": (
        card("badge-essential", "1 &middot; Series 1 &middot; 2014", "Episode 1",
             "The series premiere, establishing the Metropolitan Police team and the largely improvised style that sets Suspects apart from traditionally scripted procedurals.",
             ["Series Premiere"], "At a Glance", [("Position", "Series 1, 2014"), ("Best For", "First-time viewers")],
             BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "2 &middot; Series 2", "A British TV Hub Pick",
               "A British TV Hub selection from the show's second series, continuing its fly-on-the-wall approach to London casework.",
               ["Series 2"], "At a Glance", [("Best For", "Established fans")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "3 &middot; Series 3", "A British TV Hub Pick",
               "A British TV Hub selection from Series 3, broadcast across January 2015.",
               ["Series 3"], "At a Glance", [("Best For", "Fans of the improvised format")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "4 &middot; Series 5 &middot; 2016", "Series Finale",
               "The final episode of the final series, broadcast in August 2016, closing out the Metropolitan Police team's run.",
               ["Series Finale"], "At a Glance", [("Best For", "Viewers finishing the series")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
    ),
    "cast_cards": (
        card("badge-essential", "Lead", "Damien Molony", "A core member of the Metropolitan Police team at the center of the series.", ["Lead"], "At a Glance", [("Appears", "Multiple series")])
        + card("badge-essential", "Lead", "Clare-Hope Ashitey", "A lead detective working alongside the rest of the team across the series' run.", ["Lead"], "At a Glance", [("Appears", "Multiple series")])
        + card("badge-classic", "Recurring", "Fay Ripley", "A senior member of the police team, part of the show's regular ensemble.", ["Recurring"], "At a Glance", [("Appears", "Multiple series")])
        + card("badge-classic", "Recurring", "James Murray", "Part of the Suspects ensemble across the show's run.", ["Recurring"], "At a Glance", [("Appears", "Multiple series")])
    ),
    "special_cards": (
        card("badge-classic", "Format", "Largely Improvised Dialogue", "Most of the show's dialogue was improvised by the cast from character notes and detailed plot descriptions rather than a traditional script, with fly-on-the-wall filming meant to make reactions and investigations feel unusually realistic.", ["Improvised Format"], "At a Glance", [("Dialogue", "Mostly improvised")])
        + card("badge-classic", "Tone", "A Naturalistic Procedural", "The improvised approach gives Suspects a looser, more observational feel than most scripted British procedurals, closer to a documentary crew following real detectives.", ["Naturalistic"], "At a Glance", [("Style", "Fly-on-the-wall")])
        + card("badge-classic", "Planned Conclusion", "Five Series, a Deliberate Close", "Suspects ran for five series before concluding in 2016, with its fifth series understood as the show's final run.", ["Complete Run"], "At a Glance", [("Final Series", "Series 5, 2016")])
    ),
    "setting_card": card("badge-classic", "Setting &amp; Filming", "London, England", "Suspects is set at a London police station, with the Metropolitan Police investigating crimes across the city. Filming took place at Brownall House, a former Tower Hamlets Council office building on Cambridge Heath Road.", ["London, England"], "At a Glance", [("City", "London"), ("Filmed At", "Brownall House")]),
    "books_section": "",
    "faq_cards": (
        faq_card("Status", "Is Suspects finished?", "Yes. Suspects ran for five series between 2014 and 2016, with the fifth series understood as the show's final run.", [("Status", "Complete"), ("Ended", "2016")])
        + faq_card("Episode Count", "How many episodes of Suspects are there?", "There are 23 episodes across five series: 5, 4, 4, 4, and 6 episodes respectively.", [("Episodes", "23"), ("Series", "5")])
        + faq_card("Format", "Is Suspects scripted?", "Mostly not in the traditional sense. Most dialogue was improvised by the cast from character notes and plot outlines, with fly-on-the-wall filming for a more naturalistic feel.", [("Format", "Largely improvised")])
        + faq_card("Streaming", "Where can I watch Suspects in the US?", "Suspects is available via BritBox, Acorn TV, and PBS in the US, including through PBS Masterpiece's Amazon Channel and participating PBS member stations.", [("Available On", "BritBox, Acorn TV, PBS")])
        + faq_card("Filming Location", "Where is Suspects filmed?", "Suspects was filmed at Brownall House, a former council office building in Tower Hamlets, London, standing in for the show's police station.", [("City", "London")])
    ),
    "tvseries_jsonld": tvseries_jsonld("Suspects", None, "Suspects follows a Metropolitan Police team investigating crimes across London, with most dialogue improvised from character notes rather than a fully scripted script. Five series and 23 episodes aired between 2014 and 2016.", "British Crime Drama", 5, "2014", "2016", ["Damien Molony", "Clare-Hope Ashitey"], "https://britishtvhub.com/shows/suspects.html"),
    "faq_jsonld": faq_jsonld("Suspects", [
        ("Is Suspects finished?", "Yes. Suspects ran for five series between 2014 and 2016, with the fifth series understood as the show's final run."),
        ("How many episodes of Suspects are there?", "There are 23 episodes across five series: 5, 4, 4, 4, and 6 episodes respectively."),
        ("Is Suspects scripted?", "Mostly not in the traditional sense. Most dialogue was improvised by the cast from character notes and plot outlines, with fly-on-the-wall filming for a more naturalistic feel."),
        ("Where can I watch Suspects in the US?", "Suspects is available via BritBox, Acorn TV, and PBS in the US, including through PBS Masterpiece's Amazon Channel and participating PBS member stations."),
        ("Where is Suspects filmed?", "Suspects was filmed at Brownall House, a former council office building in Tower Hamlets, London, standing in for the show's police station."),
    ]),
})

# ============================================================ 8. THE GOOD SHIP MURDER
SHOWS.append({
    "slug": "the-good-ship-murder",
    "title": "The Good Ship Murder",
    "meta_desc": "Where to watch The Good Ship Murder in the US. The guide to Channel 5's cruise-ship mystery starring Shayne Ward, with Series 4 renewed.",
    "eyebrow": "British Cozy Mystery &middot; Channel 5 &middot; 2023&ndash;present &middot; Renewed for Series 4",
    "tags": ["3 Series + 2 Specials", "24 Episodes", "Stars Shayne Ward", "Mediterranean Cruise Ship", "Renewed for Series 4"],
    "description": "Shayne Ward stars as Jack Grayling, a former detective turned cruise-ship singer who keeps finding himself solving murders among the passengers of a Mediterranean cruise liner. Catherine Tyldesley played First Officer Kate Woods opposite him for the show's first three series. Three series and two Christmas specials have aired on Channel 5, 24 episodes in total, and the show has been renewed for a fourth series, which brings cast changes including Fiona Allen and Peter Davison. The Good Ship Murder streams on BritBox in the US.",
    "viewer_guide_heading": "New Viewer's <em>Guide</em>",
    "viewer_guide_card": card("badge-new", "Where to Start", "Series 1, Episode 1 (2023)",
        "Jack Grayling, a cruise-ship singer with a police past, is drawn into his first on-board murder investigation, setting up the light, sun-splashed tone the series keeps throughout.",
        ["Series 1", "2023"],
        "At a Glance", [("Watch Order", "Watch in order"), ("Cast Change", "Kate Woods departs after Series 3")]),
    "watch_block": watch_block("BritBox", BRITBOX, "Series 1&ndash;3 plus specials &middot; Subscription required", buy_title="The Good Ship Murder"),
    "episode_cards": (
        card("badge-essential", "1 &middot; Series 1 &middot; 2023", "Episode 1",
             "The series premiere, introducing Jack Grayling's unlikely second career solving murders aboard a Mediterranean cruise ship.",
             ["Series Premiere"], "At a Glance", [("Position", "Series 1, 2023"), ("Best For", "First-time viewers")],
             BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "2 &middot; Christmas Special &middot; 2024", "Holiday Special",
               "A British TV Hub pick for the show's first Christmas special, broadcast in December 2024 between Series 1 and Series 2.",
               ["Christmas Special"], "At a Glance", [("Best For", "Holiday viewing")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "3 &middot; Series 2 &middot; 2025", "A British TV Hub Pick",
               "A British TV Hub selection from Series 2, which aired weekly on BritBox in the US.",
               ["Series 2"], "At a Glance", [("Best For", "Returning fans")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
        + card("badge-classic", "4 &middot; Series 3 &middot; 2026", "A British TV Hub Pick",
               "A British TV Hub selection from the most recently aired series, Catherine Tyldesley's last full run as Kate Woods.",
               ["Final Series With Tyldesley"], "At a Glance", [("Best For", "Fans of the original pairing")],
               BRITBOX, "Watch via BritBox on Prime Video &rarr;")
    ),
    "cast_cards": (
        card("badge-essential", "Lead", "Shayne Ward", "Jack Grayling &mdash; a former detective now singing aboard a cruise ship, whose investigative instincts keep pulling him back into casework.", ["Lead"], "At a Glance", [("Role", "Jack Grayling"), ("Appears", "Series 1&ndash;4")])
        + card("badge-classic", "Series 1&ndash;3", "Catherine Tyldesley", "First Officer Kate Woods, Jack's partner in solving the ship's mysteries for the show's first three series; she departs the regular cast after Series 3 but returns to guest in the Series 4 premiere.", ["First Officer"], "At a Glance", [("Role", "Kate Woods"), ("Appears", "Series 1&ndash;3, S4 guest")])
        + card("badge-new", "Joins Series 4", "Fiona Allen", "Captain Serena \"The Iceberg\" Teller, taking command of the ship as part of the Series 4 cast changes.", ["Captain"], "At a Glance", [("Role", "Capt. Serena Teller"), ("Joins", "Series 4")])
        + card("badge-new", "Joins Series 4", "Peter Davison", "Eddie Grayling, joining the cast as part of the Series 4 lineup.", ["Series 4 Addition"], "At a Glance", [("Role", "Eddie Grayling"), ("Joins", "Series 4")])
    ),
    "special_cards": (
        card("badge-classic", "Setting as Character", "A Floating Mystery Setting", "The cruise ship itself, filmed aboard the MSC Virtuosa and around Malta, gives every mystery a sun-drenched, holiday backdrop distinct from the UK village settings common to the genre.", ["Cruise Ship Setting"], "At a Glance", [("Filmed Aboard", "MSC Virtuosa")])
        + card("badge-classic", "Tone", "A Light, Breezy Whodunit", "The series leans into a holiday-fantasy atmosphere, pairing gentle romantic comedy with its murder-of-the-week plots.", ["Light Mystery"], "At a Glance", [("Tone", "Breezy, warm")])
        + card("badge-classic", "Cast Refresh", "New Faces for Series 4", "With Catherine Tyldesley departing the regular cast, Series 4 brings in Fiona Allen and Peter Davison, refreshing the ship's crew while Shayne Ward's Jack Grayling remains the constant lead.", ["Cast Refresh"], "At a Glance", [("New for S4", "Fiona Allen, Peter Davison")])
    ),
    "setting_card": card("badge-classic", "Setting &amp; Filming", "A Mediterranean Cruise Ship", "The series is set aboard a luxury Mediterranean cruise ship and was filmed on the real MSC Virtuosa, which sails from Southampton, with much of the filming taking place around Malta.", ["Mediterranean"], "At a Glance", [("Ship", "MSC Virtuosa"), ("Filmed In", "Malta")]),
    "books_section": "",
    "faq_cards": (
        faq_card("Status", "Will there be a Series 4 of The Good Ship Murder?", "Yes. Channel 5 announced a fourth series in March 2026, bringing cast changes including Fiona Allen and Peter Davison.", [("Status", "Renewed"), ("Confirmed", "March 2026")])
        + faq_card("Cast Change", "Is Catherine Tyldesley leaving The Good Ship Murder?", "Yes. Tyldesley departs the regular cast after Series 3, though she returns to guest in the first episode of Series 4.", [("Departs After", "Series 3"), ("Guests In", "S4 premiere")])
        + faq_card("Episode Count", "How many episodes of The Good Ship Murder are there?", "There are 24 episodes so far across three series and two Christmas specials: 8 in Series 1, 7 in Series 2, 7 in Series 3, plus one episode in each special.", [("Episodes", "24"), ("Series", "3 + 2 specials")])
        + faq_card("Streaming", "Where can I watch The Good Ship Murder in the US?", "BritBox is The Good Ship Murder's US streaming home.", [("Primary", "BritBox")])
        + faq_card("Filming Location", "Where is The Good Ship Murder filmed?", "The series was filmed aboard the real MSC Virtuosa cruise ship, which sails from Southampton, with much of the production based around Malta.", [("Ship", "MSC Virtuosa"), ("Filmed In", "Malta")])
    ),
    "tvseries_jsonld": tvseries_jsonld("The Good Ship Murder", None, "Shayne Ward stars as Jack Grayling, a former detective turned cruise-ship singer who keeps solving murders among the passengers of a Mediterranean cruise liner. Three series and two Christmas specials have aired, with a fourth series renewed.", "British Cozy Mystery", 3, "2023", None, ["Shayne Ward", "Catherine Tyldesley"], "https://britishtvhub.com/shows/the-good-ship-murder.html"),
    "faq_jsonld": faq_jsonld("The Good Ship Murder", [
        ("Will there be a Series 4 of The Good Ship Murder?", "Yes. Channel 5 announced a fourth series in March 2026, bringing cast changes including Fiona Allen and Peter Davison."),
        ("Is Catherine Tyldesley leaving The Good Ship Murder?", "Yes. Tyldesley departs the regular cast after Series 3, though she returns to guest in the first episode of Series 4."),
        ("How many episodes of The Good Ship Murder are there?", "There are 24 episodes so far across three series and two Christmas specials: 8 in Series 1, 7 in Series 2, 7 in Series 3, plus one episode in each special."),
        ("Where can I watch The Good Ship Murder in the US?", "BritBox is The Good Ship Murder's US streaming home."),
        ("Where is The Good Ship Murder filmed?", "The series was filmed aboard the real MSC Virtuosa cruise ship, which sails from Southampton, with much of the production based around Malta."),
    ]),
})

# ============================================================ 9. QUEENS OF MYSTERY
SHOWS.append({
    "slug": "queens-of-mystery",
    "title": "Queens of Mystery",
    "meta_desc": "Where to watch Queens of Mystery in the US. The guide to Acorn TV's cozy mystery starring Julie Graham, Sarah Woodward, and Siobhan Redmond.",
    "eyebrow": "British Cozy Mystery &middot; Acorn TV Original &middot; 2019&ndash;2021 &middot; 2 Series",
    "tags": ["2 Series", "12 Episodes", "Stars Julie Graham", "Fictional Village of Wildemarsh", "Crime-Writing Aunts"],
    "description": "Julie Graham, Sarah Woodward, and Siobhan Redmond play three crime-writing sisters who can't resist helping their detective niece solve real murders in the fictional English village of Wildemarsh. Created by Julian Unthank for Acorn TV, the series ran for two series and twelve episodes (six two-part stories) between 2019 and 2021. No third series has been confirmed as of November 2026. Queens of Mystery streams on Acorn TV in the US.",
    "viewer_guide_heading": "New Viewer's <em>Guide</em>",
    "viewer_guide_card": card("badge-new", "Where to Start", "Series 1, Part 1 (2019)",
        "Detective Sergeant Matilda Stone, played by Olivia Vinall in Series 1, investigates her first Wildemarsh murder with her three crime-novelist aunts offering unwanted but often useful help.",
        ["Series 1", "2019"],
        "At a Glance", [("Watch Order", "Watch in order"), ("Cast Change", "Mattie Stone recast for Series 2")]),
    "watch_block": watch_block("Acorn TV", ACORN, "Both series, 12 episodes &middot; Subscription required", buy_title="Queens of Mystery"),
    "episode_cards": (
        card("badge-essential", "1 &middot; Series 1 &middot; 2019", "Part 1",
             "The series premiere, introducing the three Stone sisters and their niece, Detective Sergeant Mattie Stone, as they take on Wildemarsh's first case together.",
             ["Series Premiere"], "At a Glance", [("Position", "Series 1, 2019"), ("Best For", "First-time viewers")],
             ACORN, "Watch via Acorn TV on Prime Video &rarr;")
        + card("badge-classic", "2 &middot; Series 1", "A British TV Hub Pick",
               "A British TV Hub selection from the first series, showcasing the sisters' competing theories and cozy village humour.",
               ["Series 1"], "At a Glance", [("Best For", "Fans of ensemble comedy-mystery")],
               ACORN, "Watch via Acorn TV on Prime Video &rarr;")
        + card("badge-classic", "3 &middot; Series 2 &middot; 2021", "A British TV Hub Pick",
               "A British TV Hub selection from Series 2, which introduced Florence Hall as the recast Mattie Stone.",
               ["Series 2"], "At a Glance", [("Best For", "Returning viewers")],
               ACORN, "Watch via Acorn TV on Prime Video &rarr;")
    ),
    "cast_cards": (
        card("badge-essential", "Lead", "Julie Graham", "Cat Stone &mdash; one of the three crime-writing Stone sisters at the heart of the series.", ["Lead"], "At a Glance", [("Role", "Cat Stone"), ("Appears", "Both series")])
        + card("badge-essential", "Lead", "Sarah Woodward", "Beth Stone, another of the mystery-solving Stone sisters.", ["Lead"], "At a Glance", [("Role", "Beth Stone"), ("Appears", "Both series")])
        + card("badge-essential", "Lead", "Siobhan Redmond", "Jane Stone, completing the trio of crime-writing aunts.", ["Lead"], "At a Glance", [("Role", "Jane Stone"), ("Appears", "Both series")])
        + card("badge-classic", "Series 1", "Olivia Vinall", "Detective Sergeant Matilda \"Mattie\" Stone, the aunts' niece and the police officer whose cases they keep getting pulled into, in Series 1.", ["Detective Sergeant"], "At a Glance", [("Role", "DS Mattie Stone"), ("Appears", "Series 1")])
        + card("badge-new", "Recast for Series 2", "Florence Hall", "Taking over the role of Detective Sergeant Mattie Stone for Series 2.", ["Detective Sergeant"], "At a Glance", [("Role", "DS Mattie Stone"), ("Appears", "Series 2")])
    ),
    "special_cards": (
        card("badge-classic", "Premise", "Three Aunts Who Can't Resist a Case", "The show's core joke and charm is that the Stone sisters, all crime novelists, are constitutionally unable to stay out of their niece's real police investigations.", ["Amateur Sleuths"], "At a Glance", [("Trio", "Cat, Beth, Jane Stone")])
        + card("badge-classic", "Structure", "Six Two-Part Mysteries", "Each series tells three two-part mysteries, giving every case room to unfold over roughly 90 minutes of combined runtime rather than a single compressed episode.", ["Two-Part Mysteries"], "At a Glance", [("Format", "Two-part stories")])
        + card("badge-classic", "Narration", "A Literary, Storybook Framing", "The series is narrated, giving the whole show a storybook quality that matches its cozy, village-set tone.", ["Narrated"], "At a Glance", [("Narrator", "Juliet Stevenson")])
    ),
    "setting_card": card("badge-classic", "Setting &amp; Filming", "The Fictional Village of Wildemarsh", "Queens of Mystery is set in the fictional English village of Wildemarsh. Filming took place in Kent, including Stone Street in Cranbrook, Farningham, Smarden, Benenden, and Lympne Castle.", ["Kent, England"], "At a Glance", [("Fictional Setting", "Wildemarsh"), ("Filmed In", "Kent")]),
    "books_section": "",
    "faq_cards": (
        faq_card("Status", "Will there be a Series 3 of Queens of Mystery?", "No third series has been confirmed as of November 2026. The show was renewed for Series 2 in March 2021, but no further renewal or cancellation has been announced since.", [("Status", "Unconfirmed")])
        + faq_card("Episode Count", "How many episodes of Queens of Mystery are there?", "There are 12 episodes across two series, six each, structured as six two-part mysteries.", [("Episodes", "12"), ("Series", "2")])
        + faq_card("Cast", "Who plays the aunts in Queens of Mystery?", "Julie Graham, Sarah Woodward, and Siobhan Redmond play the three crime-writing Stone sisters, Cat, Beth, and Jane.", [("Cast", "Julie Graham, Sarah Woodward, Siobhan Redmond")])
        + faq_card("Cast Change", "Why did the actress playing Mattie Stone change?", "Olivia Vinall played Detective Sergeant Mattie Stone in Series 1; Florence Hall took over the role for Series 2.", [("Series 1", "Olivia Vinall"), ("Series 2", "Florence Hall")])
        + faq_card("Streaming", "Where can I watch Queens of Mystery in the US?", "Acorn TV is Queens of Mystery's US streaming home, with both series available to subscribers.", [("Primary", "Acorn TV")])
        + faq_card("Filming Location", "Where is Queens of Mystery filmed?", "The series is set in the fictional village of Wildemarsh and was filmed on location in Kent, England.", [("Region", "Kent")])
    ),
    "tvseries_jsonld": tvseries_jsonld("Queens of Mystery", None, "Julie Graham, Sarah Woodward, and Siobhan Redmond play three crime-writing sisters who help their detective niece solve murders in the fictional village of Wildemarsh. Two series and twelve episodes aired between 2019 and 2021.", "British Cozy Mystery", 2, "2019", "2021", ["Julie Graham", "Sarah Woodward", "Siobhan Redmond"], "https://britishtvhub.com/shows/queens-of-mystery.html"),
    "faq_jsonld": faq_jsonld("Queens of Mystery", [
        ("Will there be a Series 3 of Queens of Mystery?", "No third series has been confirmed as of November 2026. The show was renewed for Series 2 in March 2021, but no further renewal or cancellation has been announced since."),
        ("How many episodes of Queens of Mystery are there?", "There are 12 episodes across two series, six each, structured as six two-part mysteries."),
        ("Who plays the aunts in Queens of Mystery?", "Julie Graham, Sarah Woodward, and Siobhan Redmond play the three crime-writing Stone sisters, Cat, Beth, and Jane."),
        ("Why did the actress playing Mattie Stone change?", "Olivia Vinall played Detective Sergeant Mattie Stone in Series 1; Florence Hall took over the role for Series 2."),
        ("Where can I watch Queens of Mystery in the US?", "Acorn TV is Queens of Mystery's US streaming home, with both series available to subscribers."),
        ("Where is Queens of Mystery filmed?", "The series is set in the fictional village of Wildemarsh and was filmed on location in Kent, England."),
    ]),
})

# ============================================================ 10. THE PUZZLE LADY
SHOWS.append({
    "slug": "the-puzzle-lady",
    "title": "The Puzzle Lady",
    "meta_desc": "Where to watch The Puzzle Lady in the US. The guide to Phyllis Logan's Channel 5 mystery, known in the UK as Murder Most Puzzling.",
    "eyebrow": "British Cozy Mystery &middot; PBS &middot; 2025&ndash;present &middot; Series 1",
    "tags": ["6 Episodes", "Stars Phyllis Logan", "Fictional Town of Bakerbury", "Based on the Novels", "New for 2025/26"],
    "description": "Phyllis Logan stars as Cora Felton, a celebrity crossword compiler known as \"The Puzzle Lady,\" who helps the local police solve murders in the small town of Bakerbury, based on Parnell Hall's bestselling Puzzle Lady novels. Charlotte Hope plays Cora's niece Sherry, who does the actual puzzle-setting behind Cora's public persona. The show aired on Channel 5 in the UK under the title Murder Most Puzzling and airs on PBS member stations in the US as The Puzzle Lady. Series 1 ran six episodes, broadcast in two batches between June 2025 and March 2026.",
    "viewer_guide_heading": "New Viewer's <em>Guide</em>",
    "viewer_guide_card": card("badge-new", "Where to Start", "Episode 1 (2025)",
        "Cora Felton and her niece Sherry move to the sleepy town of Bakerbury to escape a mysterious pursuer from their past, only for a teenage girl's murder to pull Cora into her first local case.",
        ["Episode 1", "2025"],
        "At a Glance", [("Watch Order", "Watch in order"), ("UK Title", "Murder Most Puzzling")]),
    "watch_block": watch_block("PBS", MASTERPIECE, "Series 1, 6 episodes &middot; Availability varies by station",
        also="The Puzzle Lady airs on participating PBS member stations and via PBS Passport. It is a general PBS drama rather than a Masterpiece-branded title, so availability and timing vary by local station; check your local PBS station's schedule.",
        buy_title="The Puzzle Lady TV series"),
    "episode_cards": (
        card("badge-essential", "1 &middot; Episode 1 &middot; 2025", "Series Premiere",
             "The opening episode, introducing Cora Felton's public persona as the crossword-compiling Puzzle Lady and the murder that pulls her into Bakerbury's police investigation.",
             ["Series Premiere"], "At a Glance", [("Position", "Episode 1, 2025"), ("Best For", "First-time viewers")])
        + card("badge-classic", "2 &middot; Episode 3", "A British TV Hub Pick",
               "A British TV Hub selection, following Cora as she is hired by a solicitor to look into a convicted killer's case around her birthday.",
               ["Case Reopened"], "At a Glance", [("Best For", "Fans of tipsy-amateur-sleuth mysteries")])
        + card("badge-classic", "3 &middot; Episode 6 &middot; 2026", "Series Finale",
               "The final episode of Series 1, broadcast in March 2026, closing out Cora and Sherry's first run of Bakerbury mysteries.",
               ["Series Finale"], "At a Glance", [("Best For", "Viewers finishing Series 1")])
    ),
    "cast_cards": (
        card("badge-essential", "Lead", "Phyllis Logan", "Cora Felton &mdash; the eccentric, no-nonsense celebrity crossword compiler known as \"The Puzzle Lady,\" whose public image hides the fact that her niece actually sets the puzzles.", ["Lead"], "At a Glance", [("Role", "Cora Felton")])
        + card("badge-essential", "Lead", "Charlotte Hope", "Sherry Carter, Cora's niece, who writes the crosswords behind Cora's famous byline while the two hide from a pursuer in their past.", ["Lead"], "At a Glance", [("Role", "Sherry Carter")])
        + card("badge-classic", "Recurring", "Adam Best", "DCI Derek Hooper, the local police officer whose investigations keep intersecting with Cora's amateur sleuthing.", ["Detective Chief Inspector"], "At a Glance", [("Role", "DCI Derek Hooper")])
        + card("badge-classic", "Recurring", "Kevin McNally", "Gilbert Sullivan, part of the Bakerbury supporting cast.", ["Recurring"], "At a Glance", [("Role", "Gilbert Sullivan")])
    ),
    "special_cards": (
        card("badge-classic", "Source Material", "Based on Parnell Hall's Puzzle Lady Novels", "The series adapts Parnell Hall's long-running, bestselling Puzzle Lady series of cozy mystery novels, carrying over Cora Felton's crossword-compiler alter ego from the books.", ["Novel Adaptation"], "At a Glance", [("Author", "Parnell Hall")])
        + card("badge-classic", "Dual Titles", "Different Names on Each Side of the Atlantic", "The show was announced under the working title The Puzzle Lady, aired in the UK on Channel 5 as Murder Most Puzzling, and is broadcast in the US on PBS stations under the original title, The Puzzle Lady.", ["Title Variation"], "At a Glance", [("UK Title", "Murder Most Puzzling"), ("US Title", "The Puzzle Lady")])
        + card("badge-classic", "Premise", "A Secret Behind the Byline", "Much of the show's gentle comedy comes from the gap between Cora's public image as a crossword genius and the reality that her niece Sherry does the actual puzzle-writing.", ["Comic Premise"], "At a Glance", [("Hook", "Cora's hidden secret")])
    ),
    "setting_card": card("badge-classic", "Setting &amp; Filming", "The Fictional Town of Bakerbury", "The Puzzle Lady is set in the fictional English town of Bakerbury. Filming took place in Northern Ireland in late 2024.", ["Northern Ireland"], "At a Glance", [("Fictional Setting", "Bakerbury"), ("Filmed In", "Northern Ireland")]),
    "books_section": "  " + f'''<div class="section-header">
    <h2>Books Behind the <em>Series</em></h2>
  </div>

''' + card("badge-classic", "Source Novels", "Parnell Hall's Puzzle Lady Series", "The Puzzle Lady adapts Parnell Hall's bestselling Puzzle Lady series of cozy mystery novels, which follow Cora Felton's crossword-compiler persona through a long-running string of books.", ["Novel Series"], "At a Glance", [("Author", "Parnell Hall")]) + "\n  <hr class=\"divider\">\n\n",
    "faq_cards": (
        faq_card("Naming", "Is The Puzzle Lady the same show as Murder Most Puzzling?", "Yes. The series was announced under the working title The Puzzle Lady, aired in the UK on Channel 5 as Murder Most Puzzling, and airs in the US on PBS stations under the title The Puzzle Lady.", [("UK Title", "Murder Most Puzzling"), ("US Title", "The Puzzle Lady")])
        + faq_card("Status", "Will there be a Series 2 of The Puzzle Lady?", "No second series has been confirmed as of November 2026. Series 1 ran six episodes, broadcast in the UK in two batches between June 2025 and March 2026.", [("Status", "Unconfirmed")])
        + faq_card("Episode Count", "How many episodes of The Puzzle Lady are there?", "Series 1 has six episodes.", [("Episodes", "6")])
        + faq_card("Source Material", "Is The Puzzle Lady based on a book?", "Yes. It adapts Parnell Hall's bestselling Puzzle Lady series of cozy mystery novels.", [("Author", "Parnell Hall")])
        + faq_card("Streaming", "Where can I watch The Puzzle Lady in the US?", "The Puzzle Lady airs on participating PBS member stations and via PBS Passport. It is a general PBS title rather than a Masterpiece-branded one, so exact availability varies by local station; check your local PBS station's schedule for air dates.", [("US Network", "PBS member stations")])
        + faq_card("Filming Location", "Where is The Puzzle Lady filmed?", "The series is set in the fictional town of Bakerbury and was filmed on location in Northern Ireland.", [("Filmed In", "Northern Ireland")])
    ),
    "tvseries_jsonld": tvseries_jsonld("The Puzzle Lady", "Murder Most Puzzling", "Phyllis Logan stars as Cora Felton, a celebrity crossword compiler known as the Puzzle Lady, who helps solve murders in the small English town of Bakerbury, based on Parnell Hall's novels. Series 1 ran six episodes, broadcast in the UK as Murder Most Puzzling.", "British Cozy Mystery", 1, "2025", None, ["Phyllis Logan", "Charlotte Hope"], "https://britishtvhub.com/shows/the-puzzle-lady.html"),
    "faq_jsonld": faq_jsonld("The Puzzle Lady", [
        ("Is The Puzzle Lady the same show as Murder Most Puzzling?", "Yes. The series was announced under the working title The Puzzle Lady, aired in the UK on Channel 5 as Murder Most Puzzling, and airs in the US on PBS stations under the title The Puzzle Lady."),
        ("Will there be a Series 2 of The Puzzle Lady?", "No second series has been confirmed as of November 2026. Series 1 ran six episodes, broadcast in the UK in two batches between June 2025 and March 2026."),
        ("How many episodes of The Puzzle Lady are there?", "Series 1 has six episodes."),
        ("Is The Puzzle Lady based on a book?", "Yes. It adapts Parnell Hall's bestselling Puzzle Lady series of cozy mystery novels."),
        ("Where can I watch The Puzzle Lady in the US?", "The Puzzle Lady airs on participating PBS member stations and via PBS Passport. It is a general PBS title rather than a Masterpiece-branded one, so exact availability varies by local station; check your local PBS station's schedule for air dates."),
        ("Where is The Puzzle Lady filmed?", "The series is set in the fictional town of Bakerbury and was filmed on location in Northern Ireland."),
    ]),
})
