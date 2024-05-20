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
  code: "MOD = 10**9 + 7\n\n\nclass ModInt:\n    def __init__(self, x):\n        self.x\
    \ = x % MOD\n\n    def __str__(self):\n        return str(self.x)\n\n    __repr__\
    \ = __str__\n\n    def __add__(self, other):\n        return (\n            ModInt(self.x\
    \ + other.x)\n            if isinstance(other, ModInt)\n            else ModInt(self.x\
    \ + other)\n        )\n\n    def __sub__(self, other):\n        return (\n   \
    \         ModInt(self.x - other.x)\n            if isinstance(other, ModInt)\n\
    \            else ModInt(self.x - other)\n        )\n\n    def __mul__(self, other):\n\
    \        return (\n            ModInt(self.x * other.x)\n            if isinstance(other,\
    \ ModInt)\n            else ModInt(self.x * other)\n        )\n\n    def __truediv__(self,\
    \ other):\n        return (\n            ModInt(self.x * pow(other.x, -1, MOD))\n\
    \            if isinstance(other, ModInt)\n            else ModInt(self.x * pow(other,\
    \ -1, MOD))\n        )\n\n    def __pow__(self, other):\n        return (\n  \
    \          ModInt(pow(self.x, other.x, MOD))\n            if isinstance(other,\
    \ ModInt)\n            else ModInt(pow(self.x, other, MOD))\n        )\n\n   \
    \ __radd__ = __add__\n\n    def __rsub__(self, other):\n        return (\n   \
    \         ModInt(other.x - self.x)\n            if isinstance(other, ModInt)\n\
    \            else ModInt(other - self.x)\n        )\n\n    __rmul__ = __mul__\n\
    \n    def __rtruediv__(self, other):\n        return (\n            ModInt(other.x\
    \ * pow(self.x, -1, MOD))\n            if isinstance(other, ModInt)\n        \
    \    else ModInt(other * pow(self.x, -1, MOD))\n        )\n\n    def __rpow__(self,\
    \ other):\n        return (\n            ModInt(pow(other.x, self.x, MOD))\n \
    \           if isinstance(other, ModInt)\n            else ModInt(pow(other, self.x,\
    \ MOD))\n        )\n"
  dependsOn: []
  isVerificationFile: false
  path: utility/modint.py
  requiredBy: []
  timestamp: '2023-09-20 16:27:32+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: utility/modint.py
layout: document
title: modint
---

遅いのでコンテストでは非推奨．