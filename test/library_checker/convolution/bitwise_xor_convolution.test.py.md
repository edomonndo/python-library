---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: convolution/walsh_hadamard_tranform.py
    title: "\u30A6\u30A9\u30EB\u30B7\u30E5\u30A2\u30C0\u30DE\u30FC\u30EB\u5909\u63DB"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bitwise_xor_convolution
    links:
    - https://judge.yosupo.jp/problem/bitwise_xor_convolution
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_xor_convolution


    from convolution.walsh_hadamard_tranform import bitwise_xor_conv


    n = int(input())

    A = [int(x) for x in input().split()]

    B = [int(x) for x in input().split()]

    bitwise_xor_conv(A, B)

    print(*A)

    '
  dependsOn:
  - convolution/walsh_hadamard_tranform.py
  isVerificationFile: true
  path: test/library_checker/convolution/bitwise_xor_convolution.test.py
  requiredBy: []
  timestamp: '2024-09-03 09:26:50+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/convolution/bitwise_xor_convolution.test.py
layout: document
title: Bitwise Xor Convolution
---
