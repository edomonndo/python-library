---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: graph/low_link.py
    title: "\u9593\u63A5\u70B9\uFF0C\u6A4B"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_A\n\
    \nfrom graph.low_link import LowLink\n\nn, m = map(int, input().split())\ng =\
    \ [[] for _ in range(n)]\nfor _ in range(m):\n    u, v = map(int, input().split())\n\
    \    g[u].append(v)\n    g[v].append(u)\n\nLL = LowLink(g)\narticulation = LL.get_articulation()\n\
    ans = [i for i, v in articulation if v]\nif ans:\n    print(*ans, sep=\"\\n\"\
    )\n"
  dependsOn:
  - graph/low_link.py
  isVerificationFile: true
  path: test/aoj/grl_3_a_articulation_points.test.py
  requiredBy: []
  timestamp: '2024-06-12 09:49:37+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/aoj/grl_3_a_articulation_points.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl_3_a_articulation_points.test.py
- /verify/test/aoj/grl_3_a_articulation_points.test.py.html
title: test/aoj/grl_3_a_articulation_points.test.py
---
