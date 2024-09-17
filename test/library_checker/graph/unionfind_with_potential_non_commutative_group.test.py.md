---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/connectivity/weighted_unionfind.py
    title: graph/connectivity/weighted_unionfind.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind_with_potential_non_commutative_group
    links:
    - https://judge.yosupo.jp/problem/unionfind_with_potential_non_commutative_group
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind_with_potential_non_commutative_group\n\
    \nfrom graph.connectivity.weighted_unionfind import WeightedUnionFind\n\nMOD =\
    \ 998244353\n\n\nclass Monoid:\n    def __init__(self, a=0, b=0, c=0, d=0):\n\
    \        self.a = a\n        self.b = b\n        self.c = c\n        self.d =\
    \ d\n\n    def __str__(self):\n        return f\"M<{self.a},{self.b},{self.c},{self.d}>\"\
    \n\n    __repr__ = __str__\n\n    def __add__(self, other: \"Monoid\") -> \"Monoid\"\
    :\n        ds = [[self.a, self.b], [self.c, self.d]]\n        do = [[other.a,\
    \ other.b], [other.c, other.d]]\n        dat = [[0, 0], [0, 0]]\n        for i\
    \ in range(2):\n            for j in range(2):\n                for k in range(2):\n\
    \                    dat[i][k] += do[i][j] * ds[j][k]\n                    dat[i][k]\
    \ %= MOD\n        return Monoid(dat[0][0], dat[0][1], dat[1][0], dat[1][1])\n\n\
    \    def __neg__(self) -> \"Monoid\":\n        return Monoid(self.d, -self.b %\
    \ MOD, -self.c % MOD, self.a)\n\n    def __sub__(self, other: \"Monoid\") -> \"\
    Monoid\":\n        return self + other.__neg__()\n\n    def ok(self, other: \"\
    Monoid\") -> bool:\n        if (\n            self.a == other.a\n            and\
    \ self.b == other.b\n            and self.c == other.c\n            and self.d\
    \ == other.d\n        ):\n            return True\n        return False\n\n  \
    \  def tolist(self) -> list[int]:\n        return [self.a, self.b, self.c, self.d]\n\
    \n\nn, q = map(int, input().split())\nuf = WeightedUnionFind(n, Monoid(1, 0, 0,\
    \ 1))\nfor _ in range(q):\n    t, *qu = map(int, input().split())\n    if t ==\
    \ 0:\n        u, v, a, b, c, d = qu\n        p = Monoid(a, b, c, d)\n        if\
    \ uf.same(u, v):\n            x = uf.diff(u, v)\n            if x.ok(p):\n   \
    \             print(1)\n            else:\n                print(0)\n\n      \
    \  else:\n            uf.merge(u, v, p)\n            print(1)\n    else:\n   \
    \     u, v = qu\n        if uf.same(u, v):\n            x = uf.diff(u, v)\n  \
    \          print(*x.tolist())\n        else:\n            print(-1)\n"
  dependsOn:
  - graph/connectivity/weighted_unionfind.py
  isVerificationFile: true
  path: test/library_checker/graph/unionfind_with_potential_non_commutative_group.test.py
  requiredBy: []
  timestamp: '2024-08-29 22:20:26+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/unionfind_with_potential_non_commutative_group.test.py
layout: document
title: Unionfind with Potential (Non-Commutative Group)
---

