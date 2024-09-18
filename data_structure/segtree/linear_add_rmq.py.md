---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: utility/bit.py
    title: utility/bit.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library_checker/data_structure/range_linear_add_range_min.test.py
    title: Range Linear Add Range Min
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import TypeVar\n\nT = TypeVar(\"T\")\n\nfrom utility.bit import\
    \ Bit32\n\n\nclass LinearAddRmQ:\n\n    class Node:\n        def __init__(self,\
    \ x: int = 0, y: T = 0):\n            self.lza = self.lzb = 0\n            self.lbrx\
    \ = self.rbrx = x\n            self.lbry = self.rbry = y\n\n        def __repr__(self):\n\
    \            return f\"Node<({self.lza},{self.lzb}),({self.lbrx},{self.lbry}),({self.rbrx},{self.rbry})>\"\
    \n\n    def __init__(self, V: list[T]):\n        self.n = len(V)\n        self.op\
    \ = min\n        self.e = float(\"inf\")\n        self.log = (self.n - 1).bit_length()\n\
    \        self.size = 1 << self.log\n        self.correct = [1] * (self.size <<\
    \ 1)\n        self.d = [self.Node() for _ in range(self.size << 1)]\n        for\
    \ i in range(self.n):\n            self.d[self.size + i] = self.Node(i, V[i])\n\
    \        for i in range(self.n, self.size):\n            self.d[self.size + i]\
    \ = self.Node(i, 0)\n        for i in range(self.size - 1, 0, -1):\n         \
    \   self._update(i)\n\n    @staticmethod\n    def _cross(ax: int, ay: T, bx: int,\
    \ by: T, cx: int, cy: T) -> T:\n        return (by - ay) * (cx - ax) - (cy - ay)\
    \ * (bx - ax)\n\n    def set(self, p: int, x: T) -> None:\n        assert 0 <=\
    \ p and p < self.n\n        p_orgin = p\n        p += self.size\n        for i\
    \ in range(self.log, 0, -1):\n            self._push(p >> i)\n        if self.d[p].lbry\
    \ == x:\n            return\n        is_decrease = self.d[p].lbry > x\n      \
    \  self.d[p] = self.Node(p_orgin, x)\n        for i in range(1, self.log + 1):\n\
    \            if (\n                is_decrease\n                or self.d[p >>\
    \ i].lbrx == p_orgin\n                or self.d[p >> i].rbrx == p_orgin\n    \
    \        ):\n                self._update(p >> i)\n\n    def get(self, p: int)\
    \ -> T:\n        assert 0 <= p and p < self.n\n        p += self.size\n      \
    \  nd = self.d[p]\n        a = nd.lza * self.log\n        b = nd.lzb * self.log\n\
    \        return nd.lbry + (p - self.size) * a + b\n\n    def prod(self, l: int,\
    \ r: int) -> T:\n        assert 0 <= l and l <= r and r <= self.n\n        if\
    \ l == r:\n            return self.e\n        l += self.size\n        r += self.size\n\
    \        for i in range(self.log, 0, -1):\n            if ((l >> i) << i) != l:\n\
    \                self._push(l >> i)\n            if ((r >> i) << i) != r:\n  \
    \              self._push((r - 1) >> i)\n        res = self.e\n        while l\
    \ < r:\n            if l & 1:\n                res = self.op(res, self._min_subtree(l))\n\
    \                l += 1\n            if r & 1:\n                r -= 1\n     \
    \           res = self.op(self._min_subtree(r), res)\n            l >>= 1\n  \
    \          r >>= 1\n        return res\n\n    def apply(self, l: int, r: int,\
    \ a: T, b: T) -> None:\n        assert 0 <= l and l <= r and r <= self.n\n   \
    \     if l == r:\n            return\n        l += self.size\n        r += self.size\n\
    \        l2, r2 = l, r\n        while l < r:\n            if l & 1:\n        \
    \        self._all_apply(l, a, b)\n                l += 1\n            if r &\
    \ 1:\n                r -= 1\n                self._all_apply(r, a, b)\n     \
    \       l >>= 1\n            r >>= 1\n        l, r = l2, r2\n        for i in\
    \ range(1, self.log + 1):\n            if ((l >> i) << i) != l:\n            \
    \    self.correct[l >> i] = 0\n            if ((r >> i) << i) != r:\n        \
    \        self.correct[(r - 1) >> i] = 0\n\n    def _leftmost(self, k: int) ->\
    \ int:\n        msb = 31 - Bit32.clz(k)\n        return (k - (1 << msb)) << (self.log\
    \ - msb)\n\n    def _update(self, k: int) -> None:\n        # assert 0 <= k <\
    \ self.size\n        correct, d, size = self.correct, self.d, self.size\n    \
    \    self._push(k)\n        l, r = k << 1, (k << 1) + 1\n        if not correct[l]:\n\
    \            self._update(l)\n        if not correct[r]:\n            self._update(r)\n\
    \        splitx = self._leftmost(r)\n        lza = lzb = lzA = lzB = 0\n     \
    \   ax, ay = d[l].lbrx, d[l].lbry\n        bx, by = d[l].rbrx, d[l].rbry\n   \
    \     cx, cy = d[r].lbrx, d[r].lbry\n        dx, dy = d[r].rbrx, d[r].rbry\n\n\
    \        def movel(f: int):\n            nonlocal lza, lzb, l, ax, ay, bx, by\n\
    \            lza += d[l].lza\n            lzb += d[l].lzb\n            l = (l\
    \ << 1) + f\n            ax, ay = d[l].lbrx, d[l].lbry\n            bx, by = d[l].rbrx,\
    \ d[l].rbry\n            ay += lza * ax + lzb\n            by += lza * bx + lzb\n\
    \n        def mover(f: int):\n            nonlocal lzA, lzB, r, cx, cy, dx, dy\n\
    \            lzA += d[r].lza\n            lzB += d[r].lzb\n            r = (r\
    \ << 1) + f\n            cx, cy = d[r].lbrx, d[r].lbry\n            dx, dy = d[r].rbrx,\
    \ d[r].rbry\n            cy += lzA * cx + lzB\n            dy += lzA * dx + lzB\n\
    \n        while l < size or r < size:\n            s1 = self._cross(ax, ay, bx,\
    \ by, cx, cy)\n            if l < size and s1 > 0:\n                movel(0)\n\
    \            elif r < size and self._cross(bx, by, cx, cy, dx, dy) > 0:\n    \
    \            mover(1)\n            elif l >= size:\n                mover(0)\n\
    \            elif r >= size:\n                movel(1)\n            else:\n  \
    \              s2 = self._cross(bx, by, ax, ay, dx, dy)\n                if s1\
    \ + s2 == 0 or s1 * (dx - splitx) < s2 * (splitx - cx):\n                    movel(1)\n\
    \                else:\n                    mover(0)\n        d[k].lbrx, d[k].lbry\
    \ = ax, ay\n        d[k].rbrx, d[k].rbry = cx, cy\n        correct[k] = 1\n\n\
    \    def _all_apply(self, k: int, a: T, b: T) -> None:\n        nd = self.d[k]\n\
    \        nd.lbry += a * nd.lbrx + b\n        nd.rbry += a * nd.rbrx + b\n    \
    \    if k < self.size:\n            nd.lza += a\n            nd.lzb += b\n\n \
    \   def _push(self, k: int) -> None:\n        nd = self.d[k]\n        self._all_apply(k\
    \ << 1, nd.lza, nd.lzb)\n        self._all_apply((k << 1) + 1, nd.lza, nd.lzb)\n\
    \        nd.lza = nd.lzb = 0\n\n    def _min_subtree(self, k: int, a: T = 0, b:\
    \ T = 0) -> T:\n        d = self.d\n        if not self.correct[k]:\n        \
    \    self._update(k)\n        while k < self.size:\n            f = (d[k].lbry\
    \ - d[k].rbry) > a * (d[k].rbrx - d[k].lbrx)\n            a += d[k].lza\n    \
    \        b += d[k].lzb\n            k = (k << 1) + f\n        return d[k].lbry\
    \ + a * d[k].lbrx + b\n"
  dependsOn:
  - utility/bit.py
  isVerificationFile: false
  path: data_structure/segtree/linear_add_rmq.py
  requiredBy: []
  timestamp: '2024-09-18 10:00:08+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/library_checker/data_structure/range_linear_add_range_min.test.py
documentation_of: data_structure/segtree/linear_add_rmq.py
layout: document
redirect_from:
- /library/data_structure/segtree/linear_add_rmq.py
- /library/data_structure/segtree/linear_add_rmq.py.html
title: data_structure/segtree/linear_add_rmq.py
---
