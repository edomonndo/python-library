---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/math/sum_of_floor_of_linear.test.py
    title: test/library_checker/math/sum_of_floor_of_linear.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def floor_sum(n: int, m: int, a: int, b: int) -> int:\n    \"\"\"\n    Sum\
    \ of (floor((A * i + B)/M) for i in range(N))\n    \"\"\"\n\n    res = 0\n   \
    \ while True:\n        if a >= m:\n            res += (n - 1) * n * (a // m) //\
    \ 2\n            a %= m\n        if b >= m:\n            res += n * (b // m)\n\
    \            b %= m\n        y_max = (a * n + b) // m\n        if y_max == 0:\n\
    \            break\n        x_max = b - y_max * m\n        res += (n + x_max //\
    \ a) * y_max\n        n, m, a, b = y_max, a, m, x_max % a\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: math_/floor_sum.py
  requiredBy: []
  timestamp: '2023-06-21 21:40:34+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/math/sum_of_floor_of_linear.test.py
documentation_of: math_/floor_sum.py
layout: document
title: Floor sum
---

### `floor_sum(N: int, M: int, A: int, B: int)`

以下の値を計算する。

$$\displaystyle\sum^{N-1}_{i=0} floor(\frac{Ai+B}{M})$$
