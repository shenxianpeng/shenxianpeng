"""Render the profile banners in the blog's Evergreen design system.

Every banner is the headline "From commit to release." with the pipeline drawn
as a line under it, one dot per stage. There is no small text: X and LinkedIn
show these images at about half of their width on a desktop and at a quarter
on a phone, so stage and project names became too small to read. The X bio and
the LinkedIn About carry those names. The GitHub profile README uses a text
heading instead of an image.
Colours and fonts come from shenxianpeng/blog (assets/css/schemes/evergreen.css,
DESIGN.md): Geist for type.

    pip install playwright   # uses a local Chromium; fonts load from Google Fonts
    python3 assets/brand/gen_banners.py            # writes next to this script
    python3 assets/brand/gen_banners.py out-dir    # or into another directory
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent
OUT.mkdir(parents=True, exist_ok=True)

THEMES = {
    "dark": dict(bg="#111914", ink="#F2F3EF", accent="#4FB88A", dot="rgba(242,243,239,.055)"),
    "light": dict(bg="#F2F3EF", ink="#0D120F", accent="#1D6A4B", dot="rgba(13,18,15,.06)"),
}

# One dot per stage on the line under the headline.
STAGES = ["commit", "review", "build", "release"]


def page(w, h, t, body):
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400..800&display=swap">
<style>
html,body{{margin:0;padding:0}}
body{{width:{w}px;height:{h}px;overflow:hidden;position:relative;background:{t['bg']};
  background-image:radial-gradient({t['dot']} 1.4px,transparent 1.6px);background-size:32px 32px;background-position:16px 16px}}
.h{{font-family:Geist,system-ui,sans-serif;font-weight:700;letter-spacing:-0.045em}}
</style></head><body>
{body}
</body></html>"""


def headline(t, size):
    """The headline with the pipeline line under it, as wide as the headline.

    Dot size and spacing scale with the type: 19 px dots and a 34 px gap at 120 px.
    """
    d = round(size * 0.16)
    gap = round(size * 0.28)
    dot = f'<span style="width:{d}px;height:{d}px;border-radius:50%;background:{t["accent"]}"></span>'
    return f'''<div style="display:inline-flex;flex-direction:column;gap:{gap}px">
    <div class="h" style="font-size:{size}px;line-height:1;color:{t['ink']};white-space:nowrap">From commit to release.</div>
    <div style="position:relative;height:{d}px">
      <div style="position:absolute;left:{d // 2}px;right:{d // 2}px;top:{(d - 3) // 2}px;height:3px;background:{t['accent']}"></div>
      <div style="position:relative;display:flex;justify-content:space-between">{dot * len(STAGES)}</div>
    </div>
  </div>'''


def x_header():
    """X header, right-aligned: the avatar covers the bottom-left corner (x < 375, y > 333).

    X shows it about 600 px wide on a desktop and 390 px on a phone.
    """
    t = THEMES["dark"]
    w, h = 1500, 500
    body = f'<div style="position:absolute;right:120px;top:160px">{headline(t, 104)}</div>'
    return w, h, page(w, h, t, body)


def linkedin():
    """LinkedIn background, right-aligned: the photo covers the left side (x < 347).

    LinkedIn shows it about 804 px wide on a desktop and 390 px on a phone.
    """
    t = THEMES["dark"]
    w, h = 1584, 396
    body = f'<div style="position:absolute;right:104px;top:136px">{headline(t, 84)}</div>'
    return w, h, page(w, h, t, body)


JOBS = {
    "x-1500x500.png": x_header(),
    "linkedin-1584x396.png": linkedin(),
}

FONTS = ["700 104px Geist"]

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for name, (w, h, html) in JOBS.items():
            pg = browser.new_page(viewport={"width": w, "height": h})
            pg.set_content(html, wait_until="networkidle")
            pg.evaluate("fs => Promise.all(fs.map(f => document.fonts.load(f))).then(() => document.fonts.ready)", FONTS)
            pg.wait_for_timeout(300)
            pg.screenshot(path=str(OUT / name), clip={"x": 0, "y": 0, "width": w, "height": h})
            pg.close()
            print("wrote", OUT / name)
        browser.close()
