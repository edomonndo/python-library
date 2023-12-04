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
  code: "class RollingHash:\n    class FenwickTree:\n        def __init__(self, n:\
    \ int):\n            self.n = n\n            self.data = [0] * n\n\n        def\
    \ add(self, p: int, x: int):\n            assert 0 <= p < self.n, \"0<=p<n,p={0},n={1}\"\
    .format(p, self.n)\n            p += 1\n            while p <= self.n:\n     \
    \           self.data[p - 1] += x\n                p += p & -p\n\n        def\
    \ sum(self, l, r):\n            assert (\n                0 <= l and l <= r and\
    \ r <= self.n\n            ), \"0<=l<=r<=n,l={0},r={1},n={2}\".format(l, r, self.n)\n\
    \            return self.sum0(r) - self.sum0(l)\n\n        def sum0(self, r):\n\
    \            s = 0\n            while r > 0:\n                s += self.data[r\
    \ - 1]\n                r -= r & -r\n            return s\n\n    def __init__(self,\
    \ s: list[int], mod: int = 10**9 + 7, base: int = None):\n        if base is None:\n\
    \            import random\n\n            base = random.randrange(2, mod)\n  \
    \      n = len(s)\n        self.mod = mod\n        self.power = [1] * (n + 1)\n\
    \        v = 1\n        for i in range(n):\n            v = v * base % mod\n \
    \           self.power[i + 1] = v\n\n        self.hash = self.FenwickTree(n)\n\
    \        self.value = [0] * n\n        for i in range(n):\n            v = self.power[i]\
    \ * s[i] % self.mod\n            self.hash.add(i, v)\n            self.value[i]\
    \ = v\n\n    def update(self, p: int, x: int):\n        v = self.power[p] * x\
    \ % self.mod\n        self.hash.add(p, (-self.value[p] + v) % self.mod)\n    \
    \    self.value[p] = v\n\n    def get(self, l, r):\n        return self.hash.sum(l,\
    \ r) * self.power[-l - 1] % self.mod\n"
  dependsOn: []
  isVerificationFile: false
  path: string_/rolling_hash.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
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