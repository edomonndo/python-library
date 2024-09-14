---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/connectivity/range_parallel_unionfind.py
    title: Range Parallel Union Find
  - icon: ':question:'
    path: graph/connectivity/unionfind.py
    title: Union Find
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/range_parallel_unionfind
    links:
    - https://judge.yosupo.jp/problem/range_parallel_unionfind
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_parallel_unionfind\n\
    \nfrom graph.connectivity.unionfind import UnionFind\nfrom graph.connectivity.range_parallel_unionfind\
    \ import RangeParallelUnionFind\n\nMOD = 998244353\n\nn, q = map(int, input().split())\n\
    X = [int(x) for x in input().split()]\nrpuf = RangeParallelUnionFind(n)\nuf =\
    \ UnionFind(n)\nans = 0\nfor i in range(q):\n    k, a, b = map(int, input().split())\n\
    \    if k != 0 and a != b:\n        for u, v in rpuf.enumerate(a, b, k):\n   \
    \         u = uf.leader(u)\n            v = uf.leader(v)\n            w = uf.merge(u,\
    \ v)\n            ans += X[u] * X[v] % MOD\n            ans %= MOD\n         \
    \   X[w] = X[u] + X[v]\n    print(ans)\n"
  dependsOn:
  - graph/connectivity/unionfind.py
  - graph/connectivity/range_parallel_unionfind.py
  isVerificationFile: true
  path: test/library_checker/graph/range_parallel_unionfind.test.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/range_parallel_unionfind.test.py
layout: document
title: Range Parallel Unionfind
---

