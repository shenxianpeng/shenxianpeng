"""Render the profile banners and the pipeline diagram in the blog's Evergreen design system.

Every banner is the headline "From commit to release." with the pipeline drawn
as a line under it, one dot per stage. There is no small text: X and LinkedIn
show these images at about half of their width on a desktop and at a quarter
on a phone, so stage and project names became too small to read. The X bio and
the LinkedIn About carry those names. The GitHub profile README uses a text
heading instead of an image.
Colours and fonts come from shenxianpeng/blog (assets/css/schemes/evergreen.css,
DESIGN.md): Geist for type.

The pipeline diagram (pipeline-*.png) is the long form for slides and
articles, where it is shown at full width: the headline "From commit to
release, and long after.", the same line with a fifth dot for support, and
under each dot the stage name and its projects.

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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400..800&family=Geist+Mono:wght@400..600&family=Noto+Sans+SC:wght@400;700&display=swap">
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


# The diagram's stages and projects: the rows of the profile README and
# data/pipeline.yaml in shenxianpeng/blog. Change the three together.
PIPELINE = [
    ("commit", ["commit-check", "Conventional Branch"]),
    ("review", ["cpp-linter"]),
    ("build", ["explain-error", "jenkinsfilelint", "Agent8"]),
    ("release", ["release-ledger", "clang-tools binaries"]),
    ("support", ["Jenkins Extended Security", "MkDocs NG"]),
]

PIPELINE_HEADLINE = {
    "en": "From commit to release, and long after.",
    "zh": "从提交到发布，再到发布之后。",
}

# The positioning line, under the headline.
PIPELINE_LINE = {
    "en": "Open-source tools that keep software shipping, even after upstream moves on.",
    "zh": "帮团队把软件稳稳发出去的开源工具，上游不管了也一样。",
}


def pipeline(theme, lang="en"):
    """The pipeline as a diagram, 1600x900, for slides and articles.

    One column per stage: its dot on the line, the stage name, its projects.
    The line into the last stage is dashed: it stands for years, where the
    others stand for minutes.
    """
    t = THEMES[theme]
    w, h = 1600, 900
    pad, d = 120, 22
    font = "'Noto Sans SC',Geist,sans-serif" if lang == "zh" else "Geist,system-ui,sans-serif"
    spacing = "0" if lang == "zh" else "-0.045em"
    muted = "rgba(242,243,239,.62)" if theme == "dark" else "rgba(13,18,15,.62)"
    chip = "rgba(242,243,239,.09)" if theme == "dark" else "rgba(13,18,15,.07)"
    cols = []
    for i, (stage, projects) in enumerate(PIPELINE):
        last, before_last = i == len(PIPELINE) - 1, i == len(PIPELINE) - 2
        line = "" if last else (
            f'<div style="position:absolute;left:{d}px;right:0;top:{(d - 4) // 2}px;height:4px;'
            + (f'background:repeating-linear-gradient(to right,{t["accent"]} 0 14px,transparent 14px 26px)'
               if before_last else f'background:{t["accent"]}')
            + '"></div>')
        names = "".join(f'<div style="margin-top:14px">{n}</div>' for n in projects)
        cols.append(f'''<div style="position:relative;flex:1;padding-right:28px">
      {line}
      <div style="width:{d}px;height:{d}px;border-radius:50%;background:{t['accent']}"></div>
      <div style="display:inline-block;margin-top:34px;padding:4px 14px;border-radius:8px;background:{chip};
        font:500 26px 'Geist Mono',monospace;color:{t['ink']}">{stage}</div>
      <div style="margin-top:14px;font:500 27px/1.25 Geist,system-ui,sans-serif;color:{t['accent']}">{names}</div>
    </div>''')
    body = f'''<div style="position:absolute;left:{pad}px;right:{pad - 28}px;top:132px">
    <div style="font:700 68px/1.1 {font};letter-spacing:{spacing};color:{t['ink']}">{PIPELINE_HEADLINE[lang]}</div>
    <div style="margin-top:26px;font:400 31px/1.3 {font};color:{muted}">{PIPELINE_LINE[lang]}</div>
    <div style="display:flex;margin-top:96px">{"".join(cols)}</div>
  </div>
  <div style="position:absolute;left:{pad}px;bottom:84px;font:500 24px Geist,system-ui,sans-serif;color:{muted}">shenxianpeng.dev</div>'''
    return w, h, page(w, h, t, body)


JOBS = {
    "x-1500x500.png": x_header(),
    "linkedin-1584x396.png": linkedin(),
    "pipeline-1600x900.png": pipeline("dark"),
    "pipeline-light-1600x900.png": pipeline("light"),
    "pipeline-zh-1600x900.png": pipeline("dark", "zh"),
}

FONTS = ["700 104px Geist", "500 27px Geist", "500 26px 'Geist Mono'", "700 68px 'Noto Sans SC'", "400 31px Geist"]

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
