---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/enumerate_cliques.py
    title: graph/enumerate_cliques.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/enumerate_cliques
    links:
    - https://judge.yosupo.jp/problem/enumerate_cliques
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/enumerate_cliques\n\
    \nfrom graph.enumerate_cliques import enumerate_cliques\n\n\nMOD = 998244353\n\
    \n\ndef calc(vs: list[int]) -> int:\n    res = 1\n    for v in vs:\n        res\
    \ = (res * X[v]) % MOD\n    return res\n\n\ndef merge(x: int, y: int) -> int:\n\
    \    return (x + y) % MOD\n\n\nn, m = map(int, input().split())\nX = [int(x) for\
    \ x in input().split()]\nedges = [tuple(map(int, input().split())) for _ in range(m)]\n\
    print(enumerate_cliques(n, edges, calc, merge, 0))\n"
  dependsOn:
  - graph/enumerate_cliques.py
  isVerificationFile: true
  path: test/library_checker/graph/enumerate_cliques.test.py
  requiredBy: []
  timestamp: '2024-07-19 16:23:17+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/enumerate_cliques.test.py
layout: document
title: Enumerate Cliques
---

