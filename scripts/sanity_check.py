import re, sys

files = [
    "shows-like-silent-witness-tv.html",
    "shows-like-sherwood-tv.html",
    "shows-like-the-gold-tv.html",
    "shows-like-dalgliesh-tv.html",
    "shows-like-victoria-tv.html",
    "shows-like-poldark-tv.html",
    "shows-like-the-chelsea-detective-tv.html",
    "shows-like-trigger-point-tv.html",
    "shows-like-madame-blanc-mysteries-tv.html",
    "shows-like-lynley-tv.html",
]

for fname in files:
    html = open(fname, encoding="utf-8").read()
    print(f"=== {fname} ===")
    print(" divs:", html.count("<div"), html.count("</div>"))
    print(" a tags:", html.count("<a "), html.count("</a>"))
    print(" script tags:", html.count("<script"), html.count("</script>"))
    print(" size:", len(html))
    print(" Netflix mentions:", html.count("Netflix"))
    amazon_text = re.findall(r">([^<>]*Amazon[^<>]*)<", html)
    print(" Amazon-in-visible-text:", amazon_text)
    placeholders = re.findall(r"\{[a-z_]+\}", html)
    print(" unfilled placeholders:", placeholders[:5])
    print()
