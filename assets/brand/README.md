# Personal Brand Assets · 个人品牌素材

## 定位文案

所有平台用同一句话开头，改的时候一起改（博客首页、About 页、GitHub 主页 README、X、LinkedIn、公众号）。

| 用途 | English | 中文 |
| --- | --- | --- |
| 定位句 | Release engineer. I build open-source tools that keep software shipping, even after upstream moves on. | 发布工程师。我做开源工具，帮团队把软件稳稳发出去，上游不管了也一样。 |
| 标题 | From commit to release, and long after. | 从提交到发布，再到发布之后。 |
| 短标题（首页大字） | Keep software shipping. | 把软件稳稳发出去。 |
| 资历 | On the build, test and release side of software since 2009. | 2009 年入行，一直在做构建、测试和发布。 |

为什么是发布这一段（About 页第二段，写文章、做分享时的开场也用它）：

> AI has made writing code cheap. What comes after the code is as expensive as ever: knowing who, or which agent, made a change, building it on the hosts you actually have, showing where a release came from, and patching it for years. From December 2027 the EU Cyber Resilience Act turns part of that into a legal duty: a manufacturer selling software in the EU has to declare a support period and ship security updates until it ends.

> AI 让写代码变便宜了，代码写完之后的事一样没便宜：这次改动是谁、或者哪个 agent 提交的，在你手上那些机器上还能不能构建，发出去的版本说不说得清来历，往后几年出了漏洞谁来补。从 2027 年 12 月起，欧盟《网络弹性法案》把其中一部分写成了法律义务：在欧盟卖软件的厂商要声明支持期，并在支持期内持续提供安全更新。

各平台简介，可以直接粘贴：

| 平台 | 文案 |
| --- | --- |
| GitHub bio（160 字符以内） | Release engineer. Open-source tools that keep software shipping, from commit to release and long after. cpp-linter · commit-check · keelinfra |
| X bio（160 字符以内） | Release engineer. Open-source tools that keep software shipping, even after upstream moves on. commit → review → build → release → support |
| LinkedIn headline | Release engineer · Open-source tools that keep software shipping, even after upstream moves on · cpp-linter, commit-check, Conventional Branch, keelinfra |
| 公众号简介 | 2009 年入行，一直在做构建、测试和发布。写怎么把软件稳稳发出去，上游不管了又该怎么办。 |

五个阶段和各自的项目，X 简介和 LinkedIn About 里按这个顺序写：

| 阶段 | 项目 |
| --- | --- |
| commit | commit-check、Conventional Branch |
| review | cpp-linter |
| build | explain-error、jenkinsfilelint、Agent8 |
| release | release-ledger、clang-tools-static-binaries |
| support | Extended Security for Jenkins、MkDocs NG |

keelinfra 和 keelapps 面向同一群人（在公司里维护研发工具的团队），放在一起讲。Keelhaven 是业余项目，不放进这条线。

## 流水线图

`pipeline-*.png` 是上面五个阶段画成的图：标题、定位句、一条带五个点的线，每个点下面是阶段名和项目。
release 到 support 那一段是虚线，前面几段是几分钟的事，这一段是几年。用在 Slides、文章和公众号里，
这些地方图是按原宽显示的，小字看得清。

| File | Size | Intended use |
| --- | --- | --- |
| `pipeline-1600x900.png` | 1600×900 | 流水线图，深色，英文 |
| `pipeline-light-1600x900.png` | 1600×900 | 流水线图，浅色，英文 |
| `pipeline-zh-1600x900.png` | 1600×900 | 流水线图，深色，中文标题 |

## 横幅

"From commit to release." 横幅：一句标题，下面一条带四个点的线，代表 commit → review → build → release
四个阶段。横幅用短标题，不画第五个点：support 是“and long after”，在流水线图和文字里讲。图上不放阶段名和项目名：X、LinkedIn 在桌面上把图缩到原宽的一半左右，手机上缩到四分之一，
小字缩完都看不清。阶段和项目写在 X 简介和 LinkedIn About 里。GitHub 主页 README 不用图，
标题直接用文字，正文里五行就是那条线。

| 平台 | 原图宽 | 桌面显示宽 | 手机显示宽 | 标题在桌面 / 手机上的大小 |
| --- | --- | --- | --- | --- |
| X | 1500 | 约 600 | 约 390 | 42 / 27 px |
| LinkedIn | 1584 | 约 804 | 约 390 | 43 / 21 px |

配色和字体与博客 shenxianpeng.dev 的 Evergreen 设计系统一致
（`shenxianpeng/blog` 的 `assets/css/schemes/evergreen.css` 与 `DESIGN.md`）：
深色 `#111914` / 浅色 `#F2F3EF` 底，强调色 `#4FB88A` / `#1D6A4B`，Geist。

| File | Size | Intended use |
| --- | --- | --- |
| `x-1500x500.png` | 1500×500 | X 头图，深色，右对齐。左下角（x < 375、y > 333）留给头像 |
| `linkedin-1584x396.png` | 1584×396 | LinkedIn 背景图，深色，右对齐。左侧（x < 347）留给头像 |

横幅和流水线图都由 `gen_banners.py` 生成，改文案或项目后重跑即可：

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
