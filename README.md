# From commit to release, and long after.

Release engineer. Open-source tools that keep software shipping, whether a person or an AI agent wrote the code, even after upstream moves on.

[Blog][blog] · [About][about] · [LinkedIn][linkedin] · [RSS][rss]

<a href="https://committers.top/lithuania_public"><img src="https://user-badge.committers.top/lithuania_public/shenxianpeng.svg" alt="committers.top rank: Lithuania #3, public contributions" height="20"></a>
<a href="https://x.com/xianpengshen"><img src="https://img.shields.io/badge/follow-@xianpengshen-1D6A4B?style=flat&logo=x&logoColor=white&labelColor=24292f" alt="Follow @xianpengshen on X" height="20"></a>
<a href="https://github.com/sponsors/shenxianpeng"><img src="https://img.shields.io/badge/GitHub-Sponsors-EA4AAA?style=flat&logo=githubsponsors" alt="Sponsor me on GitHub" height="20"></a>
<a href="https://pypi.org/user/xpshen/"><img src="https://img.shields.io/badge/-PyPI-4B8BBE?style=flat&labelColor=306998&logo=pypi&logoColor=FFE873" alt="My PyPI packages" height="20"></a>
<a href="https://shenxianpeng.dev/portfolio/pypistats/"><img src="https://img.shields.io/badge/-PyPI_Stats-4B8BBE?style=flat&labelColor=306998&logo=pypi&logoColor=FFE873" alt="My PyPI package stats" height="20"></a>

## Open source

`commit` &nbsp;[**commit-check**][commit-check]: checks commit messages, branch names and AI attribution, in CI or as a pre-commit hook. About 55,000 downloads a month.

`review` &nbsp;[**cpp-linter**][cpp-linter]: runs clang-format and clang-tidy on every pull request. More than 1,000 repositories depend on it, including projects from:

<p>
  <a href="https://github.com/aws/s2n-tls"><img src="https://github.com/aws.png?size=56" alt="" width="24" align="top"></a> <b>AWS</b>&nbsp;&nbsp;
  <a href="https://github.com/apache/orc"><img src="https://github.com/apache.png?size=56" alt="" width="24" align="top"></a> <b>Apache</b>&nbsp;&nbsp;
  <a href="https://github.com/Samsung/mTower"><img src="https://github.com/Samsung.png?size=56" alt="" width="24" align="top"></a> <b>Samsung</b>&nbsp;&nbsp;
  <a href="https://github.com/qualcomm/eld"><img src="https://github.com/qualcomm.png?size=56" alt="" width="24" align="top"></a> <b>Qualcomm</b>&nbsp;&nbsp;
  <a href="https://github.com/bloomberg/blazingmq"><img src="https://github.com/bloomberg.png?size=56" alt="" width="24" align="top"></a> <b>Bloomberg</b>&nbsp;&nbsp;
  <a href="https://github.com/llnl/AMS"><img src="https://github.com/LLNL.png?size=56" alt="" width="24" align="top"></a> <b>LLNL</b>&nbsp;&nbsp;
  <a href="https://github.com/nextcloud/desktop"><img src="https://github.com/nextcloud.png?size=56" alt="" width="24" align="top"></a> <b>Nextcloud</b>
</p>

`build` &nbsp;[**explain-error**][explain-error-plugin]: explains failed Jenkins builds with AI. [**Agent8**][agent8] keeps Java 8 build hosts (AIX, Solaris, HP-UX) on a current Jenkins.

`release` &nbsp;[**clang-tools-static-binaries**][clang-tools]: builds and publishes static clang-format, clang-tidy and other LLVM tools for every LLVM version, so nobody has to build LLVM. Downloaded more than 750,000 times.

`support` &nbsp;[**Extended Security for Jenkins**][jenkins-es]: Jenkins 2.541.3, the last LTS that runs on Java 17, with the core security fixes released after it. [**MkDocs NG**][mkdocs] keeps MkDocs 1.x sites and their plugins building, with 1.x supported until the end of 2028.

Also: [Conventional Branch][conventional-branch] · [gitstats][gitstats] · [Keelhaven][keelhaven] · [release-ledger][release-ledger] · merged PRs in [Python][python-prs] and [PyPA][pypa-prs]

## Writing

<!-- BLOG-POST-LIST:START -->
- [pybadges Fails on Python 3.13: How to Fix &quot;No module named &#39;imghdr&#39;&quot;](https://shenxianpeng.dev/posts/2026/pybadges-imghdr/) - Nov 6, 2026
- [Six Months of Maintaining MkDocs NG: Why I Keep Going](https://shenxianpeng.dev/posts/2026/mkdocs-ng-1.11/) - Nov 4, 2026
- [After OVHcloud&#39;s Release Was Swapped: Three in Four Popular CLIs Could Be Too](https://shenxianpeng.dev/posts/2026/swappable-github-releases/) - Oct 24, 2026<!-- BLOG-POST-LIST:END -->

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
[jenkins-es]: https://github.com/keelinfra/jenkins-extended-security
[release-ledger]: https://github.com/keelinfra/release-ledger
[clang-tools]: https://github.com/cpp-linter/clang-tools-static-binaries
[gitstats]: https://github.com/shenxianpeng/gitstats
[mkdocs]: https://github.com/mkdocs-ng/mkdocs
[python-prs]: https://github.com/search?q=is%3Apr+author%3Ashenxianpeng+is%3Amerged+user%3Apython&type=pullrequests
[pypa-prs]: https://github.com/search?q=is%3Apr+author%3Ashenxianpeng+is%3Amerged+user%3Apypa&type=pullrequests
[keelhaven]: https://github.com/shenxianpeng/keelhaven
