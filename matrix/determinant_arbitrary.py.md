---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/matrix/determinant_of_matrix_arbitrary_mod.test.py
    title: test/library_checker/matrix/determinant_of_matrix_arbitrary_mod.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "MOD = 998244353\n\n\ndef determinant_arbitrary_mod(N, A, MOD):\n    res =\
    \ 1\n    for i in range(N):\n        for j in range(i + 1, N):\n            while\
    \ A[j][i]:\n                tmp = A[i][i] // A[j][i]\n                if tmp:\n\
    \                    for k in range(i, N):\n                        A[i][k] -=\
    \ tmp * A[j][k]\n                        A[i][k] %= MOD\n                A[i],\
    \ A[j] = A[j], A[i]\n                res *= -1\n                res %= MOD\n \
    \       res *= A[i][i]\n        res %= MOD\n        if not res:\n            break\n\
    \    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: matrix/determinant_arbitrary.py
  requiredBy: []
  timestamp: '2024-05-29 07:39:33+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/matrix/determinant_of_matrix_arbitrary_mod.test.py
documentation_of: matrix/determinant_arbitrary.py
layout: document
title: "\u884C\u5217\u5F0F"
---

### `determinant_arbitrary_mod(N, A, m=998244353)`

$N$行$N$列の正方行列$A$と非負整数$m$から行列式を$\mod m$で求める.

Aは正方行列を表す2次元配列
Aを破壊的変更することに注意