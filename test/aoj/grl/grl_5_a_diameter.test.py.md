---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/tree/diameter.py
    title: "\u6728\u306E\u76F4\u5F84"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_A\n\
    \nfrom graph.tree.diameter import diameter\n\nN = int(input())\nG = [[] for _\
    \ in range(N)]\nfor _ in range(N - 1):\n    a, b, c = map(int, input().split())\n\
    \    G[a].append((b, c))\n    G[b].append((a, c))\n\ndiam = diameter(N, G)\nprint(diam)\n"
  dependsOn:
  - graph/tree/diameter.py
  isVerificationFile: true
  path: test/aoj/grl/grl_5_a_diameter.test.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_5_a_diameter.test.py
layout: document
title: "GRL5A \u6728\u306E\u76F4\u5F84"
---
