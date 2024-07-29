---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/connectivity/weighted_unionfind.py
    title: "\u91CD\u307F\u4ED8\u304D Union Find"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind_with_potential
    links:
    - https://judge.yosupo.jp/problem/unionfind_with_potential
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind_with_potential\n\
    \nfrom graph.connectivity.weighted_unionfind import WeightedUnionFind\n\nMOD =\
    \ 998244353\n\n\nclass Monoid:\n    def __init__(self, val=0):\n        self.val\
    \ = val % MOD\n\n    def __str__(self):\n        return f\"M<{self.val}>\"\n\n\
    \    __repr__ = __str__\n\n    def __add__(self, other: \"Monoid\") -> \"Monoid\"\
    :\n        return Monoid(self.val + other.val)\n\n    def __neg__(self) -> \"\
    Monoid\":\n        return Monoid(-self.val)\n\n    def __sub__(self, other: \"\
    Monoid\") -> \"Monoid\":\n        return self + other.__neg__()\n\n\nn, q = map(int,\
    \ input().split())\nuf = WeightedUnionFind(n, Monoid(0))\nfor _ in range(q):\n\
    \    t, *qu = map(int, input().split())\n    if t == 0:\n        u, v, x = qu\n\
    \        if uf.same(u, v):\n            if uf.diff(u, v).val == x:\n         \
    \       print(1)\n            else:\n                print(0)\n        else:\n\
    \            uf.merge(u, v, Monoid(x))\n            print(1)\n    else:\n    \
    \    u, v = qu\n        res = uf.diff(u, v)\n        if res:\n            print(res.val)\n\
    \        else:\n            print(-1)\n"
  dependsOn:
  - graph/connectivity/weighted_unionfind.py
  isVerificationFile: true
  path: test/library_checker/graph/unionfind_with_potential.test.py
  requiredBy: []
  timestamp: '2024-07-29 12:40:49+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/unionfind_with_potential.test.py
layout: document
title: Unionfind with Potential
---

