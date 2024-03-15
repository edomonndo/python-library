---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/wavelet_matrix.py
    title: "\u30A6\u30A7\u30FC\u30D6\u30EC\u30C3\u30C8\u884C\u5217"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_range_frequency
    links:
    - https://judge.yosupo.jp/problem/static_range_frequency
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_frequency\n\
    \nfrom data_structure.wavelet_matrix import WaveletMatrix\n\nN, Q = map(int, input().split())\n\
    A = list(map(int, input().split()))\n\nWM = WaveletMatrix(A)\n\nfor _ in range(Q):\n\
    \    l, r, x = map(int, input().split())\n    print(WM.rangefreq(l, r, x, x +\
    \ 1))\n"
  dependsOn:
  - data_structure/wavelet_matrix.py
  isVerificationFile: true
  path: test/library_checker/data_structure/static_range_frequency.test.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/static_range_frequency.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/static_range_frequency.test.py
- /verify/test/library_checker/data_structure/static_range_frequency.test.py.html
title: test/library_checker/data_structure/static_range_frequency.test.py
---
