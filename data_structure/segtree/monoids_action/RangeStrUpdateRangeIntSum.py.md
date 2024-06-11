---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://atcoder.jp/contests/abl/tasks/abl_e
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://atcoder.jp/contests/abl/tasks/abl_e\n\nMOD = 998244353\n\npower10\
    \ = [1] * (200_001)\none = [0] * (200_001)\nfor i in range(200_000):\n    power10[i\
    \ + 1] = (power10[i] * 10) % MOD\n    one[i + 1] = (one[i] * 10 + 1) % MOD\n\n\
    \nclass S:\n    def __init__(self, value=0, size=0):\n        self.value = value\n\
    \        self.size = size\n\n    def __str__(self) -> str:\n        return f\"\
    ({self.value},{self.size})\"\n\n    __repr__ = __str__\n\n\nclass F:\n    def\
    \ __init__(self, digit=0):\n        self.digit = digit\n\n\ndef op(l: S, r: S)\
    \ -> S:\n    value = (l.value * power10[r.size] + r.value) % MOD\n    size = l.size\
    \ + r.size\n    return S(value, size)\n\n\ndef mapping(f: F, x: S) -> S:\n   \
    \ if f.digit == 0:\n        return x\n    value = f.digit * one[x.size] % MOD\n\
    \    return S(value, x.size)\n\n\ndef composition(f: F, g: F) -> F:\n    if f.digit\
    \ == 0:\n        return g\n    return f\n\n\n\"\"\"\nfrom data_structure.segtree.monoids_action.RangeStrUpdateRangeIntSum\
    \ import *\nfrom atcoder.lazysegtree import LazySegTree\n\nn, q = map(int, input().split())\n\
    seg = LazySegTree(op, S(), mapping, composition, F(), [S(1, 1) for _ in range(n)])\n\
    \nfor _ in range(q):\n    l, r, d = map(int, input().split())\n    seg.apply(l\
    \ - 1, r, F(d))\n    print(seg.all_prod().value)\n\"\"\"\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/segtree/monoids_action/RangeStrUpdateRangeIntSum.py
  requiredBy: []
  timestamp: '2024-06-11 17:27:30+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/segtree/monoids_action/RangeStrUpdateRangeIntSum.py
layout: document
redirect_from:
- /library/data_structure/segtree/monoids_action/RangeStrUpdateRangeIntSum.py
- /library/data_structure/segtree/monoids_action/RangeStrUpdateRangeIntSum.py.html
title: data_structure/segtree/monoids_action/RangeStrUpdateRangeIntSum.py
---
