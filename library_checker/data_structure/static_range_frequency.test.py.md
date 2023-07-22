---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_range_frequency
    links:
    - https://judge.yosupo.jp/problem/static_range_frequency
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_frequency\n\
    \nfrom data_structure.wavelet_matrix import WaveletMatrix\n\nN, Q = map(int, input().split())\n\
    A = list(map(int, input().split()))\n\nWM = WaveletMatrix(A)\n\nfor _ in range(Q):\n\
    \    l, r, x = map(int, input().split())\n    print(WM.rangefreq(l, r, x, x +\
    \ 1))\n"
  dependsOn: []
  isVerificationFile: true
  path: library_checker/data_structure/static_range_frequency.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: library_checker/data_structure/static_range_frequency.test.py
layout: document
redirect_from:
- /verify/library_checker/data_structure/static_range_frequency.test.py
- /verify/library_checker/data_structure/static_range_frequency.test.py.html
title: library_checker/data_structure/static_range_frequency.test.py
---
