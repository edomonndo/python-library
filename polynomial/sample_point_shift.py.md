---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: convolution/convolution.py
    title: "\u7573\u307F\u8FBC\u307F $mod=998244353$"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/polynomial/shift_of_sampling_points_of_polynomial.test.py
    title: Shift of Sampling Points of Polynomial
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from convolution.convolution import *\n\n\ndef sample_point_shift(y: list[int],\
    \ t: int, m: int = -1) -> list[int]:\n    if m == -1:\n        m == len(y)\n \
    \   T = t\n    k = len(y) - 1\n    T %= MOD\n    if T <= k:\n        res = [0]\
    \ * m\n        ptr = 0\n        for i in range(T, k + 1):\n            res[ptr]\
    \ = y[i]\n            ptr += 1\n            if ptr == m:\n                break\n\
    \        if k + 1 < T + m:\n            suf = sample_point_shift(y, k + 1, m -\
    \ ptr)\n            for i in range(k + 1, T + m):\n                res[ptr] =\
    \ suf[i - k - 1]\n                ptr += 1\n        return res\n    if T + m >\
    \ MOD:\n        pref = sample_point_shift(y, T, MOD - T)\n        suf = sample_point_shift(y,\
    \ 0, m - len(pref))\n        return pref + suf\n\n    finv = [1] * (k + 1)\n \
    \   d = [0] * (k + 1)\n    tmp = 1\n    for i in range(2, k + 1):\n        tmp\
    \ = tmp * i % MOD\n    finv[-1] = tmp = pow(tmp, MOD - 2, MOD)\n    for i in range(k)[::-1]:\n\
    \        finv[i] = tmp = tmp * (i + 1) % MOD\n    for i, x in enumerate(y):\n\
    \        d[i] = (finv[i] * finv[k - i] % MOD) * x % MOD\n        if (k - i) &\
    \ 1:\n            d[i] = -d[i]\n\n    h = [0] * (m + k)\n    for i in range(m\
    \ + k):\n        h[i] = pow(T - k + i, MOD - 2, MOD)\n\n    dh = multiply(d, h)\n\
    \n    res = [0] * m\n    cur = T\n    for i in range(1, k + 1):\n        cur =\
    \ cur * (T - i) % MOD\n    for i in range(m):\n        res[i] = cur * dh[k + i]\
    \ % MOD\n        cur = (cur * (T + i + 1) % MOD) * h[i] % MOD\n    return res\n"
  dependsOn:
  - convolution/convolution.py
  isVerificationFile: false
  path: polynomial/sample_point_shift.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/polynomial/shift_of_sampling_points_of_polynomial.test.py
documentation_of: polynomial/sample_point_shift.py
layout: document
title: Sample Point Shift
---
