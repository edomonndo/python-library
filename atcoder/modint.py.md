---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: atcoder/math.py
    title: atcoder/math.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: atcoder/convolution.py
    title: atcoder/convolution.py
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
  code: "from typing import Any\nfrom atcoder.math import _inv_gcd\n\n\nclass ModContext:\n\
    \    context: list[int] = []\n\n    def __init__(self, mod: int) -> None:\n  \
    \      assert 1 <= mod\n\n        self.mod = mod\n\n    def __enter__(self) ->\
    \ None:\n        self.context.append(self.mod)\n\n    def __exit__(self, exc_type:\
    \ Any, exc_value: Any, traceback: Any) -> None:\n        self.context.pop()\n\n\
    \    @classmethod\n    def get_mod(cls) -> int:\n        return cls.context[-1]\n\
    \n\nclass Modint:\n    def __init__(self, v: int = 0) -> None:\n        self._mod\
    \ = ModContext.get_mod()\n        if v == 0:\n            self._v = 0\n      \
    \  else:\n            self._v = v % self._mod\n\n    def mod(self) -> int:\n \
    \       return self._mod\n\n    def val(self) -> int:\n        return self._v\n\
    \n    def __iadd__(self, rhs: \"Modint\" | int) -> \"Modint\":\n        if isinstance(rhs,\
    \ Modint):\n            self._v += rhs._v\n        else:\n            self._v\
    \ += rhs\n        if self._v >= self._mod:\n            self._v -= self._mod\n\
    \        return self\n\n    def __isub__(self, rhs: \"Modint\" | int) -> \"Modint\"\
    :\n        if isinstance(rhs, Modint):\n            self._v -= rhs._v\n      \
    \  else:\n            self._v -= rhs\n        if self._v < 0:\n            self._v\
    \ += self._mod\n        return self\n\n    def __imul__(self, rhs: \"Modint\"\
    \ | int) -> \"Modint\":\n        if isinstance(rhs, Modint):\n            self._v\
    \ = self._v * rhs._v % self._mod\n        else:\n            self._v = self._v\
    \ * rhs % self._mod\n        return self\n\n    def __ifloordiv__(self, rhs: \"\
    Modint\" | int) -> \"Modint\":\n        if isinstance(rhs, Modint):\n        \
    \    inv = rhs.inv()._v\n        else:\n            inv = _inv_gcd(rhs, self._mod)[1]\n\
    \        self._v = self._v * inv % self._mod\n        return self\n\n    def __pos__(self)\
    \ -> \"Modint\":\n        return self\n\n    def __neg__(self) -> \"Modint\":\n\
    \        return Modint() - self\n\n    def __pow__(self, n: int) -> \"Modint\"\
    :\n        assert 0 <= n\n\n        return Modint(pow(self._v, n, self._mod))\n\
    \n    def inv(self) -> \"Modint\":\n        eg = _inv_gcd(self._v, self._mod)\n\
    \n        assert eg[0] == 1\n\n        return Modint(eg[1])\n\n    def __add__(self,\
    \ rhs: \"Modint\" | int) -> \"Modint\":\n        if isinstance(rhs, Modint):\n\
    \            result = self._v + rhs._v\n            if result >= self._mod:\n\
    \                result -= self._mod\n            return raw(result)\n       \
    \ else:\n            return Modint(self._v + rhs)\n\n    def __sub__(self, rhs:\
    \ \"Modint\" | int) -> \"Modint\":\n        if isinstance(rhs, Modint):\n    \
    \        result = self._v - rhs._v\n            if result < 0:\n             \
    \   result += self._mod\n            return raw(result)\n        else:\n     \
    \       return Modint(self._v - rhs)\n\n    def __mul__(self, rhs: \"Modint\"\
    \ | int) -> \"Modint\":\n        if isinstance(rhs, Modint):\n            return\
    \ Modint(self._v * rhs._v)\n        else:\n            return Modint(self._v *\
    \ rhs)\n\n    def __floordiv__(self, rhs: \"Modint\" | int) -> \"Modint\":\n \
    \       if isinstance(rhs, Modint):\n            inv = rhs.inv()._v\n        else:\n\
    \            inv = _inv_gcd(rhs, self._mod)[1]\n        return Modint(self._v\
    \ * inv)\n\n    def __eq__(self, rhs: \"Modint\" | int) -> bool:  # type: ignore\n\
    \        if isinstance(rhs, Modint):\n            return self._v == rhs._v\n \
    \       else:\n            return self._v == rhs\n\n    def __ne__(self, rhs:\
    \ \"Modint\" | int) -> bool:  # type: ignore\n        if isinstance(rhs, Modint):\n\
    \            return self._v != rhs._v\n        else:\n            return self._v\
    \ != rhs\n\n\ndef raw(v: int) -> Modint:\n    x = Modint()\n    x._v = v\n   \
    \ return x\n"
  dependsOn:
  - atcoder/math.py
  isVerificationFile: false
  path: atcoder/modint.py
  requiredBy:
  - atcoder/convolution.py
  timestamp: '2024-05-29 14:24:11+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: atcoder/modint.py
layout: document
redirect_from:
- /library/atcoder/modint.py
- /library/atcoder/modint.py.html
title: atcoder/modint.py
---
