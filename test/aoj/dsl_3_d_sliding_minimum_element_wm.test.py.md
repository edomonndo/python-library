---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_D
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_D\n\
    \nfrom data_structure.wavelet_matrix import WaveletMatrix\n\nN, L = map(int, input().split())\n\
    A = list(map(int, input().split()))\nWM = WaveletMatrix(A)\nans = []\nfor l in\
    \ range(N - L + 1):\n    ans.append(WM.quantile(l, l + L, 0))\nprint(*ans)\n"
  dependsOn: []
  isVerificationFile: true
  path: test/aoj/dsl_3_d_sliding_minimum_element_wm.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/dsl_3_d_sliding_minimum_element_wm.test.py
layout: document
redirect_from:
- /verify/test/aoj/dsl_3_d_sliding_minimum_element_wm.test.py
- /verify/test/aoj/dsl_3_d_sliding_minimum_element_wm.test.py.html
title: test/aoj/dsl_3_d_sliding_minimum_element_wm.test.py
---
