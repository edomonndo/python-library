---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: polynomial/tayler_shift.py
    title: polynomial/tayler_shift.py
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
  code: "MOD = 998244353\n\n\nclass Comb:\n    def __init__(self, n: int):\n     \
    \   fact = [0] * (n + 1)\n        inv_fact = [0] * (n + 1)\n        inv = [0]\
    \ * (n + 1)\n        fact[0] = inv_fact[0] = inv[0] = 1\n        for i in range(1,\
    \ n + 1):\n            fact[i] = fact[i - 1] * i % MOD\n        inv_fact[n] =\
    \ pow(fact[n], -1, MOD)\n        inv[n] = inv_fact[-1] * fact[-2] % MOD\n    \
    \    for i in range(n - 1, 0, -1):\n            inv_fact[i] = inv_fact[i + 1]\
    \ * (i + 1) % MOD\n            inv[i] = inv_fact[i] * fact[i - 1] % MOD\n    \
    \    self.fact = fact\n        self.inv_fact = inv_fact\n        self.inv = inv\n\
    \n    def nCr(self, n: int, r: int) -> int:\n        if not 0 <= r <= n:\n   \
    \         return 0\n        return self.fact[n] * self.inv_fact[r] % MOD * self.inv_fact[n\
    \ - r] % MOD\n\n    def nPr(self, n: int, r: int) -> int:\n        if not 0 <=\
    \ r <= n:\n            return 0\n        return self.fact[n] * self.inv_fact[n\
    \ - r] % MOD\n\n    def nHr(self, n: int, r: int) -> int:\n        if n == 0 and\
    \ r == 0:\n            return 1\n        if n <= 0 or r < 0:\n            return\
    \ 0\n        return self.nCr(n + r - 1, r)\n\n    def pairCombination(self, n:\
    \ int) -> int:\n        \"\"\"combination of paris for n\"\"\"\n        if n %\
    \ 2:\n            return 1\n        return self.fact[n] * self.inv_fact[n >> 1]\
    \ // (2 ^ (n >> 1))\n\n    def move(self, r: int, c: int) -> int:\n        return\
    \ self.nCr(r + c, r)\n"
  dependsOn: []
  isVerificationFile: false
  path: enumerative_combinatorics/combination_mod.py
  requiredBy:
  - polynomial/tayler_shift.py
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: enumerative_combinatorics/combination_mod.py
layout: document
title: "\u4E8C\u9805\u4FC2\u6570(mod)"
---

### `combination_mod(n: int, r: int, m=10**9 + 7)`

$nCr\pmod m$を求める.

繰り返し計算が必要な場合は，Combクラスで前処理することでクエリに$O(1)$で答えられる．