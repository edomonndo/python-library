---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: convolution/convolution.py
    title: "\u7573\u307F\u8FBC\u307F $mod=998244353$"
  - icon: ':heavy_check_mark:'
    path: polynomial/formal_power_series.py
    title: "\u5F62\u5F0F\u7684\u51AA\u7D1A\u6570"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/polynomial/composition_inverse_of_formal_power_series.test.py
    title: Compositional Inverse of Formal Power Series
  - icon: ':heavy_check_mark:'
    path: test/library_checker/polynomial/composition_of_formal_power_series.test.py
    title: Composition of Formal Power Series
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from convolution.convolution import *\nfrom polynomial.formal_power_series\
    \ import FPS\n\n\ndef _composition_preprocess(b: list[int], k: int, deg: int)\
    \ -> list[int]:\n    X = [[] for _ in range(k + 1)]\n    X[0] = [1]\n    for i,\
    \ x in enumerate(X):\n        if i == k:\n            break\n        X[i + 1]\
    \ = multiply(x, b)[: deg + 1]\n    return X\n\n\ndef _composition_main(\n    X:\
    \ list[list[int]],\n    a: list[int],\n    sz_y: int,\n    xd: int,\n    d: int,\n\
    \    k: int,\n    deg: int,\n) -> None:\n    sz = len(a)\n    Z = [1]\n    F =\
    \ [0] * (deg + 1)\n    for i in range(k):\n        Y = [0] * sz_y\n        for\
    \ j, x_ in enumerate(X):\n            if i * d + j >= sz:\n                break\n\
    \            for t, x in enumerate(x_):\n                Y[t] += x * a[i * d +\
    \ j] % MOD\n        Y = multiply(Y, Z)[: deg + 1]\n        for j, y in enumerate(Y):\n\
    \            F[j] += y\n        Z = multiply(Z, xd)[: deg + 1]\n    F.pop()\n\
    \    return [x % MOD for x in F]\n\n\ndef composition(a: list[int], b: list[int])\
    \ -> list[int]:\n    deg = min(len(a), len(b))\n    k = int(deg**0.5 + 1)\n  \
    \  d = (deg + k) // k\n\n    X = _composition_preprocess(b, k, deg)\n    sz_y\
    \ = len(X[-1])\n    X[d + 1 :] = []\n    xd = X.pop()\n    return _composition_main(X,\
    \ a, sz_y, xd, d, k, deg)\n\n\ndef composition_multi(a_: list[list[int]], b: list[int],\
    \ deg: int) -> list[list[int]]:\n    k = int(deg**0.5 + 1)\n    d = (deg + k)\
    \ // k\n\n    X = _composition_preprocess(b, k, deg)\n    X[d + 1 :] = []\n  \
    \  xd = X.pop()\n    sz_y = len(X[-1])\n    return [_composition_main(X, a, sz_y,\
    \ xd, d, k, deg) for a in a_]\n\n\ndef composition_inverse(f: list[int], deg:\
    \ int = -1) -> list[int]:\n    if deg == -1:\n        deg = len(f)\n    dfdx =\
    \ FPS.fps_diff(f)\n    f = [-x for x in f]\n    res = [0]\n    m = 1\n    while\
    \ m < deg:\n        m <<= 1\n        cf0, cf1 = composition_multi([f, dfdx], res,\
    \ m)\n        cf0[1] += 1\n        tmp = multiply(cf0, FPS.inv(cf1, m))\n    \
    \    res[m >> 1 :] = tmp[m >> 1 : min(deg, m)]\n    return res\n"
  dependsOn:
  - convolution/convolution.py
  - polynomial/formal_power_series.py
  isVerificationFile: false
  path: polynomial/composition.py
  requiredBy: []
  timestamp: '2024-07-02 07:37:15+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/polynomial/composition_of_formal_power_series.test.py
  - test/library_checker/polynomial/composition_inverse_of_formal_power_series.test.py
documentation_of: polynomial/composition.py
layout: document
title: Composition
---
