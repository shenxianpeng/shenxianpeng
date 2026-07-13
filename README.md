### Hi, I'm Xianpeng 👋

![Profile Views](https://komarev.com/ghpvc/?username=shenxianpeng)
[![My PyPI packages](https://img.shields.io/badge/-PyPI-4B8BBE?style=flat&labelColor=306998&logo=pypi&logoColor=FFE873 "My PyPI packages")](https://pypi.org/user/xpshen/)
[![My PyPI packages stats](https://img.shields.io/badge/-PyPI_Stats-4B8BBE?style=flat&labelColor=306998&logo=pypi&logoColor=FFE873 "My PyPI packages stats")][pypistats]
[![Sponsor me on GitHub](https://img.shields.io/badge/GitHub-Sponsors-EA4AAA?style=flat&logo=githubsponsors "Sponsor me on GitHub")][sponsor]
[![committers.top badge](https://user-badge.committers.top/lithuania_public/shenxianpeng.svg)](https://user-badge.committers.top/lithuania_public/shenxianpeng)

[About](https://shenxianpeng.github.io/en/about/) | [Blog][blog] | [RSS][rss] | [Medium][medium] | [Dev.to][dev.to] | [WeChat][qrcode] | [Zhihu][zhihu]

---

I build open-source tools for **DevOps, CI/CD, and software delivery**, collected under the **Open Delivery Stack (ODS)** vision — a machine-readable layer for how software gets governed, tested, and shipped. AI is increasingly part of this: explaining failures, reviewing changes, and helping teams ship with evidence.

#### 📦 What I Build

| Focus | What it does | Projects |
| --- | --- | --- |
| 🏛️ **Delivery Governance** | Machine-readable evidence at every commit-to-deploy stage | 📜 [spec][ods-spec] · 🔧 [cli][ods-cli] · ✅ [validate-action][ods-validate-action] |
| 📏 **Code Quality & Standards** | Catch C/C++, Dockerfile & Jenkinsfile issues early; enforce commit & branch conventions | 🔍 [cpp-linter-action][cpp-linter-action] · 🪝 [cpp-linter-hooks][cpp-linter-hooks] · ✅ [commit-check][commit-check] · 🌿 [conventional-branch][conventional-branch] · 🏗️ [jenkinsfilelint][jenkinsci/jenkinsfilelint] · 🐳 [hadolint][hadolint-pre-commit] |
| 🧠 **CI/CD Intelligence** | AI failure diagnosis, dependency safety & Python EOL awareness | 🤖 [explain-error-plugin][explain-error-plugin] · 🛡️ [pipguard][pipguard] · ⏰ [py-eol][py-eol] |
| 🧰 **Workflows & Insights** | Platform tooling, API integrations & engineering maturity metrics | 🔗 [atlassian-api-py][atlassian-api-py] · 📊 [gitstats][gitstats] · 📈 [devops-maturity][devops-maturity] |

#### 👥 Community

- Maintainer and contributor in the [**Jenkins**][jenkinsci] ecosystem, including [jenkinsci/explain-error-plugin][explain-error-plugin] and [jenkinsci/jenkinsfilelint][jenkinsfilelint].
- Contributor to [**PyPA**][pypa] ([merged PRs][pypa-prs]) and [**Python**][python] ([merged PRs][python-prs]).
- Maintainer of [**mkdocs-ng/mkdocs**][mkdocs], [**mkdocs-ng/mkdocs-material**][mkdocs-material], and [**badgepy**][badgepy].

---

**WeChat:** [**shenxianpeng**][qrcode] - sharing AI + DevOps practices and real-world engineering notes.

---

#### ✍️ Writing

<!-- BLOG-POST-LIST:START -->
- [Jenkinsfile Lint 1.5.0 Released— Standalone Mode Without a Jenkins Server](https://shenxianpeng.github.io/en/posts/2026/jenkinsfilelint-standalone/) - Jul 12, 2026
- [Which Code in Your Repository is AI-Written—Now There&#39;s a Tool to Govern It](https://shenxianpeng.github.io/en/posts/2026/commit-check-ai-attribution/) - Jul 6, 2026
- [Originally Just Wanted to Propose a Doc PR, Ended Up Moving the Project to the Official Jenkins Organization](https://shenxianpeng.github.io/en/posts/2026/jenkinsfilelint/) - Jun 9, 2026
- [From Demo to Production—8-Layer Architecture for Agentic Applications](https://shenxianpeng.github.io/en/posts/2026/agentic-application-8-layers/) - Jun 8, 2026
- [Conventional Branch Now Has Its Own Domain—conventionalbranch.org](https://shenxianpeng.github.io/en/posts/2026/conventional-branch-domain/) - May 31, 2026
- [cpp-linter-hooks: The Most Complete pre-commit Solution for C/C++ Projects](https://shenxianpeng.github.io/en/posts/2026/cpp-linter-hooks/) - May 20, 2026
- [Conventional Branch Official Skill Is Here—Install with One Command](https://shenxianpeng.github.io/en/posts/2026/conventional-branch-skill/) - May 17, 2026
- [mkdocs-ng Maintenance Progress — v1.7.x Fix Summary and Next Steps](https://shenxianpeng.github.io/en/posts/2026/mkdocs-ng-update/) - May 14, 2026
- [Building an AI Agent Inside Jira —— A Jira Copilot Implementation Guide](https://shenxianpeng.github.io/en/posts/2026/jira-ai-agent/) - May 12, 2026
- [Counter-intuitive Designs in the pi project — From AGENTS.md to &quot;Just Close Your PR First&quot;](https://shenxianpeng.github.io/en/posts/2026/pi-contributing-philosophy/) - Apr 26, 2026<!-- BLOG-POST-LIST:END -->


[blog]: https://shenxianpeng.github.io/en/posts/
[rss]: https://shenxianpeng.github.io/index.xml
[medium]: https://medium.com/@xianpeng.shen
[dev.to]: https://dev.to/shenxianpeng
[zhihu]: https://www.zhihu.com/people/shenxianpeng
[qrcode]: https://github.com/shenxianpeng/blog/blob/main/assets/img/qrcode.jpg
[sponsor]: https://github.com/sponsors/shenxianpeng
[cpp-linter-org]: https://github.com/cpp-linter
[cpp-linter-action]: https://github.com/cpp-linter/cpp-linter-action
[cpp-linter-hooks]: https://github.com/cpp-linter/cpp-linter-hooks
[clang-tools-static-binaries]: https://github.com/cpp-linter/clang-tools-static-binaries
[clang-tools-docker]: https://github.com/cpp-linter/clang-tools-docker
[clang-tools-wheel]: https://github.com/cpp-linter/clang-tools-wheel
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
[jenkinsci/jenkinsfilelint]: https://github.com/jenkinsci/jenkinsfilelint
[pipguard]: https://github.com/shenxianpeng/pipguard
[repokeeper]: https://github.com/shenxianpeng/repokeeper
[jenkinsci]: https://github.com/jenkinsci
[pypa]: https://github.com/pypa
[python]: https://github.com/python
[pypa-prs]: https://github.com/pulls/search?q=is%3Apr+author%3Ashenxianpeng+archived%3Afalse+is%3Amerged+user%3Apypa
[python-prs]: https://github.com/pulls/search?q=is%3Apr+author%3Ashenxianpeng+archived%3Afalse+is%3Amerged+user%3Apython
[pypistats]: https://shenxianpeng.github.io/en/portfolio/pypistats/
[ods]: https://github.com/open-delivery-spec
[ods-spec]: https://github.com/open-delivery-spec/spec
[ods-cli]: https://github.com/open-delivery-spec/cli
[ods-validate-action]: https://github.com/open-delivery-spec/validate-action
