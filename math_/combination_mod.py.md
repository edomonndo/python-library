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
  code: "def combination_mod(n: int, r: int, mod=10**9 + 7) -> int:\n    num = 1\n\
    \    denom = 1\n    for i in range(r):\n        num = (num * (n - i)) % mod\n\
    \        denom = (denom * (r - i)) % mod\n\n    return num * pow(denom, mod -\
    \ 2, mod)\n\n\nclass Comb:\n    def __init__(self, H: int, W: int, MOD=10**9 +\
    \ 7):\n        fact = [1] * (H + W)\n        for i in range(1, H + W):\n     \
    \       fact[i] = fact[i - 1] * i % MOD\n        inv_fact = [1] * (H + W)\n  \
    \      inv_fact[H + W - 1] = pow(fact[H + W - 1], -1, MOD)\n        for i in range(H\
    \ + W - 2, -1, -1):\n            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD\n\
    \        self.fact = fact\n        self.inv_fact = inv_fact\n        self.MOD\
    \ = MOD\n\n    def nCr(self, n: int, r: int) -> int:\n        return (\n     \
    \       self.fact[n] * self.inv_fact[r] % self.MOD * self.inv_fact[n - r] % self.MOD\n\
    \        )\n\n    def move(self, r: int, c: int):\n        return self.nCr(r +\
    \ c, r)\n"
  dependsOn: []
  isVerificationFile: false
  path: math_/combination_mod.py
  requiredBy: []
  timestamp: '2023-12-04 22:53:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: math_/combination_mod.py
layout: document
title: "\u4E8C\u9805\u4FC2\u6570(mod)"
---

### `combination_mod(n: int, r: int, m=10**9 + 7)`

$nCr\pmod m$を求める.

繰り返し計算が必要な場合は，Combクラスで前処理することでクエリに$O(1)$で答えられる．