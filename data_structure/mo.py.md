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
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class MoState:\n    def __init__(self,max_value):\n        self.cnt=[0]*(max_value+1)\n\
    \        self.res=0\n    def add(self, x):\n        \"\u533A\u9593\u306E\u7AEF\
    \u306B x \u3092\u8FFD\u52A0\u3059\u308B\u3068\u304D\u306E\u51E6\u7406\"\n    \
    \    self.cnt[x] += 1\n        # ToDo\n        pass\n\n    def delete(self, x):\n\
    \        \"\u533A\u9593\u306E\u7AEF\u304B\u3089 x \u3092\u524A\u9664\u3059\u308B\
    \u3068\u304D\u306E\u51E6\u7406\"\n        self.cnt[x] -= 1\n        # ToDo\n \
    \       pass\n\nclass Mo():\n    def __init__(self, arr):\n        self.arr =\
    \ arr\n        self.n = len(arr)\n        self.qs = []\n\n    def add_query(self,\
    \ l, r):\n        self.qs.append((l, r))\n\n    def _init_states(self):\n    \
    \    max_value=max(self.arr)\n        self.state=MoState(max_value)\n        self.l\
    \ = 0\n        self.r = 0\n\n    def _one_process(self, l, r):\n        \"\u30AF\
    \u30A8\u30EA\u306E\u305F\u3081\u306B\u533A\u9593\u3092\u4F38\u7E2E\u3055\u305B\
    \u308B\"\n        while l < self.l:\n            self.l -= 1\n            self.state.add(self.arr[self.l])\n\
    \        while self.r < r:\n            self.r += 1\n            self.state.add(self.arr[self.r\
    \ - 1])\n        while self.l < l:\n            self.state.delete(self.arr[self.l])\n\
    \            self.l += 1\n        while r < self.r:\n            self.state.delete(self.arr[self.r\
    \ - 1])\n            self.r -= 1\n\n    def calc(self):\n        self._init_states()\n\
    \n        qs = self.qs\n        qsize = len(qs)\n        self.b = block_size =\
    \ int((qsize-1)**0.5)+1\n        t = (self.n + block_size - 1) // block_size\n\
    \        self.buckets = [[] for b in range(t)]\n        for i,(l,r) in enumerate(qs):\n\
    \            self.buckets[l // self.b].append((r, l, i))\n       \n        ans\
    \ = [-1] * qsize\n        for i,b in enumerate(self.buckets):\n            b.sort(reverse=i&1)\n\
    \            for r,l,j in b:\n                self._one_process(l, r)\n      \
    \          ans[j] = self.state.res\n        return ans"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/mo.py
  requiredBy: []
  timestamp: '2024-02-05 08:23:41+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/mo.py
layout: document
title: Mo's Algorithm
---

静的な配列で,クエリが先読みでき,区間$[l,r)$の結果から区間$[l+1,r)$,$[l−1,r)$,$[l,r−1)$,$[l,r+1)$の結果を容易に計算できるとき,適用できる.

区間の変更に対する処理は問題ごとに設定する必要がある. `MoState`クラスに記述する.

### mo = Mo(A)

初期化．

### mo.add_query(l, r)

半開区間$[l,r)$のクエリを追加する.

### mo.calc()

クエリの結果を取得する.