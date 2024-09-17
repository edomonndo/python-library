---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':grey_question:'
    path: test/atcoder/other/able.test.py
    title: E - Replace Digits
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "MOD = 998244353\n\npower10 = [1] * (200_001)\none = [0] * (200_001)\nfor\
    \ i in range(200_000):\n    power10[i + 1] = (power10[i] * 10) % MOD\n    one[i\
    \ + 1] = (one[i] * 10 + 1) % MOD\n\n\nclass S:\n    def __init__(self, value=0,\
    \ size=0):\n        self.value = value % MOD\n        self.size = size\n\n   \
    \ def __str__(self) -> str:\n        return f\"S({self.value},{self.size})\"\n\
    \n    __repr__ = __str__\n\n    def __add__(self, other: \"S\"):\n        return\
    \ __class__(\n            self.value * power10[other.size] + other.value,\n  \
    \          self.size + other.size,\n        )\n\n\nclass F:\n    def __init__(self,\
    \ digit=0):\n        self.digit = digit\n\n    def __str__(self) -> str:\n   \
    \     return f\"F({self.digit})\"\n\n    __repr__ = __str__\n\n\ndef op(l: S,\
    \ r: S) -> S:\n    return l + r\n\n\ndef mapping(f: F, x: S) -> S:\n    if f.digit\
    \ == 0:\n        return x\n    return S(f.digit * one[x.size], x.size)\n\n\ndef\
    \ composition(f: F, g: F) -> F:\n    if f.digit == 0:\n        return g\n    return\
    \ f\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/segtree/monoids_action/range_str_update_range_int_sum.py
  requiredBy: []
  timestamp: '2024-06-24 17:29:04+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith:
  - test/atcoder/other/able.test.py
documentation_of: data_structure/segtree/monoids_action/range_str_update_range_int_sum.py
layout: document
redirect_from:
- /library/data_structure/segtree/monoids_action/range_str_update_range_int_sum.py
- /library/data_structure/segtree/monoids_action/range_str_update_range_int_sum.py.html
title: data_structure/segtree/monoids_action/range_str_update_range_int_sum.py
---
