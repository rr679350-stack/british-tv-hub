import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import build_shows_like_nov8 as b
import shows_like_nov8_data as d

os.chdir(os.path.join(os.path.dirname(__file__), ".."))
for cfg in d.PAGES:
    b.build_page(cfg)
print("done")
