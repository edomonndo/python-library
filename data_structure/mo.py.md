---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':grey_question:'
    path: test/atcoder/abc242g.test.py
    title: test/atcoder/abc242g.test.py
  - icon: ':grey_question:'
    path: test/atcoder/abc293g.test.py
    title: test/atcoder/abc293g.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class MoState:\n    def __init__(self, max_value):\n        self.cnt = [0]\
    \ * (max_value + 1)\n        self.res = 0\n\n    def add(self, x):\n        \"\
    \u533A\u9593\u306E\u7AEF\u306B x \u3092\u8FFD\u52A0\u3059\u308B\u3068\u304D\u306E\
    \u51E6\u7406\"\n        self.cnt[x] += 1\n        # ToDo\n        pass\n\n   \
    \ def delete(self, x):\n        \"\u533A\u9593\u306E\u7AEF\u304B\u3089 x \u3092\
    \u524A\u9664\u3059\u308B\u3068\u304D\u306E\u51E6\u7406\"\n        self.cnt[x]\
    \ -= 1\n        # ToDo\n        pass\n\n\nclass Mo:\n    def __init__(self, arr,\
    \ state: MoState):\n        self.arr = arr\n        self.qs = []\n        self.n_min\
    \ = 10**9\n        self.n_max = -(10**9)\n        self.state = state\n\n    def\
    \ add_query(self, l, r):\n        \"\"\"[l, r)\"\"\"\n        self.qs.append((l,\
    \ r))\n        self.n_min = min(self.n_min, l)\n        self.n_max = max(self.n_max,\
    \ r)\n\n    def calc(self):\n        max_value = max(self.arr)\n        state\
    \ = self.state\n\n        n_min, n_max = self.n_min, self.n_max\n        N = n_max\
    \ - n_min\n        qs = self.qs\n        Q = len(qs)\n        shift = Q.bit_length()\n\
    \        mask = (1 << shift) - 1\n        block_cnt = max(1, int(min(N, Q**0.5)))\n\
    \        block_size = (N + block_cnt - 1) // block_cnt\n        buckets = [[]\
    \ for _ in range(block_cnt)]\n        for i, (l, r) in enumerate(qs):\n      \
    \      l -= n_min\n            r -= n_min\n            bi = l // block_size\n\
    \            x = -r if bi & 1 else r\n            x = (x << shift) | i\n     \
    \       buckets[bi].append(x)\n        for i in range(block_cnt):\n          \
    \  buckets[i].sort()\n        ans = [-1] * Q\n        l = r = qs[0][0]\n     \
    \   for b in buckets:\n            for ri in b:\n                i = ri & mask\n\
    \                L, R = qs[i]\n                \"\u30AF\u30A8\u30EA\u306E\u305F\
    \u3081\u306B\u533A\u9593\u3092\u4F38\u7E2E\u3055\u305B\u308B\"\n             \
    \   while r < R:\n                    state.add(self.arr[r])\n               \
    \     r += 1\n                while r > R:\n                    r -= 1\n     \
    \               state.delete(self.arr[r])\n                while l < L:\n    \
    \                state.delete(self.arr[l])\n                    l += 1\n     \
    \           while l > L:\n                    l -= 1\n                    state.add(self.arr[l])\n\
    \                ans[i] = state.res\n        return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/mo.py
  requiredBy: []
  timestamp: '2024-02-28 11:58:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith:
  - test/atcoder/abc293g.test.py
  - test/atcoder/abc242g.test.py
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