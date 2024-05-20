---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: atcoder/convolution.py
    title: atcoder/convolution.py
  - icon: ':warning:'
    path: atcoder/lazysegtree.py
    title: atcoder/lazysegtree.py
  - icon: ':warning:'
    path: atcoder/segtree.py
    title: atcoder/segtree.py
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
  code: "def _ceil_pow2(n: int) -> int:\n    x = 0\n    while (1 << x) < n:\n    \
    \    x += 1\n\n    return x\n\n\ndef _bsf(n: int) -> int:\n    x = 0\n    while\
    \ n % 2 == 0:\n        x += 1\n        n //= 2\n\n    return x\n"
  dependsOn: []
  isVerificationFile: false
  path: atcoder/_bit.py
  requiredBy:
  - atcoder/segtree.py
  - atcoder/lazysegtree.py
  - atcoder/convolution.py
  timestamp: '2024-02-05 08:23:41+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: atcoder/_bit.py
layout: document
redirect_from:
- /library/atcoder/_bit.py
- /library/atcoder/_bit.py.html
title: atcoder/_bit.py
---