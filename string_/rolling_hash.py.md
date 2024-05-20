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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class RollingHash:\n    class FenwickTree:\n        def __init__(self, n:\
    \ int):\n            self.n = n\n            self.data = [0] * n\n\n        def\
    \ add(self, p: int, x: int):\n            assert 0 <= p < self.n, \"0<=p<n,p={0},n={1}\"\
    .format(p, self.n)\n            p += 1\n            while p <= self.n:\n     \
    \           self.data[p - 1] += x\n                p += p & -p\n\n        def\
    \ sum(self, l, r):\n            assert (\n                0 <= l and l <= r and\
    \ r <= self.n\n            ), \"0<=l<=r<=n,l={0},r={1},n={2}\".format(l, r, self.n)\n\
    \            return self.sum0(r) - self.sum0(l)\n\n        def sum0(self, r):\n\
    \            s = 0\n            while r > 0:\n                s += self.data[r\
    \ - 1]\n                r -= r & -r\n            return s\n\n    def __init__(\n\
    \        self,\n        s: list[int],\n        L: int = 2,\n        mods: tuple[int]\
    \ = (10**9 + 7, 10**9 + 9),\n        bases: tuple[int] = None,\n    ):\n     \
    \   if bases is None:\n            import random\n\n            bases = [random.randrange(2,\
    \ mod) for mod in mods]\n        self.n = n = len(s)\n        self.L = L\n   \
    \     self.mods = mods\n        self.power = [[1] * (n + 1) for _ in range(L)]\n\
    \        for i in range(L):\n            v = 1\n            for j in range(n):\n\
    \                v = v * bases[i] % mods[i]\n                self.power[i][j +\
    \ 1] = v\n\n        self.hashs = [self.FenwickTree(n) for _ in range(L)]\n   \
    \     self.values = [[0] * n for _ in range(L)]\n        for i in range(L):\n\
    \            for j in range(n):\n                v = self.power[i][j] * s[j] %\
    \ self.mods[i]\n                self.hashs[i].add(j, v)\n                self.values[i][j]\
    \ = v\n\n    def update(self, p: int, x: int):\n        for i in range(self.L):\n\
    \            v = self.power[i][p] * x % self.mods[i]\n            self.hashs[i].add(p,\
    \ (-self.values[i][p] + v) % self.mods[i])\n            self.values[i][p] = v\n\
    \n    def get(self, l: int, r: int) -> tuple[int]:\n        res = []\n       \
    \ for i in range(self.L):\n            res.append(self.hashs[i].sum(l, r) * self.power[i][-l\
    \ - 1] % self.mods[i])\n        return tuple(res)\n\n    def connect(self, h1:\
    \ int, h2: int, h2len: int) -> tuple[int]:\n        res = []\n        for i in\
    \ range(self.L):\n            res.append((h1 * self.power[i][h2len] + h2) % self.mods[i])\n\
    \        return tuple(res)\n\n    def lcp(self, l, r) -> int:\n        def _ok(length)\
    \ -> bool:\n            d = dict()\n            for i in range(self.n - length\
    \ + 1):\n                h = self.get(i, i + length)\n                if h in\
    \ d:\n                    if (i - d[h]) >= length:\n                        return\
    \ True\n                else:\n                    d[h] = i\n            return\
    \ False\n\n        while (r - l) > 1:\n            m = (r + l) >> 1\n        \
    \    if _ok(m):\n                l = m\n            else:\n                r =\
    \ m\n        return l\n"
  dependsOn: []
  isVerificationFile: false
  path: string_/rolling_hash.py
  requiredBy: []
  timestamp: '2024-01-05 12:48:48+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: string_/rolling_hash.py
layout: document
title: "\u30ED\u30FC\u30EA\u30F3\u30B0\u30CF\u30C3\u30B7\u30E5"
---

文字列を高速に検索する.

### RollingHash(list, mod, base)

文字列は整数(>0)に変換しておくこと．(例：`LIST = [ord(s)-ord("a")+1 for s in S]`)

baseの指定がない場合，2以上mod未満の値からランダムに選択する.

### update(p, x)

0-indexでp番目の値をxに変更する.

### get(l, r)

区間$[l,r)$のハッシュを取得する．