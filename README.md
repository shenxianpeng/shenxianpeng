## Hi👋, I'm Xianpeng 

**I build open-source tools that make software delivery verifiable.**

Linting, commit and branch standards, and machine-readable evidence from commit to deploy — increasingly with AI in the loop: explaining CI failures, reviewing changes, and helping teams ship with proof instead of vibes.

[About][about] · [Blog][blog] · [RSS][rss] · [Medium][medium] · [Dev.to][dev.to] · [Zhihu][zhihu] · [WeChat][qrcode]

<a href="https://pypi.org/user/xpshen/"><img src="https://img.shields.io/badge/-PyPI-4B8BBE?style=flat&labelColor=306998&logo=pypi&logoColor=FFE873" alt="My PyPI packages" height="20"></a>
<a href="https://shenxianpeng.github.io/en/portfolio/pypistats/"><img src="https://img.shields.io/badge/-PyPI_Stats-4B8BBE?style=flat&labelColor=306998&logo=pypi&logoColor=FFE873" alt="My PyPI package stats" height="20"></a>
<a href="https://github.com/sponsors/shenxianpeng"><img src="https://img.shields.io/badge/GitHub-Sponsors-EA4AAA?style=flat&logo=githubsponsors" alt="Sponsor me on GitHub" height="20"></a>
<a href="https://user-badge.committers.top/lithuania_public/shenxianpeng"><img src="https://user-badge.committers.top/lithuania_public/shenxianpeng.svg" alt="Committers.top rank in Lithuania" height="20"></a>
<img src="https://komarev.com/ghpvc/?username=shenxianpeng&style=flat&color=blue" alt="Profile views" height="20">

---

### ⭐ Start here

#### [cpp-linter-action][cpp-linter-action] [![stars](https://img.shields.io/github/stars/cpp-linter/cpp-linter-action?style=social&label=)][cpp-linter-action]

clang-format & clang-tidy on every pull request, posted back as inline review comments.

```yaml
- uses: cpp-linter/cpp-linter-action@v2
  with:
    style: file
```

#### [commit-check][commit-check] [![stars](https://img.shields.io/github/stars/commit-check/commit-check?style=social&label=)][commit-check]

Enforce commit message, branch naming, and AI-attribution rules — in CI or as a pre-commit hook.

```yaml
- repo: https://github.com/commit-check/commit-check
  rev: v2.13.1
  hooks:
    - id: check-message
    - id: check-branch
```

#### [Conventional Branch][conventional-branch] [![stars](https://img.shields.io/github/stars/conventional-branch/conventional-branch?style=social&label=)][conventional-branch]

