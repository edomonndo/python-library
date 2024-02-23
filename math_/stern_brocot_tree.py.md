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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from fractions import Fraction\n\n\ndef stern_brocot(p: int | Fraction, n:\
    \ int) -> tuple[int, int, int, int]:\n    \"\"\"\n    a/b <= \u221Ap <= c/d \u3092\
    \u6E80\u305F\u3059 a,b,c,d <= n \u3092\u6C42\u3081\u308B\n    \"\"\"\n    la =\
    \ rb = 0\n    lb = ra = 1\n    lu = ru = 1\n    a = d = 0\n    b = c = 1\n   \
    \ while lu or ru:\n        ma = la + ra\n        mb = lb + rb\n        if p *\
    \ mb**2 < ma**2:\n            ra = ma\n            rb = mb\n            if ma\
    \ <= n and mb <= n:\n                c = ma\n                d = mb\n        \
    \    else:\n                lu = 0\n        else:\n            la = ma\n     \
    \       lb = mb\n            if ma <= n and mb <= n:\n                a = ma\n\
    \                b = mb\n            else:\n                ru = 0\n    return\
    \ a, b, c, d\n"
  dependsOn: []
  isVerificationFile: false
  path: math_/stern_brocot_tree.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: math_/stern_brocot_tree.py
layout: document
title: Stern Brocot tree
---

https://tjkendev.github.io/procon-library/python/math/stern-brocot-tree.html