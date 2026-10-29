<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/brand/github-dark-1920x320.png">
  <source media="(prefers-color-scheme: light)" srcset="assets/brand/github-light-1920x320.png">
  <img alt="From commit to release." src="assets/brand/github-light-1920x320.png">
</picture>

I build open-source guardrails for software delivery: the checks between a commit and a release, whether a person or an AI agent wrote the code.

[Blog][blog] · [About][about] · [X][x] · [LinkedIn][linkedin] · [RSS][rss] · [Sponsor][sponsors]

## Open source

`commit` &nbsp;[**commit-check**][commit-check]: checks commit messages, branch names and AI attribution, in CI or as a pre-commit hook. About 55,000 downloads a month.

`review` &nbsp;[**cpp-linter**][cpp-linter]: runs clang-format and clang-tidy on every pull request. More than 1,000 repositories depend on it, including projects from:

<p>
  <a href="https://github.com/apache/orc"><img src="https://github.com/apache.png?size=56" alt="" width="24" align="top"></a> <b>Apache</b>&nbsp;&nbsp;
  <a href="https://github.com/Samsung/mTower"><img src="https://github.com/Samsung.png?size=56" alt="" width="24" align="top"></a> <b>Samsung</b>&nbsp;&nbsp;
  <a href="https://github.com/qualcomm/eld"><img src="https://github.com/qualcomm.png?size=56" alt="" width="24" align="top"></a> <b>Qualcomm</b>&nbsp;&nbsp;
  <a href="https://github.com/bloomberg/blazingmq"><img src="https://github.com/bloomberg.png?size=56" alt="" width="24" align="top"></a> <b>Bloomberg</b>&nbsp;&nbsp;
  <a href="https://github.com/llnl/AMS"><img src="https://github.com/LLNL.png?size=56" alt="" width="24" align="top"></a> <b>LLNL</b>&nbsp;&nbsp;
  <a href="https://github.com/stanford-ssi/samwise-flight-software"><img src="https://github.com/stanford-ssi.png?size=56" alt="" width="24" align="top"></a> <b>Stanford SSI</b>&nbsp;&nbsp;
  <a href="https://github.com/nextcloud/desktop"><img src="https://github.com/nextcloud.png?size=56" alt="" width="24" align="top"></a> <b>Nextcloud</b>
</p>

`build` &nbsp;[**explain-error**][explain-error-plugin]: explains failed Jenkins builds with AI. [**Agent8**][agent8] keeps Java 8 build hosts (AIX, Solaris, HP-UX) on a current Jenkins.

`release` &nbsp;[**release-ledger**][release-ledger]: attaches an SBOM, signs provenance and checks every supported version against known exploited vulnerabilities.

Also: [Conventional Branch][conventional-branch] · [gitstats][gitstats] · [Keelhaven][keelhaven] · [mkdocs-ng][mkdocs] · merged PRs in [Python][python-prs] and [PyPA][pypa-prs]

## Writing

<!-- BLOG-POST-LIST:START -->
- [After OVHcloud&#39;s Release Was Swapped: Three in Four Popular CLIs Could Be Too](https://shenxianpeng.dev/posts/2026/swappable-github-releases/) - Oct 24, 2026
- [Jira Is Moving to the Cloud. What Happens to Jenkins and Bitbucket?](https://shenxianpeng.dev/posts/2026/jira-cloud-jenkins-bitbucket/) - Oct 24, 2026
- [Open-Source AI Attribution Index, 2026 Q3: Only 13.2% of Commits Disclose AI, and That Is Too Low](https://shenxianpeng.dev/posts/2026/ai-coding-index-q3/) - Oct 24, 2026<!-- BLOG-POST-LIST:END -->

More [on the blog][blog]. 中文读者请关注公众号「[沈显鹏][qrcode]」。

[about]: https://shenxianpeng.dev/about/
[blog]: https://shenxianpeng.dev/posts/
[rss]: https://shenxianpeng.dev/index.xml
[x]: https://x.com/xianpengshen
[linkedin]: https://www.linkedin.com/in/xianpeng-shen/
[qrcode]: https://github.com/shenxianpeng/blog/blob/main/assets/img/qrcode.jpg
[sponsors]: https://github.com/sponsors/shenxianpeng
[commit-check]: https://github.com/commit-check/commit-check
[conventional-branch]: https://conventionalbranch.org
[cpp-linter]: https://github.com/cpp-linter
[explain-error-plugin]: https://github.com/jenkinsci/explain-error-plugin
[agent8]: https://github.com/keelinfra/agent8
[release-ledger]: https://github.com/keelinfra/release-ledger
[gitstats]: https://github.com/shenxianpeng/gitstats
[mkdocs]: https://github.com/mkdocs-ng/mkdocs
[python-prs]: https://github.com/search?q=is%3Apr+author%3Ashenxianpeng+is%3Amerged+user%3Apython&type=pullrequests
[pypa-prs]: https://github.com/search?q=is%3Apr+author%3Ashenxianpeng+is%3Amerged+user%3Apypa&type=pullrequests
[keelhaven]: https://github.com/shenxianpeng/keelhaven
