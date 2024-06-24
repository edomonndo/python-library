---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: tree/centroid_decomposition.py
    title: "\u91CD\u5FC3\u5206\u89E3"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/abc291/tasks/abc291_h
    links:
    - https://atcoder.jp/contests/abc291/tasks/abc291_h
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc291/tasks/abc291_h\n\
    \n\nfrom tree.centroid_decomposition import CentroidDecomposition\n\nn = int(input())\n\
    g = [[] for _ in range(n)]\nfor _ in range(n - 1):\n    u, v = map(lambda x: int(x)\
    \ - 1, input().split())\n    g[u].append(v)\n    g[v].append(u)\n\ntree = CentroidDecomposition(g)\n\
    print(*[v + 1 if v >= 0 else v for v in tree.belong])\n"
  dependsOn:
  - tree/centroid_decomposition.py
  isVerificationFile: true
  path: test/atcoder/abc200-299/abc291h.test.py
  requiredBy: []
  timestamp: '2024-06-24 17:00:04+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/atcoder/abc200-299/abc291h.test.py
layout: document
title: H - Balanced Tree
---
