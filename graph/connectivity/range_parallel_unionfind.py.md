---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: atcoder/dsu.py
    title: atcoder/dsu.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/range_parallel_unionfind.test.py
    title: Range Parallel Unionfind
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from atcoder.dsu import DSU\n\n\nclass RangeParallelUnionFind:\n    def __init__(self,\
    \ n):\n        self.n = n\n        self.ufs = []\n        num = 1\n        while\
    \ (1 << (num * 2)) < n:\n            num += 1\n        for i in range(num):\n\
    \            self.ufs.append(DSU(max(1, n - (1 << (i * 2)) + 1)))\n\n    def enumerate(self,\
    \ u: int, v: int, d: int) -> list[tuple[int, int]]:\n        \"enumerate pair\
    \ of (u, v) corresponds to merge(u + i, v + i) for i in range(d)\"\n        if\
    \ u == v or d <= 0:\n            return\n        assert 0 <= u < self.n and 0\
    \ <= v < self.n\n        assert u + d <= self.n and v + d <= self.n\n        if\
    \ u > v:\n            u, v = v, u\n        res = []\n        width = v - u\n\n\
    \        def dfs(p: int, num: int):\n            st = [(p, num)]\n           \
    \ while st:\n                p, num = st.pop()\n                if self.ufs[num].same(p,\
    \ p + width):\n                    continue\n                self.ufs[num].merge(p,\
    \ p + width)\n                if num == 0:\n                    res.append((p,\
    \ p + width))\n                    continue\n                for t in range(4):\n\
    \                    st.append((p + (t << (2 * num - 2)), num - 1))\n        \
    \    return\n\n        b = 0\n        w = 1\n        while w * 4 < d:\n      \
    \      b += 1\n            w *= 4\n        while d > 0:\n            d = max(0,\
    \ d - w)\n            dfs(u + d, b)\n        return res\n"
  dependsOn:
  - atcoder/dsu.py
  isVerificationFile: false
  path: graph/connectivity/range_parallel_unionfind.py
  requiredBy: []
  timestamp: '2024-07-29 12:40:49+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/range_parallel_unionfind.test.py
documentation_of: graph/connectivity/range_parallel_unionfind.py
layout: document
title: Range Parallel Union Find
---
