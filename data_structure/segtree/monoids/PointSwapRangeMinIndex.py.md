---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/yukicoder/875_range_mindex_query.test.py
    title: No.875 Range Mindex Query
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "inf = float(\"inf\")\n\n\nclass S:\n    def __init__(self, value=inf, index=0):\n\
    \        self.value = value\n        self.index = index\n\n    def __lt__(self,\
    \ other: \"S\") -> bool:\n        if self.value < other.value:\n            return\
    \ True\n        elif self.value > other.value:\n            return False\n   \
    \     else:\n            return self.index < other.index\n\n\ndef op(l: S, r:\
    \ S) -> S:\n    if l < r:\n        return l\n    return r\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/segtree/monoids/PointSwapRangeMinIndex.py
  requiredBy: []
  timestamp: '2024-06-11 17:27:30+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/yukicoder/875_range_mindex_query.test.py
documentation_of: data_structure/segtree/monoids/PointSwapRangeMinIndex.py
layout: document
redirect_from:
- /library/data_structure/segtree/monoids/PointSwapRangeMinIndex.py
- /library/data_structure/segtree/monoids/PointSwapRangeMinIndex.py.html
title: data_structure/segtree/monoids/PointSwapRangeMinIndex.py
---
