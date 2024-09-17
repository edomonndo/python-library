---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/wavelet_matrix.py
    title: data_structure/wavelet_matrix.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_range_count_distinct
    links:
    - https://judge.yosupo.jp/problem/static_range_count_distinct
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_count_distinct\n\
    \nfrom data_structure.wavelet_matrix import WaveletMatrix\nfrom collections import\
    \ Counter\n\n\ndef compress_tolist(arr):\n    # 0-index\n    return list(map({e:\
    \ i for i, e in enumerate(sorted(set(arr)), 0)}.__getitem__, arr))\n\n\nN, Q =\
    \ map(int, input().split())\nA = [int(x) for x in input().split()]\nA = compress_tolist(A)\n\
    B = Counter()\nfor i, a in enumerate(A):\n    A[i] = B[a]\n    B[a] = i + 1\n\n\
    WM = WaveletMatrix(A)\nfor _ in range(Q):\n    l, r = map(int, input().split())\n\
    \    print(WM.rangefreq_to(l, r, l + 1))\n"
  dependsOn:
  - data_structure/wavelet_matrix.py
  isVerificationFile: true
  path: test/library_checker/data_structure/static_range_count_distinct.test.py
  requiredBy: []
  timestamp: '2024-08-29 22:20:26+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/static_range_count_distinct.test.py
layout: document
title: Static Range Count Distinct
---
