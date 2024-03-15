---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from bisect import bisect_right, bisect_left\nclass MergeSortTree:\n    def\
    \ __init__(self, V):\n        n = len(V)\n        d = [None]*n*2\n        cum\
    \ = [None]*n*2\n        for i,a in enumerate(V):\n            d[n+i] = [a]\n \
    \           cum[n+i] = [0,a]\n        for i in reversed(range(1,n)):\n       \
    \     d[i] = d[i*2] + d[i*2+1]\n            d[i].sort()\n            cum[i]=[0]\n\
    \            for a in d[i]:\n              cum[i].append(cum[i][-1]+a)\n     \
    \   self.n = n\n        self.d = d\n        self.cum = cum\n\n    def sum_le(self,\
    \ l, r, x):\n        assert 0 <= l and l <= r and r <= self.n\n        l += self.n\n\
    \        r += self.n\n        res = 0\n        while l < r:\n            if l\
    \ & 1:\n                i = bisect_right(self.d[l],x)\n                res +=\
    \ self.cum[l][i]\n                l += 1\n            if r & 1:\n            \
    \    r -= 1\n                i = bisect_right(self.d[r],x)\n                res\
    \ += self.cum[r][i]\n            l >>= 1\n            r >>= 1\n        return\
    \ res\n    \n    def sum_lt(self, l, r, x):\n        assert 0 <= l and l <= r\
    \ and r <= self.n\n        l += self.n\n        r += self.n\n        res = 0\n\
    \        while l < r:\n            if l & 1:\n                i = bisect_left(self.d[l],x)\n\
    \                res += self.cum[l][i]\n                l += 1\n            if\
    \ r & 1:\n                r -= 1\n                i = bisect_left(self.d[r],x)\n\
    \                res += self.cum[r][i]\n            l >>= 1\n            r >>=\
    \ 1\n        return res"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/merge_sort_tree.py
  requiredBy: []
  timestamp: '2024-02-05 08:23:41+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/merge_sort_tree.py
layout: document
title: Merge Sort Tree
---

セグメント木にソート済みの配列をのせたもの.


### mst = MergeSortTree(arr)

初期化．$arr$はクエリの配列であり変更不可．

### mst.sum_le(l, r, x)

配列$arr$の半開区間$[l,r)$で、$x$以下の値の合計を計算する.

### mst.sum_lt(l, r, x)

配列$arr$の半開区間$[l,r)$で、$x$未満の値の合計を計算する.