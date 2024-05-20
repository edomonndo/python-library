---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: convolution/cooley_turkey.py
    title: "\u7573\u307F\u8FBC\u307F \u30AB\u30E9\u30C4\u30D0\u6CD5"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/convolution_mod_1000000007
    links:
    - https://judge.yosupo.jp/problem/convolution_mod_1000000007
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/convolution_mod_1000000007


    from convolution.cooley_turkey import CooleyTukey


    N, M = map(int, input().split())

    A = list(map(int, input().split()))

    B = list(map(int, input().split()))


    C = CooleyTukey().karatsuba(A, B, 10**9 + 7)

    print(*C)

    '
  dependsOn:
  - convolution/cooley_turkey.py
  isVerificationFile: true
  path: test/library_checker/convolution/convolution_mod_1000000007.test.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/convolution/convolution_mod_1000000007.test.py
layout: document
redirect_from:
- /verify/test/library_checker/convolution/convolution_mod_1000000007.test.py
- /verify/test/library_checker/convolution/convolution_mod_1000000007.test.py.html
title: test/library_checker/convolution/convolution_mod_1000000007.test.py
---
