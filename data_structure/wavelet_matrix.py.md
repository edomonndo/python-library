---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl_3_d_sliding_minimum_element_wm.test.py
    title: test/aoj/dsl_3_d_sliding_minimum_element_wm.test.py
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/range_kth_smallest.test.py
    title: Range Kth Smallest
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/static_range_count_distinct.test.py
    title: Static Range Count Distinct
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/static_range_frequency.test.py
    title: Static Range Frequency
  - icon: ':heavy_check_mark:'
    path: test/unit_test/wavelet_matrix.test.py
    title: test/unit_test/wavelet_matrix.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from array import array\nfrom heapq import *\nfrom collections import deque\n\
    \n\nclass BitVector:\n    # \u7C21\u6F54\u30C7\u30FC\u30BF\u69CB\u9020\n    def\
    \ __init__(self, n: int):\n        self.n = n\n        self.block_size = (n +\
    \ 31) >> 5\n        b = bytes(4 * (self.block_size + 1))\n        # Unsigned int\n\
    \        self.bit = array(\"I\", b)\n        self.acc = array(\"I\", b)\n\n  \
    \  @staticmethod\n    def _popcount(x: int) -> int:\n        x = x - ((x >> 1)\
    \ & 0x55555555)\n        x = (x & 0x33333333) + ((x >> 2) & 0x33333333)\n    \
    \    x = x + (x >> 4) & 0x0F0F0F0F\n        x += x >> 8\n        x += x >> 16\n\
    \        return x & 0x0000007F\n\n    def set(self, k: int) -> None:\n       \
    \ self.bit[k >> 5] |= 1 << (k & 31)\n\n    def build(self) -> None:\n        acc,\
    \ bit = self.acc, self.bit\n        for i in range(self.block_size):\n       \
    \     acc[i + 1] = acc[i] + self._popcount(bit[i])\n\n    def access(self, k:\
    \ int) -> int:\n        return (self.bit[k >> 5] >> (k & 31)) & 1\n\n    def rank0(self,\
    \ k: int) -> int:\n        \"\"\"k\u756A\u76EE\u307E\u3067\u306B\u51FA\u73FE\u3059\
    \u308B0\u306E\u500B\u6570\"\"\"\n        return k - self.rank1(k)\n\n    def rank1(self,\
    \ k: int) -> int:\n        \"\"\"k\u756A\u76EE\u307E\u3067\u306B\u51FA\u73FE\u3059\
    \u308B1\u306E\u500B\u6570\"\"\"\n        return self.acc[k >> 5] + self._popcount(\n\
    \            self.bit[k >> 5] & ((1 << (k & 31)) - 1)\n        )\n\n    def rank01(self,\
    \ k: int) -> tuple[int, int]:\n        one = self.rank1(k)\n        zero = k -\
    \ one\n        return zero, one\n\n    def select0(self, k: int) -> int:\n   \
    \     \"\"\"\u5148\u982D\u304B\u3089k\u756A\u76EE\u306E0\u306Eindex\u3092\u6C42\
    \u3081\u308B\"\"\"\n        if k < 0 or self.rank0(self.n) <= k:\n           \
    \ return -1\n        l, r = 0, self.block_size + 1\n        while r - l > 1:\n\
    \            m = (l + r) >> 1\n            if m * 32 - self.acc[m] > k:\n    \
    \            r = m\n            else:\n                l = m\n        idx = 32\
    \ * l\n        k = k - (l * 32 - self.acc[l]) + self.rank0(idx)\n        l, r\
    \ = idx, idx + 32\n        while r - l > 1:\n            m = (l + r) >> 1\n  \
    \          if self.rank0(m) > k:\n                r = m\n            else:\n \
    \               l = m\n        return l\n\n    def select1(self, k: int) -> int:\n\
    \        \"\"\"\u5148\u982D\u304B\u3089k\u756A\u76EE\u306E1\u306Eindex\u3092\u6C42\
    \u3081\u308B\"\"\"\n        if k < 0 or self.rank1(self.n) <= k:\n           \
    \ return -1\n        l, r = 0, self.block_size + 1\n        while r - l > 1:\n\
    \            m = (l + r) >> 1\n            if self.acc[m] > k:\n             \
    \   r = m\n            else:\n                l = m\n        idx = 32 * l\n  \
    \      k = k - self.acc[l] + self.rank1(idx)\n        l, r = idx, idx + 32\n \
    \       while r - l > 1:\n            m = (l + r) >> 1\n            if self.rank1(m)\
    \ > k:\n                r = m\n            else:\n                l = m\n    \
    \    return l\n\n\nclass WaveletMatrix:\n    def __init__(self, A: list[int],\
    \ max_value: int = 10**9):\n        self.A = A\n        self.n = len(A)\n    \
    \    self.max_value = max_value\n        self.bit_size = max_value.bit_length()\n\
    \        # Unsigned int\n        self.mid = array(\"I\", bytes(4 * self.bit_size))\n\
    \        self.b = [BitVector(self.n) for _ in range(self.bit_size)]\n        self._build()\n\
    \n    def _build(self) -> None:\n        A = self.A[:]\n        for i in range(self.bit_size\
    \ - 1, -1, -1):\n            b = self.b[i]\n            zero, one = [], []\n \
    \           for j, a in enumerate(A):\n                if a >> i & 1:\n      \
    \              b.set(j)\n                    one.append(a)\n                else:\n\
    \                    zero.append(a)\n            b.build()\n            self.mid[i]\
    \ = len(zero)\n            A = zero + one\n\n    def access(self, k: int) -> int:\n\
    \        \"\"\"A\u306Ek\u756A\u76EE\u306E\u8981\u7D20\u3092\u53D6\u5F97\u3059\u308B\
    \"\"\"\n        return self.A[k]\n\n    def accessFromB(self, k: int) -> int:\n\
    \        \"\"\"A\u306Ek\u756A\u76EE\u306E\u8981\u7D20\u3092\u53D6\u5F97\u3059\u308B\
    .\u901A\u5E38access\u3067\u53D6\u5F97\u3059\u308C\u3070\u826F\u3044.\u30E1\u30E2\
    \u30EA\u524A\u6E1B\u304C\u5FC5\u8981\u306A\u3068\u304D,\u3053\u3061\u3089\u3092\
    \u5229\u7528\u3059\u308B\u3068self.A\u306E\u914D\u5217\u3092\u6301\u305F\u306A\
    \u304F\u3066\u826F\u3044\"\"\"\n        if k < 0:\n            k += self.n\n \
    \       assert 0 <= k < self.n\n        b, mid = self.b, self.mid\n        res\
    \ = 0\n        for i in range(self.bit_size - 1, -1, -1):\n            if b[i].access(k):\n\
    \                res |= 1 << i\n                k = b[i].rank1(k) + mid[i]\n \
    \           else:\n                k = b[i].rank0(k)\n        return res\n\n \
    \   def _rank(self, r: int, value: int) -> int:\n        \"\"\"A[0,r)\u306Bvalue\u304C\
    \u51FA\u73FE\u3059\u308B\u6570\u3092\u8FD4\u3059\"\"\"\n        assert r <= self.n\n\
    \        if r < 1:\n            return 0\n        l, b, mid = 0, self.b, self.mid\n\
    \        for i in range(self.bit_size - 1, -1, -1):\n            if value >> i\
    \ & 1:\n                l = b[i].rank1(l) + mid[i]\n                r = b[i].rank1(r)\
    \ + mid[i]\n            else:\n                l = b[i].rank0(l)\n           \
    \     r = b[i].rank0(r)\n        return r - l\n\n    def rank(self, l: int, r:\
    \ int, value: int) -> int:\n        \"\"\"A[l,r)\u306Bvalue\u304C\u51FA\u73FE\u3059\
    \u308B\u6570\u3092\u8FD4\u3059\"\"\"\n        if l >= r:\n            return 0\n\
    \        return self._rank(r, value) - self._rank(l, value)\n\n    def select(self,\
    \ value: int, k: int) -> int:\n        \"\"\"A\u306B\u5BFE\u3057\u3066,k\u756A\
    \u76EE\u306Evalue\u306EIndex\u3092\u8FD4\u3059(0-index). value\u304C\u51FA\u73FE\
    \u3059\u308B\u6570\u304C\u4EE5\u4E0B\u306E\u3068\u304D,-1\u3092\u8FD4\u3059\"\"\
    \"\n        if self._rank(self.n, value) <= k:\n            return -1\n      \
    \  b = self.b\n        idx = 0\n        for i in range(self.bit_size - 1, -1,\
    \ -1):\n            if value >> i & 1:\n                idx = b[i].rank0(self.n)\
    \ + b[i].rank1(idx)\n            else:\n                idx = b[i].rank0(idx)\n\
    \        idx += k\n        for i in range(self.bit_size):\n            if value\
    \ >> i & 1:\n                idx = b[i].select1(idx - b[i].rank0(self.n))\n  \
    \          else:\n                idx = b[i].select0(idx)\n        return idx\n\
    \n    def kth_smallest(self, l: int, r: int, k: int) -> int:\n        \"\"\"A[l,\
    \ r)\u306Ek\u756A\u76EE\u306B\u5C0F\u3055\u3044\u5024\u3092\u8FD4\u3059(0-index)\"\
    \"\"\n        assert 0 <= l <= r <= self.n\n        if k >= r - l:\n         \
    \   return -1\n        b, mid = self.b, self.mid\n        res = 0\n        for\
    \ i in range(self.bit_size - 1, -1, -1):\n            l0, r0 = b[i].rank0(l),\
    \ b[i].rank0(r)\n            zero_cnt = r0 - l0\n            if zero_cnt <= k:\n\
    \                res |= 1 << i\n                k -= zero_cnt\n              \
    \  l += mid[i] - l0\n                r += mid[i] - r0\n            else:\n   \
    \             l, r = l0, r0\n        return res\n\n    quantile = kth_smallest\n\
    \n    def kth_largest(self, l: int, r: int, k: int) -> int:\n        if k >= r\
    \ - l:\n            return -1\n        return self.kth_smallest(l, r, r - l -\
    \ k - 1)\n\n    def quantilerange(self, l: int, r: int, k: int) -> int:\n    \
    \    \"\"\"A[l, r)\u306Ek\u756A\u76EE\u306B\u5C0F\u3055\u3044\u5024\u306Eindex\u3092\
    \u8FD4\u3059(k\u306F0-index)\"\"\"\n        assert 0 <= l < r and r <= self.n\n\
    \        assert k <= r - l\n        val = self.quantile(l, r, k)\n        cnt_left\
    \ = self._rank(l, val)\n        return self.select(val, cnt_left)\n\n    def maxrange(self,\
    \ l: int, r: int) -> int:\n        \"\"\"A[l,r)\u3067\u6700\u5927\u5024\u306E\
    index\u3092\u8FD4\u3059\"\"\"\n        return self.quantilerange(l, r, r - l -\
    \ 1)\n\n    def minrange(self, l: int, r: int) -> int:\n        \"\"\"A[l,r)\u3067\
    \u6700\u5C0F\u5024\u306Eindex\u3092\u8FD4\u3059\"\"\"\n        return self.quantilerange(l,\
    \ r, 0)\n\n    def topk(self, l: int, r: int, k: int) -> list[tuple[int, int]]:\n\
    \        \"\"\"\n        A[l,r)\u306E\u4E2D\u3067\u51FA\u73FE\u56DE\u6570\u304C\
    \u591A\u3044\u9806\u306Bk\u500B\u306E\u5024\u3068\u983B\u5EA6\u3092\u8FD4\u3059\
    .\n        \u983B\u5EA6\u304C\u540C\u3058\u5834\u5408\u306F\u5024\u304C\u5C0F\u3055\
    \u3044\u3082\u306E\u304C\u512A\u5148\u3055\u308C\u308B.\n        \"\"\"\n    \
    \    res = []\n        b, mid = self.b, self.mid\n        pq = [(-(r - l), 0,\
    \ l, self.bit_size - 1)]  # -width, value, left, bit\n        while pq:\n    \
    \        w, v, l, i = heappop(pq)\n            w = -w\n            if i == -1:\n\
    \                res.append((v, w))\n                k -= 1\n                if\
    \ k == 0:\n                    break\n            else:\n                r = l\
    \ + w\n                l0, l1 = b[i].rank01(l)\n                r0, r1 = b[i].rank01(r)\n\
    \                if l0 < r0:\n                    heappush(pq, (-(r0 - l0), v,\
    \ l0, i - 1))\n                l1 += mid[i]\n                r1 += mid[i]\n  \
    \              if l1 < r1:\n                    heappush(pq, (-(r1 - l1), v |\
    \ (1 << i), l1, i - 1))\n        return res\n\n    def rangesum(self, l: int,\
    \ r: int) -> int:\n        \"\"\"A[l,r)\u306E\u5408\u8A08\u3092\u8FD4\u3059\"\"\
    \"\n        return sum(value * freq for value, freq in self.topk(l, r, r - l))\n\
    \n    def intersect(self, l1: int, r1: int, l2: int, r2: int) -> list[tuple[int,\
    \ int]]:\n        \"\"\"A[l1,r1)\u3068A[l2,r2)\u306E\u9593\u3067\u5171\u901A\u3057\
    \u3066\u51FA\u73FE\u3059\u308B\u5024\u3068\u983B\u5EA6\u3092\u8FD4\u3059\"\"\"\
    \n        # Not verify\n        assert l1 < r1\n        assert l2 < r2\n     \
    \   b, mid = self.b, self.mid\n        res = []\n        q = deque([(l1, r1, l2,\
    \ r2, 0, self.bit_size - 1)])  # l1, r1, l2, r2, value, i\n        while q:\n\
    \            left1, right1, left2, right2, value, i = q.popleft()\n          \
    \  if i == -1:\n                res.append((value, right1 - left1, right2 - left2))\n\
    \                continue\n            l1_0 = b[i].rank0(left1)\n            r1_0\
    \ = b[i].rank0(right1)\n            l2_0 = b[i].rank0(left2)\n            r2_0\
    \ = b[i].rank0(right2)\n            if l1_0 < r1_0 and l2_0 < r2_0:\n        \
    \        q.append((l1_0, r1_0, l2_0, r2_0, value, i - 1))\n            l1_1 =\
    \ mid[i] + b[i].rank1(left1)\n            r1_1 = mid[i] + b[i].rank1(right1)\n\
    \            l2_1 = mid[i] + b[i].rank1(left2)\n            r2_1 = mid[i] + b[i].rank1(right2)\n\
    \            if l1_1 < r1_1 and l2_1 < r2_1:\n                q.append((l1_1,\
    \ r1_1, l2_1, r2_1, value | (1 << i), i - 1))\n        return res\n\n    def rangefreq_to(self,\
    \ l: int, r: int, value: int) -> int:\n        \"\"\"A[l,r)\u306B\u51FA\u73FE\u3059\
    \u308B0<=z<value\u3092\u6E80\u305F\u3059z\u306E\u6570\u3092\u8FD4\u3059\"\"\"\n\
    \        if value <= 0:\n            return 0\n        if l >= r or self.n ==\
    \ 0:\n            return 0\n        res = 0\n        b, mid = self.b, self.mid\n\
    \        for i in range(self.bit_size - 1, -1, -1):\n            l0, r0 = b[i].rank0(l),\
    \ b[i].rank0(r)\n            if value >> i & 1:\n                res += r0 - l0\n\
    \                l += mid[i] - l0\n                r += mid[i] - r0\n        \
    \    else:\n                l, r = l0, r0\n        return res\n\n    def rangefreq(self,\
    \ l: int, r: int, x: int, y: int) -> int:\n        \"\"\"A[l,r)\u306B\u51FA\u73FE\
    \u3059\u308Bx<=z<y\u3092\u6E80\u305F\u3059z\u306E\u6570\u3092\u8FD4\u3059\"\"\"\
    \n        if x >= y or self.n == 0:\n            return 0\n        return self.rangefreq_to(l,\
    \ r, y) - self.rangefreq_to(l, r, x)\n\n    def prevvalue(self, l: int, r: int,\
    \ x: int) -> int:\n        \"\"\"A[l,r)\u306B\u51FA\u73FE\u3059\u308Bc<x\u3092\
    \u6E80\u305F\u3059\u6700\u5927\u306Ec\u3092\u8FD4\u3059\"\"\"\n        assert\
    \ l < r and 0 < r <= self.n\n        assert 0 <= x\n        cnt = self.rangefreq_to(l,\
    \ r, x)\n        if cnt == 0:\n            return -1\n        return self.kth_smallest(l,\
    \ r, cnt - 1)\n\n    def nextvalue(self, l: int, r: int, x: int) -> int:\n   \
    \     \"\"\"A[l,r)\u306B\u51FA\u73FE\u3059\u308Bx<=c\u3092\u6E80\u305F\u3059\u6700\
    \u5C0F\u306Ec\u3092\u8FD4\u3059\"\"\"\n        assert l < r and 0 < r <= self.n\n\
    \        assert 0 <= x\n        cnt = self.rangefreq_to(l, r, x)\n        if cnt\
    \ == r - l:\n            return -1\n        return self.kth_smallest(l, r, cnt)\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/wavelet_matrix.py
  requiredBy: []
  timestamp: '2024-05-21 17:51:29+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/range_kth_smallest.test.py
  - test/library_checker/data_structure/static_range_count_distinct.test.py
  - test/library_checker/data_structure/static_range_frequency.test.py
  - test/aoj/dsl_3_d_sliding_minimum_element_wm.test.py
  - test/unit_test/wavelet_matrix.test.py
documentation_of: data_structure/wavelet_matrix.py
layout: document
title: "\u30A6\u30A7\u30FC\u30D6\u30EC\u30C3\u30C8\u884C\u5217"
---

静的配列を高速に検索する．
前処理: $n$列$b$ビットの配列で$0(nb)$, 検索: ($O(\log b)$ or $O(k\log b)$)


参考：
https://miti-7.hatenablog.com/entry/2018/04/28/152259
https://miti-7.hatenablog.com/entry/2018/04/15/155638
