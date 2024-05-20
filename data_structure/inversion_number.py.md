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
  code: "def inversion(A):\n    def _add(i, x, bit):\n        while i <= n:\n    \
    \        bit[i] += x\n            i += i & -i\n\n    def _sum(i, bit):\n     \
    \   total = 0\n        while i > 0:\n            total += bit[i]\n           \
    \ i -= i & -i\n        return total\n\n    n = len(A)\n    bit = [0] * (n + 1)\n\
    \    A = list(map({e: i for i, e in enumerate(sorted(set(A)), 1)}.__getitem__,\
    \ A))\n\n    ans = 0\n    for i, a in enumerate(A):\n        ans += i - _sum(a,\
    \ bit)\n        _add(a, 1, bit)\n    return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/inversion_number.py
  requiredBy: []
  timestamp: '2024-01-05 12:48:48+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/inversion_number.py
layout: document
title: "\u8EE2\u7F6E\u6570"
---
