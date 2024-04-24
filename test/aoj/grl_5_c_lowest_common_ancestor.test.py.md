---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: tree/euler_tour.py
    title: Euler tour
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_C
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_C\n\
    \nfrom tree.euler_tour import EulerTour\n\nN = int(input())\nG = [[] for _ in\
    \ range(N)]\nfor i in range(N):\n    k, *es = map(int, input().split())\n    for\
    \ e in es:\n        G[i].append((e, 1))\n        G[e].append((i, 1))\n\net = EulerTour(G,\
    \ 0, [0] * N)\nQ = int(input())\nfor _ in range(Q):\n    u, v = map(int, input().split())\n\
    \    print(et.lca(u, v))\n"
  dependsOn:
  - tree/euler_tour.py
  isVerificationFile: true
  path: test/aoj/grl_5_c_lowest_common_ancestor.test.py
  requiredBy: []
  timestamp: '2024-04-24 11:17:49+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl_5_c_lowest_common_ancestor.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl_5_c_lowest_common_ancestor.test.py
- /verify/test/aoj/grl_5_c_lowest_common_ancestor.test.py.html
title: test/aoj/grl_5_c_lowest_common_ancestor.test.py
---
