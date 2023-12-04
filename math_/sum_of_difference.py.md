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
  code: "def sum_of_difference(n, arr):\n    accum = [0]\n    for item in arr:\n \
    \       accum.append(accum[-1] + item)\n    res = accum[n] * n\n    for i, item\
    \ in enumerate(arr):\n        res -= accum[i] + (n - i) * item\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: math_/sum_of_difference.py
  requiredBy: []
  timestamp: '2023-12-04 22:53:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: math_/sum_of_difference.py
layout: document
title: Sum of difference
---

$$\displaystyle\sum^{N-1}_{i=0} \sum^{N-1}_{j=i+1} A_i - A_j \qquad (A_i < A_j)$$