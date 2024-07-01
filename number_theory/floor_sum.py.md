---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/number_theory/sum_of_floor_of_linear.test.py
    title: test/library_checker/number_theory/sum_of_floor_of_linear.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def floor_sum(n: int, m: int, a: int, b: int) -> int:\n    res = 0\n    if\
    \ a < 0:\n        a2 = a % m\n        return floor_sum(n, m, a2, b) - n * (n -\
    \ 1) * ((a2 - a) // m) // 2\n    if b < 0:\n        b2 = b % m\n        return\
    \ floor_sum(n, m, a, b2) - n * ((b2 - b) // m)\n    if a >= m:\n        res +=\
    \ (n - 1) * n * (a // m) // 2\n        a %= m\n    if b >= m:\n        res +=\
    \ n * (b // m)\n        b %= m\n    y_max = (a * n + b) // m\n    x_max = y_max\
    \ * m - b\n    if y_max == 0:\n        return res\n    res += (n - (x_max + a\
    \ - 1) // a) * y_max\n    res += floor_sum(y_max, a, m, (a - x_max % a) % a)\n\
    \    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: number_theory/floor_sum.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/number_theory/sum_of_floor_of_linear.test.py
documentation_of: number_theory/floor_sum.py
layout: document
title: Floor sum
---

### `floor_sum(N: int, M: int, A: int, B: int)`

以下の値を計算する.

$$\displaystyle\sum^{N-1}_{i=0} floor(\frac{Ai+B}{M})$$