A naming specification for Git branches — `feature/`, `bugfix/`, `hotfix/`, `release/`, `chore/`, plus prefixes for AI coding agents. Lives at **[conventionalbranch.org](https://conventionalbranch.org)**.

---

### 🏛️ What I'm building now — [Open Delivery Spec][ods]

Standardized, machine-parseable schemas for software delivery governance: what was built, tested, reviewed, and deployed — as evidence a machine can check, at every commit-to-deploy stage.

📜 [spec][ods-spec] · 🔧 [cli][ods-cli] · ✅ [validate-action][ods-validate-action]

---

### 📦 Everything else

| Focus | Projects |
| --- | --- |
| **Code quality & standards** | [cpp-linter-hooks][cpp-linter-hooks] (clang-tidy/format for pre-commit) · [jenkinsfilelint][jenkinsfilelint] (validate Jenkinsfiles locally) · [hadolint-pre-commit][hadolint-pre-commit] (Dockerfile linting) |
| **CI/CD intelligence** | [explain-error-plugin][explain-error-plugin] (AI diagnosis of Jenkins failures) · [pipguard][pipguard] (dependency supply-chain safety) · [py-eol][py-eol] (Python EOL awareness) |
| **Workflows & insights** | [gitstats][gitstats] (git history statistics) · [devops-maturity][devops-maturity] (engineering maturity assessment) · [atlassian-api-py][atlassian-api-py] (Atlassian REST wrapper) · [badgepy][badgepy] (local SVG badge generator) |

---

### 👥 Community

- Contributor to [**Python**][python] ([merged PRs][python-prs]) and [**PyPA**][pypa] ([merged PRs][pypa-prs]).
- Maintainer and contributor in the [**Jenkins**][jenkinsci] ecosystem — [explain-error-plugin][explain-error-plugin] and [jenkinsfilelint][jenkinsfilelint].
- Maintainer of [**mkdocs-ng/mkdocs**][mkdocs] and [**mkdocs-ng/mkdocs-material**][mkdocs-material].

---

### ✍️ Writing

<!-- BLOG-POST-LIST:START -->
- [mkdocs-ng v1.8.0 Released — Upstream Issues Fixed, Builds ~14% Faster](https://shenxianpeng.github.io/en/posts/2026/mkdocs-ng-1.8/) - Aug 13, 2026
- [Open Delivery Spec update: AI code shouldn&#39;t just pass the gate — it should leave evidence](https://shenxianpeng.github.io/en/posts/2026/open-delivery-spec-update/) - Aug 8, 2026
- [From Praising to Bashing—My Attitude Shift Towards GitHub Copilot](https://shenxianpeng.github.io/en/posts/2026/goodbye-copilot/) - Jul 20, 2026
- [Open Delivery Spec—I Built a CI Quality Gate for AI-Generated Code](https://shenxianpeng.github.io/en/posts/2026/open-delivery-spec/) - Jul 17, 2026
- [Conventional Branch 1.1.0 Released—Official Support for AI Coding Agent Branch Prefixes](https://shenxianpeng.github.io/en/posts/2026/conventional-branch-v1-1-0/) - Jul 16, 2026<!-- BLOG-POST-LIST:END -->

→ **[More on my blog][blog]**, or follow on WeChat **[shenxianpeng][qrcode]** for AI + DevOps notes in Chinese.

[about]: https://shenxianpeng.github.io/en/about/
[blog]: https://shenxianpeng.github.io/en/posts/
[rss]: https://shenxianpeng.github.io/index.xml
[medium]: https://medium.com/@xianpeng.shen
[dev.to]: https://dev.to/shenxianpeng
[zhihu]: https://www.zhihu.com/people/shenxianpeng
[qrcode]: https://github.com/shenxianpeng/blog/blob/main/assets/img/qrcode.jpg
[cpp-linter-action]: https://github.com/cpp-linter/cpp-linter-action
[cpp-linter-hooks]: https://github.com/cpp-linter/cpp-linter-hooks
[commit-check]: https://github.com/commit-check/commit-check
[conventional-branch]: https://github.com/conventional-branch/conventional-branch
[devops-maturity]: https://github.com/devops-maturity/devops-maturity
[explain-error-plugin]: https://github.com/jenkinsci/explain-error-plugin
[jenkinsfilelint]: https://github.com/jenkinsci/jenkinsfilelint
[gitstats]: https://github.com/shenxianpeng/gitstats
[badgepy]: https://github.com/shenxianpeng/badgepy
[mkdocs]: https://github.com/mkdocs-ng/mkdocs
[mkdocs-material]: https://github.com/mkdocs-ng/mkdocs-material
[atlassian-api-py]: https://github.com/shenxianpeng/atlassian-api-py
[hadolint-pre-commit]: https://github.com/shenxianpeng/hadolint-pre-commit
[py-eol]: https://github.com/shenxianpeng/py-eol
[pipguard]: https://github.com/shenxianpeng/pipguard
[jenkinsci]: https://github.com/jenkinsci
[pypa]: https://github.com/pypa
[python]: https://github.com/python
[pypa-prs]: https://github.com/pulls/search?q=is%3Apr+author%3Ashenxianpeng+archived%3Afalse+is%3Amerged+user%3Apypa
[python-prs]: https://github.com/pulls/search?q=is%3Apr+author%3Ashenxianpeng+archived%3Afalse+is%3Amerged+user%3Apython
[ods]: https://github.com/open-delivery-spec
[ods-spec]: https://github.com/open-delivery-spec/spec
[ods-cli]: https://github.com/open-delivery-spec/cli
[ods-validate-action]: https://github.com/open-delivery-spec/validate-action
