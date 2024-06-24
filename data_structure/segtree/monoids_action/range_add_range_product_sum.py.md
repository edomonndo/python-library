---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/atcoder/abc300-399/abc357f.test.py
    title: F - Two Sequence Queries
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "MOD = 998244353\n\n\nclass S:\n    def __init__(self, a=0, b=0, ab=0, size=0):\n\
    \        self.a = a % MOD\n        self.b = b % MOD\n        self.ab = ab % MOD\n\
    \        self.size = size\n\n    def __str__(self) -> str:\n        return f\"\
    ({self.a},{self.b},{self.ab}{self.size})\"\n\n    __repr__ = __str__\n\n    def\
    \ __add__(self, other: \"S\"):\n        return __class__(\n            self.a\
    \ + other.a,\n            self.b + other.b,\n            self.ab + other.ab,\n\
    \            self.size + other.size,\n        )\n\n\nclass F:\n    def __init__(self,\
    \ a=0, b=0):\n        self.a = a % MOD\n        self.b = b % MOD\n\n    def __str__(self)\
    \ -> str:\n        return f\"({self.a},{self.b})\"\n\n    __repr__ = __str__\n\
    \n    def __add__(self, other: \"S\"):\n        return __class__(self.a + other.a,\
    \ self.b + other.b)\n\n\ndef op(l: S, r: S) -> S:\n    return l + r\n\n\ndef mapping(f:\
    \ F, x: S) -> S:\n    sz = x.size\n    a = x.a + f.a * sz % MOD\n    b = x.b +\
    \ f.b * sz % MOD\n    ab = x.ab + f.b * x.a % MOD + f.a * x.b % MOD + f.a * f.b\
    \ * sz % MOD\n    return S(a, b, ab, sz)\n\n\ndef composition(f: F, g: F) -> F:\n\
    \    return f + g\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/segtree/monoids_action/range_add_range_product_sum.py
  requiredBy: []
  timestamp: '2024-06-24 17:29:04+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/atcoder/abc300-399/abc357f.test.py
documentation_of: data_structure/segtree/monoids_action/range_add_range_product_sum.py
layout: document
title: "\u533A\u9593\u52A0\u7B97\u30FB\u533A\u9593\u7A4D\u548C"
---
