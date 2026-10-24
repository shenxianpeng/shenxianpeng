"""Render the profile banners in the blog's Evergreen design system.

The banner is a passing pipeline, drawn the way Jenkins and GitHub Actions
draw one: stage name, a green check, and the project that runs at that stage.
Colours and fonts come from shenxianpeng/blog (assets/css/schemes/evergreen.css,
DESIGN.md): Geist for type, Geist Mono for stage names.

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
    "dark": dict(bg="#111914", ink="#F2F3EF", muted="#8A968E", accent="#4FB88A",
                 check="#111914", dot="rgba(242,243,239,.055)"),
    "light": dict(bg="#F2F3EF", ink="#0D120F", muted="#5C665F", accent="#1D6A4B",
                  check="#F2F3EF", dot="rgba(13,18,15,.06)"),
}

# stage, main project, second project (optional)
STAGES = [
    ("commit", "commit-check", "Conventional Branch"),
    ("review", "cpp-linter", ""),
    ("build", "explain-error", "Agent8"),
    ("release", "clang-tools", "static binaries"),
]


def pipeline(t, x0, x1, y, s):
    """Stages evenly spaced from x0 to x1 on a line at y; s scales every size."""
    step = (x1 - x0) / (len(STAGES) - 1)
    r = 15 * s
    out = [f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{t["accent"]}" '
           f'stroke-width="{3 * s}" stroke-linecap="round"/>']
    for i, (stage, main, sub) in enumerate(STAGES):
        cx = x0 + i * step
        out += [
            f'<circle cx="{cx}" cy="{y}" r="{r + 5 * s}" fill="{t["bg"]}"/>',
            f'<circle cx="{cx}" cy="{y}" r="{r}" fill="{t["accent"]}"/>',
            f'<path d="M{cx - 6.5 * s},{y + 0.5 * s} L{cx - 2 * s},{y + 5 * s} L{cx + 7 * s},{y - 5 * s}" '
            f'fill="none" stroke="{t["check"]}" stroke-width="{3.2 * s}" stroke-linecap="round" stroke-linejoin="round"/>',
            f'<text x="{cx}" y="{y - 34 * s}" text-anchor="middle" class="stage" font-size="{22 * s}" fill="{t["muted"]}">{stage}</text>',
            f'<text x="{cx}" y="{y + 58 * s}" text-anchor="middle" class="proj" font-size="{27 * s}" fill="{t["ink"]}">{main}</text>',
        ]
        if sub:
            out.append(f'<text x="{cx}" y="{y + 92 * s}" text-anchor="middle" class="proj sub" '
                       f'font-size="{23 * s}" fill="{t["muted"]}">{sub}</text>')
    return "\n".join(out)


def page(w, h, t, body):
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400..800&family=Geist+Mono:wght@400..600&display=swap">
<style>
html,body{{margin:0;padding:0}}
body{{width:{w}px;height:{h}px;overflow:hidden;background:{t['bg']};
  background-image:radial-gradient({t['dot']} 1.4px,transparent 1.6px);background-size:32px 32px;background-position:16px 16px}}
svg{{display:block}}
.h{{font-family:Geist,system-ui,sans-serif;font-weight:700;letter-spacing:-0.045em}}
.stage,.meta{{font-family:'Geist Mono',ui-monospace,monospace;font-weight:500}}
.stage{{letter-spacing:.02em}}
.proj{{font-family:Geist,system-ui,sans-serif;font-weight:600;letter-spacing:-0.01em}}
.sub{{font-weight:500}}
</style></head><body>
<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">{body}</svg>
</body></html>"""


def github(theme):
    """README banner. No name or URL: the profile page shows both."""
    t = THEMES[theme]
    w, h = 1920, 320
    body = f'''<text x="128" y="144" class="h" font-size="82" fill="{t['ink']}">From commit</text>
<text x="128" y="232" class="h" font-size="82" fill="{t['ink']}">to release.</text>
{pipeline(t, 820, 1700, 146, 1.1)}'''
    return w, h, page(w, h, t, body)


def x_header():
    """X header. Text stays right of x=437: the avatar covers the bottom-left corner."""
    t = THEMES["dark"]
    w, h = 1500, 500
    body = f'''<text x="1380" y="100" text-anchor="end" class="meta" font-size="22" fill="{t['muted']}">shenxianpeng.dev</text>
<text x="1380" y="206" text-anchor="end" class="h" font-size="104" fill="{t['ink']}">From commit to release.</text>
{pipeline(t, 541, 1300, 318, 0.95)}'''
    return w, h, page(w, h, t, body)


def linkedin():
    """LinkedIn background. Text stays right of x=487: the avatar covers the left side."""
    t = THEMES["dark"]
    w, h = 1584, 396
    body = f'''<text x="1480" y="62" text-anchor="end" class="meta" font-size="20" fill="{t['muted']}">shenxianpeng.dev</text>
<text x="1480" y="150" text-anchor="end" class="h" font-size="84" fill="{t['ink']}">From commit to release.</text>
{pipeline(t, 596, 1398, 244, 1.0)}'''
    return w, h, page(w, h, t, body)


JOBS = {
    "github-dark-1920x320.png": github("dark"),
    "github-light-1920x320.png": github("light"),
    "x-1500x500.png": x_header(),
    "linkedin-1584x396.png": linkedin(),
}

FONTS = ["700 90px Geist", "600 32px Geist", "500 28px Geist", '500 26px "Geist Mono"']

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for name, (w, h, html) in JOBS.items():
            pg = browser.new_page(viewport={"width": w, "height": h})
            pg.set_content(html, wait_until="networkidle")
            # SVG text does not trigger web-font loading by itself; ask for each face.
            pg.evaluate("fs => Promise.all(fs.map(f => document.fonts.load(f))).then(() => document.fonts.ready)", FONTS)
            pg.wait_for_timeout(300)
            pg.screenshot(path=str(OUT / name), clip={"x": 0, "y": 0, "width": w, "height": h})
            pg.close()
            print("wrote", OUT / name)
        browser.close()
