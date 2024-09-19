---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: number_theory/count_squarefree.py
    title: "\u7121\u5E73\u65B9\u6570\u306E\u6570\u3048\u4E0A\u3052"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/number_theory/kth_root_integer.test.py
    title: Kth Root (Integer)
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class KthRoot:\n\n    @staticmethod\n    def floor(real: int, k: int) ->\
    \ int:\n        # assert k != 0\n        if real <= 1 or k == 1:\n           \
    \ return real\n        if k >= 64:\n            return 1\n\n        def check(a:\
    \ int, k: int) -> bool:\n            res = 1\n            while k:\n         \
    \       if k & 1:\n                    res *= a\n                    if res >\
    \ real:\n                        return False\n                k >>= 1\n     \
    \           a *= a\n            return res <= real\n\n        res = int(pow(real,\
    \ 1 / k))\n        while not check(res, k):\n            res -= 1\n        while\
    \ check(res + 1, k):\n            res += 1\n        return res\n\n    @classmethod\n\
    \    def ceil(cls, real: int, k: int) -> int:\n        if real <= 1 or k == 1:\n\
    \            return real\n        if k >= 64:\n            return 2\n        res\
    \ = cls.floor(real, k)\n        x, a = 1, res\n        while k:\n            if\
    \ k & 1:\n                x *= a\n            k >>= 1\n            a *= a\n  \
    \      if x != real:\n            res += 1\n        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: number_theory/kth_root.py
  requiredBy:
  - number_theory/count_squarefree.py
  timestamp: '2024-08-22 11:33:17+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/number_theory/kth_root_integer.test.py
documentation_of: number_theory/kth_root.py
layout: document
title: Kth Root
---
