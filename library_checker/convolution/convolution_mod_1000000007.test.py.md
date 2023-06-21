---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: convolution/cooley_turkey.py
    title: convolution/cooley_turkey.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/convolution_mod_1000000007
    links:
    - https://judge.yosupo.jp/problem/convolution_mod_1000000007
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
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
  path: library_checker/convolution/convolution_mod_1000000007.test.py
  requiredBy: []
  timestamp: '2023-06-21 08:58:45+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: library_checker/convolution/convolution_mod_1000000007.test.py
layout: document
redirect_from:
- /verify/library_checker/convolution/convolution_mod_1000000007.test.py
- /verify/library_checker/convolution/convolution_mod_1000000007.test.py.html
title: library_checker/convolution/convolution_mod_1000000007.test.py
---
