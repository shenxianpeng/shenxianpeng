# Personal Brand Assets · 个人品牌素材

"From commit to release." 横幅：一句标题，下面一条带四个点的线，代表 commit → review → build → release
四个阶段。图上不放阶段名和项目名：GitHub、X、LinkedIn 在桌面上把图缩到原宽的三分之一到一半，
手机上缩到四分之一以下，小字缩完都看不清。阶段和项目写在 README 正文、X 简介和 LinkedIn About 里。

| 平台 | 原图宽 | 桌面显示宽 | 手机显示宽 | 标题在桌面 / 手机上的大小 |
| --- | --- | --- | --- | --- |
| GitHub | 1920 | 846 | 308 | 53 / 19 px |
| X | 1500 | 约 600 | 约 390 | 42 / 27 px |
| LinkedIn | 1584 | 约 804 | 约 390 | 43 / 21 px |

配色和字体与博客 shenxianpeng.dev 的 Evergreen 设计系统一致
（`shenxianpeng/blog` 的 `assets/css/schemes/evergreen.css` 与 `DESIGN.md`）：
深色 `#111914` / 浅色 `#F2F3EF` 底，强调色 `#4FB88A` / `#1D6A4B`，Geist。

| File | Size | Intended use |
| --- | --- | --- |
| `github-dark-1920x320.png` | 1920×320 | GitHub 主页 README，深色主题。只有标题，不写名字和网址，页面本身已有 |
| `github-light-1920x320.png` | 1920×320 | GitHub 主页 README，浅色主题 |
| `x-1500x500.png` | 1500×500 | X 头图，深色，右对齐。左下角（x < 375、y > 333）留给头像 |
| `linkedin-1584x396.png` | 1584×396 | LinkedIn 背景图，深色，右对齐。左侧（x < 347）留给头像 |

以上四张由 `gen_banners.py` 生成，改文案或项目后重跑即可：

```bash
pip install playwright
python3 assets/brand/gen_banners.py
```

下面几张还是旧版 "ENGINEER. BUILDER. MAINTAINER." 设计，待用同一脚本重出：

| File | Size | Intended use |
| --- | --- | --- |
| `generic-1920x480.png` / `generic-light-1920x480.png` | 1920×480 | 通用横幅（博客、Slides 等） |
| `youtube-2560x1440.png` | 2560×1440 | YouTube channel art |
| `wechat-card-900.png` | 900 宽 | 微信公众号 "关于我" 名片 |
