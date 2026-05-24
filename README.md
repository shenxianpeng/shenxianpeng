### Hi, I'm Xianpeng

![Profile Views](https://komarev.com/ghpvc/?username=shenxianpeng)
[![My PyPI packages](https://img.shields.io/badge/-PyPI-4B8BBE?style=flat&labelColor=306998&logo=pypi&logoColor=FFE873 "My PyPI packages")](https://pypi.org/user/xpshen/)
[![My PyPI packages stats](https://img.shields.io/badge/-PyPI_Stats-4B8BBE?style=flat&labelColor=306998&logo=pypi&logoColor=FFE873 "My PyPI packages stats")][pypistats]
[![Sponsor me on GitHub](https://img.shields.io/badge/GitHub-Sponsors-EA4AAA?style=flat&logo=githubsponsors "Sponsor me on GitHub")][sponsor]
[![committers.top badge](https://user-badge.committers.top/lithuania_public/shenxianpeng.svg)](https://user-badge.committers.top/lithuania_public/shenxianpeng)

[About](https://shenxianpeng.github.io/en/about/) | [Blog][blog] | [RSS][rss] | [Medium][medium] | [Dev.to][dev.to] | [WeChat][qrcode] | [Zhihu][zhihu]

---

I build open-source tools for **AI-assisted software delivery**: standards, code quality, CI feedback, supply-chain safety, failure diagnosis, and maintainer automation.

Most of my projects are connected by one idea: help teams move from "we have many tools" to "we have an engineering system that guides, checks, explains, and improves itself."

#### The Solution Map

| Stage | Problem | Projects |
| --- | --- | --- |
| Define engineering standards | Teams need consistent branch names, commit metadata, and contribution signals before work enters CI. | [conventional-branch][conventional-branch], [commit-check][commit-check], [commit-check-action][commit-check-action], [commit-check-app][commit-check-app], [commit-check-mcp][commit-check-mcp] |
| Shift quality left | Developers should catch formatting, static analysis, Dockerfile, and Jenkinsfile issues before review. | [cpp-linter][cpp-linter], [cpp-linter-hooks][cpp-linter-hooks], [cpp-linter-action][cpp-linter-action], [jenkinsfilelint][jenkinsfilelint], [hadolint-pre-commit][hadolint-pre-commit] |
| Secure and sustain dependencies | Supply-chain and runtime-version risks should be visible before they become production problems. | [pipguard][pipguard], [py-eol][py-eol], [gnuplot-wheel][gnuplot-wheel] |
| Understand engineering systems | Teams need readable signals about repository health, delivery maturity, and generated quality reports. | [gitstats][gitstats], [badgepy][badgepy], [devops-maturity][devops-maturity] |
| Diagnose CI/CD failures with AI | Build failures should come with context, likely causes, and next actions instead of raw logs only. | [jenkinsci/explain-error-plugin][explain-error-plugin] |
| Automate OSS maintenance | Maintainers need agents that can triage, reason, patch, and keep repositories moving. | [repokeeper][repokeeper], [aion][aion], [atop][atop] |
| Standardize team workflows | Platform work should turn one engineer's operational standards into repeatable team pipelines. | [castops/cast-cli][cast-cli], [castops/cast-slice][cast-slice], [atlassian-api-py][atlassian-api-py] |

#### Featured Systems

- [**cpp-linter**][cpp-linter] turns clang-format and clang-tidy into reusable developer workflows across CLI, GitHub Actions, pre-commit hooks, containers, and installable clang tools.
- [**commit-check**][commit-check] and [**conventional-branch**][conventional-branch] make repository metadata enforceable, from local conventions to GitHub Actions, Apps, and MCP integrations.
- [**Explain Error Plugin**][explain-error-plugin] brings AI failure explanation and auto-fix workflows into Jenkins, with support for multiple AI providers.
- [**pipguard**][pipguard] blocks risky Python package installation paths before supply-chain attacks land.
- [**repokeeper**][repokeeper] explores an AI-powered maintainer loop: read issues, reason about code, open pull requests, and keep OSS projects alive.
- [**gitstats**][gitstats], [**badgepy**][badgepy], and [**devops-maturity**][devops-maturity] convert engineering activity into reports, badges, and maturity signals that teams can act on.

#### Community and Stewardship

- Member and contributor in the [**Jenkins**][jenkinsci] ecosystem, including [AI-powered Jenkins failure diagnosis][explain-error-plugin].
- Contributor to [**PyPA**][pypa] and [**Python**][python] with [merged PRs][python-prs].
- Maintainer of [**mkdocs-ng/mkdocs**][mkdocs] and [**mkdocs-ng/mkdocs-material**][mkdocs-material].
- Maintainer of developer productivity projects such as [**gitstats**][gitstats] and [**badgepy**][badgepy].

---

**WeChat:** [**shenxianpeng**][qrcode] - sharing AI + DevOps practices and real-world engineering notes.

---

#### Writing

<!-- BLOG-POST-LIST:START -->
- [cpp-linter-hooks: The Most Complete pre-commit Solution for C/C++ Projects](https://shenxianpeng.github.io/en/posts/2026/cpp-linter-hooks/)
- [Conventional Branch Official Skill Is Here—Install with One Command](https://shenxianpeng.github.io/en/posts/2026/conventional-branch-skill/)
- [mkdocs-ng Maintenance Progress — v1.7.x Fix Summary and Next Steps](https://shenxianpeng.github.io/en/posts/2026/mkdocs-ng-update/)
- [Building an AI Agent Inside Jira —— A Jira Copilot Implementation Guide](https://shenxianpeng.github.io/en/posts/2026/jira-ai-agent/)
- [Counter-intuitive Designs in the pi project — From AGENTS.md to &quot;Just Close Your PR First&quot;](https://shenxianpeng.github.io/en/posts/2026/pi-contributing-philosophy/)
- [Explain Error Plugin Major Update — AI Auto-Fix, Usage Management, and More AI Providers](https://shenxianpeng.github.io/en/posts/2026/explain-error-plugin-3/)
- [Writing an Article for Twenty-Four Cents—My Experience Using Pi + DeepSeek as a Codex Backup Solution](https://shenxianpeng.github.io/en/posts/2026/pi-deepseek/)
- [AI Agent, or Automation?](https://shenxianpeng.github.io/en/posts/2026/ai-agents-vs-automations/)
- [Python Supply Chain &#39;Nuclear Bomb&#39; Attack Just Happened—A `pip install` Steals All Your Credentials!](https://shenxianpeng.github.io/en/posts/2026/pipguard/)
- [A Three-Year Community Pain Point—I Put Hadolint on PyPI, Ending Manual Installation](https://shenxianpeng.github.io/en/posts/2026/hadolint-pre-commit/)
<!-- BLOG-POST-LIST:END -->


[blog]: https://shenxianpeng.github.io/en/posts/
[rss]: https://shenxianpeng.github.io/index.xml
[medium]: https://medium.com/@xianpeng.shen
[dev.to]: https://dev.to/shenxianpeng
[zhihu]: https://www.zhihu.com/people/shenxianpeng
[qrcode]: https://github.com/shenxianpeng/blog/blob/main/assets/img/qrcode.jpg
[sponsor]: https://github.com/sponsors/shenxianpeng
[cpp-linter]: https://github.com/cpp-linter/cpp-linter
[cpp-linter-action]: https://github.com/cpp-linter/cpp-linter-action
[cpp-linter-hooks]: https://github.com/cpp-linter/cpp-linter-hooks
[commit-check]: https://github.com/commit-check/commit-check
[commit-check-action]: https://github.com/commit-check/commit-check-action
[commit-check-app]: https://github.com/commit-check/commit-check-app
[commit-check-mcp]: https://github.com/commit-check/commit-check-mcp
[conventional-branch]: https://github.com/conventional-branch/conventional-branch
[devops-maturity]: https://github.com/devops-maturity/devops-maturity
[explain-error-plugin]: https://github.com/jenkinsci/explain-error-plugin
[gitstats]: https://github.com/shenxianpeng/gitstats
[badgepy]: https://github.com/shenxianpeng/badgepy
[mkdocs]: https://github.com/mkdocs-ng/mkdocs
[mkdocs-material]: https://github.com/mkdocs-ng/mkdocs-material
[cast-cli]: https://github.com/castops/cast-cli
[cast-slice]: https://github.com/castops/cast-slice
[atlassian-api-py]: https://github.com/shenxianpeng/atlassian-api-py
[hadolint-pre-commit]: https://github.com/shenxianpeng/hadolint-pre-commit
[py-eol]: https://github.com/shenxianpeng/py-eol
[gnuplot-wheel]: https://github.com/shenxianpeng/gnuplot-wheel
[jenkinsfilelint]: https://github.com/shenxianpeng/jenkinsfilelint
[pipguard]: https://github.com/shenxianpeng/pipguard
[repokeeper]: https://github.com/shenxianpeng/repokeeper
[aion]: https://github.com/shenxianpeng/aion
[atop]: https://github.com/shenxianpeng/atop
[jenkinsci]: https://github.com/jenkinsci
[pypa]: https://github.com/pypa
[python]: https://github.com/python
[python-prs]: https://github.com/pulls?q=is%3Apr+author%3Ashenxianpeng+archived%3Afalse+is%3Amerged+user%3Apypa+user%3Apython
[pypistats]: https://shenxianpeng.github.io/en/portfolio/pypistats/
