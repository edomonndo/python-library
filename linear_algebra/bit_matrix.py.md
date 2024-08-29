---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: utility/bitset.py
    title: Bitset
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/linear_algebra/matrix_determinant_mod2.test.py
    title: test/library_checker/linear_algebra/matrix_determinant_mod2.test.py
  - icon: ':x:'
    path: test/library_checker/linear_algebra/matrix_inverse_mod2.test.py
    title: test/library_checker/linear_algebra/matrix_inverse_mod2.test.py
  - icon: ':x:'
    path: test/library_checker/linear_algebra/matrix_product_mod2.test.py
    title: test/library_checker/linear_algebra/matrix_product_mod2.test.py
  - icon: ':x:'
    path: test/library_checker/linear_algebra/matrix_rank_mod2.test.py
    title: Rank of Matrix (Mod 2)
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Optional\n\nfrom utility.bitset import BitSet\n\n\nclass\
    \ BitMatrix:\n    def __init__(self, n: int, m: int):\n        self.n = n\n  \
    \      self.m = m\n        self.flip = False\n        if n > m:\n            self.flip\
    \ = True\n            n, m = m, n\n        self.bss = [BitSet(m) for _ in range(n)]\n\
    \n    def __getitem__(self, idx: int) -> BitSet:\n        return self.bss[idx]\n\
    \n    @staticmethod\n    def from_input(n: int, m: int) -> \"BitMatrix\":\n  \
    \      res = BitMatrix(n, m)\n        for i in range(n):\n            row = input()\n\
    \            # assert len(row) == m\n            for j, c in enumerate(row):\n\
    \                if c == \"1\":\n                    res.set(i, j, 1)\n      \
    \  return res\n\n    @staticmethod\n    def from_str(s: list[str]) -> \"BitMatrix\"\
    :\n        n = len(s)\n        m = len(s[0])\n        res = BitMatrix(n, m)\n\
    \        for i in range(n):\n            for j, c in enumerate(s[i]):\n      \
    \          if c == \"1\":\n                    res.set(i, j, 1)\n        return\
    \ res\n\n    def copy(self) -> \"BitMatrix\":\n        res = BitMatrix(0, 0)\n\
    \        res.n, res.m, res.flip = self.n, self.m, self.flip\n        res.bss =\
    \ [bs.copy() for bs in self.bss]\n        return res\n\n    def tostr(self) ->\
    \ str:\n        res = []\n        for row in self.bss:\n            res.append(row.tostr())\n\
    \        return \"\\n\".join(res)\n\n    def set(self, i: int, j: int, x: int)\
    \ -> None:\n        # assert x == 0 or x == 1\n        if self.flip:\n       \
    \     i, j = j, i\n        # assert 0 <= i < self.n\n        # assert 0 <= j <\
    \ self.m\n        self.bss[i][j] = x\n\n    def get(self, i: int, j: int) -> int:\n\
    \        if self.flip:\n            i, j = j, i\n        # assert 0 <= i < self.n\n\
    \        # assert 0 <= j < self.m\n        return self.bss[i][j]\n\n    def transpose(self,\
    \ do_flip: bool = True) -> \"BitMatrix\":\n        if do_flip:\n            res\
    \ = BitMatrix(self.m, self.n)\n            for i in range(self.n):\n         \
    \       for j in range(self.m):\n                    if self.get(i, j):\n    \
    \                    res.set(j, i, 1)\n            return res\n        else:\n\
    \            bss = [BitSet(self.n) for _ in range(self.m)]\n            for i\
    \ in range(self.n):\n                for j in range(self.m):\n               \
    \     if self.get(i, j):\n                        bss[j][i] = 1\n            res\
    \ = BitMatrix(0, 0)\n            res.n, res.m, res.flip, res.bss = self.m, self.n,\
    \ False, bss\n            return res\n\n    def __mul__(self, other: \"BitMatrix\"\
    ) -> \"BitMatrix\":\n        assert self.m == other.n\n        n, k = self.n,\
    \ other.m\n        res = BitMatrix(0, 0)\n        res.n, res.m, res.flip = self.n,\
    \ other.m, False\n        bss = [BitSet(k) for _ in range(n)]\n        if other.flip:\n\
    \            other = other.transpose(False)\n            # assert other.flip =\
    \ False\n        for i in range(self.n):\n            for j in range(self.m):\n\
    \                if self.get(i, j):\n                    bss[i] ^= other[j]\n\
    \        res.bss = bss\n        return res\n\n    def rank(self):\n        if\
    \ self.n == 0 or self.m == 0:\n            return 0\n        n, m = self.n, self.m\n\
    \        if self.flip:\n            n, m = m, n\n        nonzero = []\n      \
    \  lead = []\n        for i in range(n):\n            ai = self.bss[i].copy()\n\
    \            for aj, z in zip(nonzero, lead):\n                if ai[z]:\n   \
    \                 ai ^= aj\n            bj = -1\n            for j in range(m):\n\
    \                if ai[j]:\n                    bj = j\n                    break\n\
    \            if bj >= 0:\n                nonzero.append(ai.copy())\n        \
    \        lead.append(bj)\n        return len(nonzero)\n\n    def det(self) ->\
    \ int:\n        assert self.n == self.m\n        assert self.flip == False\n \
    \       n, bss = self.n, [bs.copy() for bs in self.bss]\n        lead = [0] *\
    \ n\n        for i in range(n):\n            for j in range(i):\n            \
    \    if bss[i][lead[j]]:\n                    bss[i].xor_hint(bss[j], lead[j])\n\
    \            lead[i] = bss[i].ctz()\n            if lead[i] == n:\n          \
    \      return 0\n        return 1\n\n    def inv(self) -> Optional[\"BitMatrix\"\
    ]:\n        assert self.n == self.m\n        assert self.flip == False\n     \
    \   n = self.n\n        bss = [BitSet(n << 1) for _ in range(n)]\n        for\
    \ i in range(n):\n            for j in range(n):\n                if self.get(i,\
    \ j):\n                    bss[i][j] = 1\n        lead = [0] * n\n        for\
    \ i in range(n):\n            bss[i][n + i] = 1\n            for j in range(i):\n\
    \                if bss[i][lead[j]]:\n                    bss[i].xor_hint(bss[j],\
    \ lead[j])\n            lead[i] = bss[i].ctz()\n            if lead[i] >= n:\n\
    \                return None\n            for j in range(i):\n               \
    \ if bss[j][lead[i]]:\n                    bss[j].xor_hint(bss[i], lead[i])\n\
    \        res = BitMatrix(n, n)\n        for i in range(n):\n            while\
    \ lead[i] != i:\n                bss[i], bss[lead[i]] = bss[lead[i]], bss[i]\n\
    \                lead[i], lead[lead[i]] = lead[lead[i]], lead[i]\n           \
    \ for j in range(n):\n                if bss[i][j + n]:\n                    res.set(i,\
    \ j, 1)\n        return res\n"
  dependsOn:
  - utility/bitset.py
  isVerificationFile: false
  path: linear_algebra/bit_matrix.py
  requiredBy: []
  timestamp: '2024-08-29 23:59:34+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/library_checker/linear_algebra/matrix_determinant_mod2.test.py
  - test/library_checker/linear_algebra/matrix_product_mod2.test.py
  - test/library_checker/linear_algebra/matrix_inverse_mod2.test.py
  - test/library_checker/linear_algebra/matrix_rank_mod2.test.py
documentation_of: linear_algebra/bit_matrix.py
layout: document
redirect_from:
- /library/linear_algebra/bit_matrix.py
- /library/linear_algebra/bit_matrix.py.html
title: linear_algebra/bit_matrix.py
---
