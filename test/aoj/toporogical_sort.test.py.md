---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: graph/toporogical_sort.py
    title: "\u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\u30C8"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/4/GRL_4_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/4/GRL_4_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/4/GRL_4_B\n\
    \nfrom graph.toporogical_sort import topological_sort\n\nN, M = map(int, input().split())\n\
    G = [[] for _ in range(N)]\ndeg = [0] * N\nfor _ in range(M):\n    u, v = map(int,\
    \ input().split())\n    G[u].append(v)\n    deg[v] += 1\n\nans = topological_sort(N,\
    \ G, deg)\nprint(*ans, sep=\"\\n\")\n"
  dependsOn:
  - graph/toporogical_sort.py
  isVerificationFile: true
  path: test/aoj/toporogical_sort.test.py
  requiredBy: []
  timestamp: '2023-08-10 00:04:04+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/aoj/toporogical_sort.test.py
layout: document
redirect_from:
- /verify/test/aoj/toporogical_sort.test.py
- /verify/test/aoj/toporogical_sort.test.py.html
title: test/aoj/toporogical_sort.test.py
---