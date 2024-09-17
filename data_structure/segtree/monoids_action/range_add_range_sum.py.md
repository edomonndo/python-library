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
  code: "MOD = 998244353\n\n\nclass S:\n    def __init__(self, a=0, size=0):\n   \
    \     self.a = a % MOD\n        self.size = size\n\n    def __str__(self) -> str:\n\
    \        return f\"({self.a},{self.size})\"\n\n    __repr__ = __str__\n\n    def\
    \ __add__(self, other: \"S\"):\n        return __class__(\n            self.a\
    \ + other.a,\n            self.size + other.size,\n        )\n\n\nclass F:\n \
    \   def __init__(self, a=0):\n        self.a = a % MOD\n\n    def __str__(self)\
    \ -> str:\n        return f\"({self.a})\"\n\n    __repr__ = __str__\n\n    def\
    \ __add__(self, other: \"S\"):\n        return __class__(self.a + other.a)\n\n\
    \ndef op(l: S, r: S) -> S:\n    return l + r\n\n\ndef mapping(f: F, x: S) -> S:\n\
    \    return S(x.a + f.a * x.size, x.size)\n\n\ndef composition(f: F, g: F) ->\
    \ F:\n    return f + g\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/segtree/monoids_action/range_add_range_sum.py
  requiredBy: []
  timestamp: '2024-06-24 17:29:04+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/segtree/monoids_action/range_add_range_sum.py
layout: document
redirect_from:
- /library/data_structure/segtree/monoids_action/range_add_range_sum.py
- /library/data_structure/segtree/monoids_action/range_add_range_sum.py.html
title: data_structure/segtree/monoids_action/range_add_range_sum.py
---
