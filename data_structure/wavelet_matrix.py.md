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
    title: test/library_checker/data_structure/range_kth_smallest.test.py
  - icon: ':grey_question:'
    path: test/library_checker/data_structure/static_range_count_distinct.test.py
    title: test/library_checker/data_structure/static_range_count_distinct.test.py
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/static_range_frequency.test.py
    title: test/library_checker/data_structure/static_range_frequency.test.py
  - icon: ':heavy_check_mark:'
    path: test/unit_test/wavelet_matrix.test.py
    title: test/unit_test/wavelet_matrix.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import heapq\nfrom collections import deque\n\n\nclass BitVector:\n    #\
    \ \u7C21\u6F54\u30C7\u30FC\u30BF\u69CB\u9020\n    # B := \u9577\u3055n\u306E01\u5217\
    \n    def __init__(self, B: list):\n        self.n = len(B)\n        self.B =\
    \ B\n        # \u7D2F\u7A4D\u548C\n        self.SB = [0]\n        for b in B:\n\
    \            self.SB.append(self.SB[-1] + b)\n\n    def access(self, i: int) ->\
    \ int:\n        # B[i]\u3092\u8FD4\u3059\n        return self.B[i]\n\n    def\
    \ rank0(self, i: int) -> int:\n        # B\u306B\u5BFE\u3057\u3066,i\u756A\u76EE\
    \u307E\u3067\u306B\u51FA\u73FE\u3059\u308B0\u306E\u500B\u6570\n        return\
    \ i - self.rank1(i)\n\n    def rank1(self, i: int) -> int:\n        # B\u306B\u5BFE\
    \u3057\u3066,i\u756A\u76EE\u307E\u3067\u306B\u51FA\u73FE\u3059\u308B1\u306E\u500B\
    \u6570\n        return self.SB[i]\n\n    def select0(self, k: int) -> int:\n \
    \       # B\u306B\u5BFE\u3057\u3066,\u5148\u982D\u304B\u3089k\u756A\u76EE\u306E\
    0\u306Eindex\u3092\u6C42\u3081\u308B\n        l, r = 0, len(self.SB)\n       \
    \ if not k < r - 1 - self.SB[r - 1]:\n            return -1\n        while r -\
    \ l > 1:\n            mid = l + r >> 1\n            if mid - self.SB[mid] <= k:\n\
    \                l = mid\n            else:\n                r = mid\n       \
    \ return l\n\n    def select1(self, k: int) -> int:\n        # B\u306B\u5BFE\u3057\
    \u3066,\u5148\u982D\u304B\u3089k\u756A\u76EE\u306E1\u306Eindex\u3092\u6C42\u3081\
    \u308B\n        l, r = 0, len(self.SB)\n        if not k < self.SB[r - 1]:\n \
    \           return -1\n        while r - l > 1:\n            mid = l + r >> 1\n\
    \            if self.SB[mid] <= k:\n                l = mid\n            else:\n\
    \                r = mid\n        return l\n\n\nclass WaveletMatrix:\n    # \u5B8C\
    \u5099\u8F9E\u66F8\n    # s := bit\u9577\n    # A := \u9577\u3055n\u306E\u914D\
    \u5217\n    def __init__(self, A):\n        self.bit_size = len(bin(max(A))) -\
    \ 2 if A else 0\n        self.A = A\n        self.n = len(A)\n        T = A[:]\n\
    \        self.B = []\n        for i in range(self.bit_size)[::-1]:\n         \
    \   L = []\n            R = []\n            _T = []\n            for b in T:\n\
    \                if b >> i & 1 == 0:\n                    _T.append(0)\n     \
    \               L.append(b)\n                else:\n                    _T.append(1)\n\
    \                    R.append(b)\n            bv = BitVector(_T)\n           \
    \ self.B.append((bv.rank0(self.n), bv))\n            T = L + R\n\n    def access(self,\
    \ i: int) -> int:\n        # A\u306Ei\u756A\u76EE\u306E\u8981\u7D20\u3092\u53D6\
    \u5F97\u3059\u308B\n        return self.A[i]\n\n    def accessFromB(self, i: int)\
    \ -> int:\n        # A\u306Ei\u756A\u76EE\u306E\u8981\u7D20\u3092\u53D6\u5F97\u3059\
    \u308B\n        # \u901A\u5E38access\u3067\u53D6\u5F97\u3059\u308C\u3070\u826F\
    \u3044.\u9AD8\u901F\u5316\u304C\u5FC5\u8981\u306A\u3068\u304D,\u3053\u3061\u3089\
    \u3092\u5229\u7528\u3059\u308B\u3068self.A\u306E\u914D\u5217\u3092\u6301\u305F\
    \u306A\u304F\u3066\u826F\u3044\n        # \u5B9F\u969B\u306B\u901F\u304F\u306A\
    \u308B\u304B\u306F\u4E0D\u660E\n        assert 0 <= i < self.n\n        res =\
    \ 0\n        for z, bv in self.B:\n            bit = bv.access(i)\n          \
    \  res = (res << 1) | bit\n            if bit:\n                i = z + bv.rank1(i)\n\
    \            else:\n                i = bv.rank0(i)\n        return res\n\n  \
    \  def rank(self, l, r, value):\n        # A[l,r)\u306Bvalue\u304C\u51FA\u73FE\
    \u3059\u308B\u6570\u3092\u8FD4\u3059\n        if l >= r:\n            return 0\n\
    \        for i, (z, bv) in enumerate(self.B):\n            # 1\n            if\
    \ (value >> (self.bit_size - i - 1)) & 1:\n                l = z + bv.rank1(l)\n\
    \                r = z + bv.rank1(r)\n            # 0\n            else:\n   \
    \             l = bv.rank0(l)\n                r = bv.rank0(r)\n        return\
    \ r - l\n\n    def select(self, value, k):\n        # A\u306B\u5BFE\u3057\u3066\
    ,k\u756A\u76EE\u306Evalue\u306EIndex\u3092\u8FD4\u3059(0-index)\n        # value\u304C\
    \u51FA\u73FE\u3059\u308B\u6570\u304C\u4EE5\u4E0B\u306E\u3068\u304D,-1\u3092\u8FD4\
    \u3059\n        if self.rank(0, self.n, value) <= k:\n            return -1\n\
    \        idx = 0\n        for i, (z, bv) in enumerate(self.B):\n            #\
    \ 1\n            if (value >> (self.bit_size - i - 1)) & 1:\n                idx\
    \ = z + bv.rank1(idx)\n            # 0\n            else:\n                idx\
    \ = bv.rank0(idx)\n        idx += k\n        for z, bv in self.B[::-1]:\n    \
    \        # 0\n            if idx < z:\n                idx = bv.select0(idx)\n\
    \            # 1\n            else:\n                idx = bv.select1(idx - z)\n\
    \        return idx\n\n    def quantile(self, l, r, k):\n        # A[l, r)\u306E\
    k\u756A\u76EE\u306B\u5C0F\u3055\u3044\u5024\u3092\u8FD4\u3059(0-index)\n     \
    \   if k >= r - l:\n            return -1\n        ret = 0\n        for i, (z,\
    \ bv) in enumerate(self.B):\n            zeros = bv.rank0(r) - bv.rank0(l)\n \
    \           # 0\n            if zeros > k:\n                l = bv.rank0(l)\n\
    \                r = bv.rank0(r)\n            # 1\n            else:\n       \
    \         k -= zeros\n                ret |= 1 << (self.bit_size - i - 1)\n  \
    \              l = z + bv.rank1(l)\n                r = z + bv.rank1(r)\n    \
    \    return ret\n\n    def quantilerange(self, l, r, k):\n        # A[l, r)\u306E\
    k\u756A\u76EE\u306B\u5C0F\u3055\u3044\u5024\u306Eindex\u3092\u8FD4\u3059(k\u306F\
    0-index)\n        assert 0 <= l < r and r <= self.n\n        assert k < r - l\n\
    \n        val = 0\n        for z, bv in self.B:\n            num_of_zero_l = bv.rank0(l)\n\
    \            num_of_zero_r = bv.rank0(r)\n            num_or_zero = num_of_zero_r\
    \ - num_of_zero_l  # l\u304B\u3089r\u307E\u3067\u306B\u3042\u308B0\u306E\u6570\
    \n            bit = 0 if k < num_or_zero else 1  # k\u756A\u76EE\u306E\u5024\u306E\
    \u4E0A\u304B\u3089i\u756A\u76EE\u306Ebit\u5024\n\n            if bit:\n      \
    \          k -= num_or_zero\n                l = z + l - num_of_zero_l\n     \
    \           r = z + r - num_of_zero_r\n            else:\n                l =\
    \ num_of_zero_l\n                r = num_of_zero_l + num_or_zero\n           \
    \ val = (val << 1) | bit\n\n        left = 0\n        for i, (z, bv) in enumerate(self.B):\n\
    \            bit = (val >> (self.bit_size - i - 1)) & 1  # \u4E0A\u304B\u3089\
    i\u756A\u76EE\u306Ebit\u5024\n            if bit:\n                left = z +\
    \ bv.rank1(left)\n            else:\n                left = bv.rank0(left)\n \
    \       rank = l + k - left\n        return self.select(val, rank)\n\n    def\
    \ maxrange(self, l, r):\n        # A[l,r)\u3067\u6700\u5927\u5024\u306Eindex\u3092\
    \u8FD4\u3059\n        return self.quantilerange(l, r, r - l - 1)\n\n    def minrange(self,\
    \ l, r):\n        # A[l,r)\u3067\u6700\u5C0F\u5024\u306Eindex\u3092\u8FD4\u3059\
    \n        return self.quantilerange(l, r, 0)\n\n    def topk(self, l, r, k):\n\
    \        # A[l,r)\u306E\u4E2D\u3067\u51FA\u73FE\u56DE\u6570\u304C\u591A\u3044\u9806\
    \u306Bk\u500B\u306E\u5024\u3068\u983B\u5EA6\u3092\u8FD4\u3059\n        # \u983B\
    \u5EA6\u304C\u540C\u3058\u5834\u5408\u306F\u5024\u304C\u5C0F\u3055\u3044\u3082\
    \u306E\u304C\u512A\u5148\u3055\u308C\u308B\n        # \u30AD\u30E5\u30FC\u306F\
    \u6700\u5927\u306Ewidth\u3092\u30AD\u30FC\u3068\u3059\u308B\u305F\u3081,\u30DE\
    \u30A4\u30CA\u30B9\u3092\u3064\u3051\u308B\n        res = []\n        pq = [(-(r\
    \ - l), 0, 0, l, r)]  # -width, depth, value, left, right\n        while pq and\
    \ k > 0:\n            _, depth, value, left, right = heapq.heappop(pq)\n     \
    \       if depth >= self.bit_size:\n                res.append((value, right -\
    \ left))\n                k -= 1\n                continue\n\n            z, bv\
    \ = self.B[depth]\n            # 0\n            l0 = bv.rank0(left)\n        \
    \    r0 = bv.rank0(right)\n            if l0 < r0:\n                heapq.heappush(pq,\
    \ (-(r0 - l0), depth + 1, value, l0, r0))\n            # 1\n            l1 = z\
    \ + bv.rank1(left)\n            r1 = z + bv.rank1(right)\n            if l1 <\
    \ r1:\n                nv = value | (1 << (self.bit_size - depth - 1))\n     \
    \           heapq.heappush(pq, (-(r1 - l1), depth + 1, nv, l1, r1))\n        return\
    \ res\n\n    def rangesum(self, l, r):\n        # A[l,r)\u306E\u5408\u8A08\u3092\
    \u8FD4\u3059\n        return sum(value * freq for value, freq in self.topk(l,\
    \ r, r - l))\n\n    def intersect(self, l1, r1, l2, r2):\n        # A[l1,r1)\u3068\
    A[l2,r2)\u306E\u9593\u3067\u5171\u901A\u3057\u3066\u51FA\u73FE\u3059\u308B\u5024\
    \u3068\u983B\u5EA6\u3092\u8FD4\u3059\n        assert l1 < r1\n        assert l2\
    \ < r2\n        res = []\n        que = deque([(l1, r1, l2, r2, 0, 0)])  # l1,\
    \ r1, l2, r2, depth, value\n        while que:\n            left1, right1, left2,\
    \ right2, depth, value = que.popleft()\n            if depth >= self.bit_size:\n\
    \                res.append((value, right1 - left1, right2 - left2))\n       \
    \         continue\n            z, bv = self.B[depth]\n            # 0\n     \
    \       l1_0 = bv.rank0(left1)\n            r1_0 = bv.rank0(right1)\n        \
    \    l2_0 = bv.rank0(left2)\n            r2_0 = bv.rank0(right2)\n           \
    \ if l1_0 < r1_0 and l2_0 < r2_0:\n                que.append((l1_0, r1_0, l2_0,\
    \ r2_0, depth + 1, value))\n            # 1\n            l1_1 = z + bv.rank1(left1)\n\
    \            r1_1 = z + bv.rank1(right1)\n            l2_1 = z + bv.rank1(left2)\n\
    \            r2_1 = z + bv.rank1(right2)\n            if l1_1 < r1_1 and l2_1\
    \ < r2_1:\n                nv = value | (1 << (self.bit_size - depth - 1))\n \
    \               que.append((l1_1, r1_1, l2_1, r2_1, depth + 1, nv))\n\n      \
    \  return res\n\n    def rangefreq_to(self, l, r, value):\n        # A[l,r)\u306B\
    \u51FA\u73FE\u3059\u308B0<=z<value\u3092\u6E80\u305F\u3059z\u306E\u6570\u3092\u8FD4\
    \u3059\n        if not value:\n            return 0\n        if l >= r or self.n\
    \ == 0:\n            return 0\n        ret = 0\n        for i, (z, bv) in enumerate(self.B):\n\
    \            # 1\n            if (value >> (self.bit_size - i - 1)) & 1:\n   \
    \             ret += bv.rank0(r) - bv.rank0(l)\n                l = z + bv.rank1(l)\n\
    \                r = z + bv.rank1(r)\n            # 0\n            else:\n   \
    \             l = bv.rank0(l)\n                r = bv.rank0(r)\n        return\
    \ ret\n\n    def rangefreq(self, l, r, x, y):\n        # A[l,r)\u306B\u51FA\u73FE\
    \u3059\u308Bx<=z<y\u3092\u6E80\u305F\u3059z\u306E\u6570\u3092\u8FD4\u3059\n  \
    \      if x >= y or self.n == 0:\n            return 0\n        return self.rangefreq_to(l,\
    \ r, y) - self.rangefreq_to(l, r, x)\n\n    def prevvalue(self, l, r, x, y):\n\
    \        # A[l,r)\u306B\u51FA\u73FE\u3059\u308Bx<=c<y\u3092\u6E80\u305F\u3059\u6700\
    \u5927\u306Ec\u3092\u8FD4\u3059\n        assert l < r and 0 < r <= self.n\n  \
    \      assert 0 <= x < y\n\n        y = min(y, self.n)\n        y -= 1  # \u3000\
    \u9589\u533A\u9593A[l,r]\u306B\u3059\u308B\n\n        stack = [(l, r, 0, 0, True)]\
    \  # l,r,depth,z,tight\n        while stack:\n            l, r, depth, c, tight\
    \ = stack.pop()\n            if depth == self.bit_size:\n                if c\
    \ >= x:\n                    return c\n                continue\n            bit\
    \ = (y >> (self.bit_size - depth - 1)) & 1\n            z, bv = self.B[depth]\n\
    \            rank0_l = bv.rank0(l)\n            rank0_r = bv.rank0(r)\n      \
    \      rank1_l = l - rank0_l\n            rank1_r = r - rank0_r\n\n          \
    \  # 0\n            l0 = rank0_l\n            r0 = rank0_r\n            if l0\
    \ != r0:\n                c0 = (c << 1) | 0\n                stack.append((l0,\
    \ r0, depth + 1, c0, tight and bit == 0))\n            # 1\n            l1 = z\
    \ + rank1_l\n            r1 = z + rank1_r\n            if l1 != r1:\n        \
    \        if not tight or bit == 1:\n                    c1 = (c << 1) | 1\n  \
    \                  stack.append((l1, r1, depth + 1, c1, tight))\n        # \u898B\
    \u3064\u304B\u3089\u306A\u3044\u3068\u30A8\u30E9\u30FC\n        return -1\n\n\
    \    def nextvalue(self, l, r, x, y):\n        # A[l,r)\u306B\u51FA\u73FE\u3059\
    \u308Bx<=c<y\u3092\u6E80\u305F\u3059\u6700\u5C0F\u306Ec\u3092\u8FD4\u3059\n  \
    \      assert l < r and 0 < r <= self.n\n        assert 0 <= x < y\n\n       \
    \ stack = [(l, r, 0, 0, True)]  # l,r,depth,z,tight\n        while stack:\n  \
    \          l, r, depth, c, tight = stack.pop()\n            if depth == self.bit_size:\n\
    \                if c < y:\n                    return c\n                continue\n\
    \            bit = (x >> (self.bit_size - depth - 1)) & 1\n            z, bv =\
    \ self.B[depth]\n            rank0_l = bv.rank0(l)\n            rank0_r = bv.rank0(r)\n\
    \            rank1_l = l - rank0_l\n            rank1_r = r - rank0_r\n\n    \
    \        # 1\n            l1 = z + rank1_l\n            r1 = z + rank1_r\n   \
    \         if l1 != r1:\n                c1 = (c << 1) | 1\n                stack.append((l1,\
    \ r1, depth + 1, c1, tight and bit == 1))\n            # 0\n            l0 = rank0_l\n\
    \            r0 = rank0_r\n            if l0 != r0:\n                if not tight\
    \ or bit == 0:\n                    c0 = (c << 1) | 0\n                    stack.append((l0,\
    \ r0, depth + 1, c0, tight))\n        # \u898B\u3064\u304B\u3089\u306A\u3044\u3068\
    \u30A8\u30E9\u30FC\n        return -1\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/wavelet_matrix.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/dsl_3_d_sliding_minimum_element_wm.test.py
  - test/library_checker/data_structure/range_kth_smallest.test.py
  - test/library_checker/data_structure/static_range_frequency.test.py
  - test/library_checker/data_structure/static_range_count_distinct.test.py
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
