---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: graph/directed_mst.py
    title: graph/directed_mst.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/directedmst
    links:
    - https://judge.yosupo.jp/problem/directedmst
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/directedmst\n\
    \n\nfrom graph.directed_mst import directed_mst\n\nn, m, r = map(int, input().split())\n\
    edges = [tuple(map(int, input().split())) for _ in range(m)]\neis = directed_mst(n,\
    \ edges, r)\nassert eis\n\ncost = 0\npar = [-1] * n\nfor ei in eis:\n    u, v,\
    \ w = edges[ei]\n    cost += w\n    par[v] = u\npar[r] = r\nprint(cost)\nprint(*par)\n"
  dependsOn:
  - graph/directed_mst.py
  isVerificationFile: true
  path: test/library_checker/graph/directed_mst.test.py
  requiredBy: []
  timestamp: '2024-08-20 10:54:57+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/graph/directed_mst.test.py
layout: document
title: Directed MST
---

