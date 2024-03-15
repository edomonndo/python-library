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
  code: "class LiChaoTree:\n    def __init__(self, xs, inf=10**19):\n        \"\"\"\
    \u6700\u5C0F\u5024(\u6700\u5927\u5024)\u3092\u6C42\u3081\u308B\u9802\u70B9\u306E\
    \u6570\"\"\"\n        xs = sorted(set(xs))\n        self.inf = inf\n        self.size\
    \ = 1 << (len(xs) - 1).bit_length()\n        self.dat = [None] * (self.size *\
    \ 2)\n        self.xs = xs + [inf] * (self.size - len(xs))  # \u9577\u3055\u3092\
    \u63C3\u3048\u308B\n        self.idx = {num: id for id, num in enumerate(xs)}\n\
    \n    def _f(self, line, x):\n        \"\"\"line=(a,b),a*x+b\u3092\u8FD4\u3059\
    \"\"\"\n        a, b = line\n        return a * x + b\n\n    def _judge(self,\
    \ line1, line2, x):\n        \"\"\"\u5EA7\u6A19\u304Cx\u306E\u70B9\u3067line1\u306E\
    \u65B9\u304C\u5927\u304D\u3051\u308C\u3070True\u3092\u305D\u3046\u3067\u306A\u3044\
    \u306A\u3089False\u3092\u8FD4\u3059\"\"\"\n        return self._f(line1, x) >\
    \ self._f(line2, x)\n\n    def _add(self, line, idx, l, r):\n        while True:\n\
    \            if self.dat[idx] is None:\n                self.dat[idx] = line\n\
    \                return\n            m = (l + r) // 2\n            line_d = self.dat[idx]\n\
    \            lx, mx, rx = self.xs[l], self.xs[m], self.xs[r - 1]\n           \
    \ f_l = self._judge(line_d, line, lx)\n            f_m = self._judge(line_d, line,\
    \ mx)\n            f_r = self._judge(line_d, line, rx)\n            if f_l and\
    \ f_r:\n                self.dat[idx] = line\n                return\n       \
    \     if not f_l and not f_r:\n                return\n            if f_m:\n \
    \               line, self.dat[idx] = self.dat[idx], line\n            if f_l\
    \ != f_m:\n                r = m\n                idx *= 2\n            else:\n\
    \                l = m\n                idx = 2 * idx + 1\n\n    def add_line(self,\
    \ a, b):\n        \"\"\"ax+b\u306E\u76F4\u7DDA\u3092\u8FFD\u52A0\u3059\u308B\"\
    \"\"\n        self._add((a, b), 1, 0, self.size)\n\n    def add_segment(self,\
    \ a, b, l, r):\n        \"\"\"\u7DDA\u5206ax+b(l<=x<r)\u3092\u8FFD\u52A0\u3059\
    \u308B\"\"\"\n        line = (a, b)\n        lidx, ridx = self.idx[l] + self.size,\
    \ self.idx[r] + self.size\n        l, r = self.idx[l], self.idx[r]\n        size\
    \ = 1\n        while lidx < ridx:\n            if lidx & 1:\n                self._add(line,\
    \ lidx, l, l + size)\n                lidx += 1\n                l += size\n \
    \           if ridx & 1:\n                self._add(line, ridx, r, r + size)\n\
    \                ridx -= 1\n                r -= size\n                self._add(line,\
    \ ridx, r, r + size)\n            lidx >>= 1\n            ridx >>= 1\n       \
    \     size <<= 1\n\n    def query(self, x):\n        \"\"\"\u5EA7\u6A19x\u306B\
    \u304A\u3051\u308B\u76F4\u7DDA\u7FA4\u306E\u6700\u5C0F\u5024\u3092\u8FD4\u3059\
    \"\"\"\n        idx = self.idx[x] + self.size\n        ans = self.inf\n      \
    \  while idx > 0:\n            if self.dat[idx]:\n                ans = min(ans,\
    \ self._f(self.dat[idx], x))\n            idx >>= 1\n        return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/li_chao_tree.py
  requiredBy: []
  timestamp: '2023-09-16 18:27:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/li_chao_tree.py
layout: document
title: Li Chao Tree
---

直線集合に直線追加($ax+b$), 直線集合に対して$x$での最小値を求める．

### LCT = LiChaoTree(arr)

初期化．$arr$はクエリの配列(オフライン不可)．

### LCT.add_edge(a, b)

直線$ax+b$を追加する．

### LCT.query(x)

点$x$での最小値を求める．