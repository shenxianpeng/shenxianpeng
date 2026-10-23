# Personal Brand Assets · 个人品牌素材

"From commit to release." 横幅：一条全部通过的流水线，每一站标出在那里运行的项目
（commit → commit-check / Conventional Branch，review → cpp-linter，
build → explain-error / Agent8，release → Open Delivery Spec）。

配色和字体与博客 shenxianpeng.dev 的 Evergreen 设计系统一致
（`shenxianpeng/blog` 的 `assets/css/schemes/evergreen.css` 与 `DESIGN.md`）：
深色 `#111914` / 浅色 `#F2F3EF` 底，强调色 `#4FB88A` / `#1D6A4B`，Geist 与 Geist Mono。

| File | Size | Intended use |
| --- | --- | --- |
| `github-dark-1920x320.png` | 1920×320 | GitHub 主页 README，深色主题。不写名字和网址，页面本身已有 |
| `github-light-1920x320.png` | 1920×320 | GitHub 主页 README，浅色主题 |
| `x-1500x500.png` | 1500×500 | X 头图。文字在 x ≥ 437 区域，避开左下角头像 |
| `linkedin-1584x396.png` | 1584×396 | LinkedIn 背景图。文字在 x ≥ 487 区域，避开左侧头像 |

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
