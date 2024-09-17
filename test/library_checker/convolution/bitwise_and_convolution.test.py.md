---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: convolution/zeta_moebius_transform.py
    title: convolution/zeta_moebius_transform.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bitwise_and_convolution
    links:
    - https://judge.yosupo.jp/problem/bitwise_and_convolution
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution


    from convolution.zeta_moebius_transform import bitwize_and_conv



    n = int(input())

    A = [int(x) for x in input().split()]

    B = [int(x) for x in input().split()]

    bitwize_and_conv(A, B)

    print(*A)

    '
  dependsOn:
  - convolution/zeta_moebius_transform.py
  isVerificationFile: true
  path: test/library_checker/convolution/bitwise_and_convolution.test.py
  requiredBy: []
  timestamp: '2024-09-03 09:51:53+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/convolution/bitwise_and_convolution.test.py
layout: document
title: Bitwise And Convolution
---
