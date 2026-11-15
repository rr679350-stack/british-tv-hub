files = ["silent-witness","sherwood","dalgliesh","the-chelsea-detective","trigger-point","lynley","victoria","poldark"]
for f in files:
    path = f"shows/{f}.html"
    html = open(path, encoding="utf-8").read()
    print(f"=== {f}.html ===")
    print(" div:", html.count("<div"), html.count("</div>"))
    print(" a:", html.count("<a "), html.count("</a>"))
    print(f" shows-like-{f}-tv count:", html.count(f"shows-like-{f}-tv"))
