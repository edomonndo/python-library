---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/static_range_mode_query.test.py
    title: test/library_checker/data_structure/static_range_mode_query.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class StaticRangeModeQuery:\n\n    def __init__(self, A: list[int]):\n  \
    \      # \u5EA7\u6A19\u5727\u7E2E(\u540C\u3058\u5024\u306Findex\u3067\u8B58\u5225\
    )\n        self.inv_A = sorted(set(A))\n        d = {a: i for i, a in enumerate(self.inv_A)}\n\
    \        self.A = [d[a] for a in A]\n\n        self.n = n = len(self.A)\n    \
    \    self.max_value = max(self.A)\n        self.size = size = int(n**0.5) + 1\n\
    \        self.bucket_cnt = (n + size - 1) // size\n        self.data = [self.A[i\
    \ * size : (i + 1) * size] for i in range(self.bucket_cnt)]\n\n        self.idx\
    \ = [[] for _ in range(self.max_value + 1)]\n        self.inv_idx = [-1] * n\n\
    \        for i, a in enumerate(self.A):\n            self.inv_idx[i] = len(self.idx[a])\n\
    \            self.idx[a].append(i)\n        # list[list[(freq, val)]]\n      \
    \  self.bucket_data = self._calc_bucket()\n\n    def _calc_bucket(self) -> list[list[tuple[int,\
    \ int]]]:\n        data = self.data\n        res = [[(0, -1)] * (self.bucket_cnt\
    \ + 1) for _ in range(self.bucket_cnt + 1)]\n        freqs = [0] * (self.max_value\
    \ + 1)\n        for i in range(self.bucket_cnt):\n            freq, val = -1,\
    \ -1\n            for j in range(i + 1, self.bucket_cnt + 1):\n              \
    \  for x in data[j - 1]:\n                    freqs[x] += 1\n                \
    \    if freqs[x] > freq:\n                        freq, val = freqs[x], x\n  \
    \              res[i][j] = (freq, val)\n            for j in range(i + 1, self.bucket_cnt\
    \ + 1):\n                for x in data[j - 1]:\n                    freqs[x] =\
    \ 0\n        return res\n\n    def query(self, l: int, r: int) -> tuple[int, int]:\n\
    \        \"\"\"(\u6700\u983B\u5024\uFF0C\u983B\u5EA6)\u3092\u6C42\u3081\u307E\u3059\
    .\"\"\"\n        assert 0 <= l < r <= self.n\n        L, R = l, r\n        k1,\
    \ k2 = l // self.size, r // self.size\n        l -= k1 * self.size\n        r\
    \ -= k2 * self.size\n\n        freq, val = 0, -1\n\n        if k1 == k2:\n   \
    \         A, idx, inv_idx = self.A, self.idx, self.inv_idx\n            for i\
    \ in range(L, R):\n                x = A[i]\n                k = inv_idx[i]\n\
    \                while k + freq < len(idx[x]) and idx[x][k + freq] < R:\n    \
    \                freq += 1\n                    val = x\n        else:\n     \
    \       data, idx, inv_idx = self.data, self.idx, self.inv_idx\n            freq,\
    \ val = self.bucket_data[k1 + 1][k2]\n\n            for i in range(l, len(data[k1])):\n\
    \                x = data[k1][i]\n                k = inv_idx[k1 * self.size +\
    \ i]\n                while k + freq < len(idx[x]) and idx[x][k + freq] < R:\n\
    \                    freq += 1\n                    val = x\n            for i\
    \ in range(r):\n                x = data[k2][i]\n                k = inv_idx[k2\
    \ * self.size + i]\n                while 0 <= k - freq and L <= idx[x][k - freq]:\n\
    \                    freq += 1\n                    val = x\n        val = self.inv_A[val]\n\
    \        return val, freq\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/static_range_mode_query.py
  requiredBy: []
  timestamp: '2024-05-21 17:51:29+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/static_range_mode_query.test.py
documentation_of: data_structure/static_range_mode_query.py
layout: document
title: "\u533A\u9593\u6700\u983B\u5024"
---

静的な数列の区間に対して最頻値と頻度を求めます.
計算量は,前処理$O(N\sqrt{N})$, クエリ$O(\sqrt{N})$です．
