---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: convolution/zeta_moebius_transform.py
    title: "\u30BC\u30FC\u30BF\u5909\u63DB\u30FB\u30E1\u30D3\u30A6\u30B9\u5909\u63DB"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
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
  timestamp: '2024-09-03 09:26:50+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/convolution/bitwise_and_convolution.test.py
layout: document
title: Bitwise And Convolution
---
