---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/math/min_of_linear.test.py
    title: test/library_checker/math/min_of_linear.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import math\n\n\ndef min_of_linear(L: int, R: int, a: int, b: int, mod: int)\
    \ -> tuple[int, int]:\n    \"\"\"\n    min((ax + b) % mod for x in range(L,R))\n\
    \    \"\"\"\n    n = R - L\n    b = (b + a * L) % mod\n    X, DX = _min_of_linear_segments(a,\
    \ b, mod)\n    x = 0\n    for i in range(len(X) - 1):\n        xl, xr = X[i],\
    \ X[i + 1]\n        if xr < n:\n            x = xr\n            continue\n   \
    \     x = xl + ((n - 1 - x) // DX[i]) * DX[i]\n        break\n    y = (a * x +\
    \ b) % mod\n    return L + x, y\n\n\ndef _min_of_linear_segments(a: int, b: int,\
    \ mod: int) -> tuple[list[int], list[int]]:\n    \"\"\"\n    `ax + b (x>=0)` \u304C\
    \u6700\u5C0F\u3068\u306A\u308B\u3068\u3053\u308D\u306E\u60C5\u5831\u3092\u8FD4\
    \u3059.\n    prefix min \u3092\u66F4\u65B0\u3059\u308B x \u5168\u4F53\u304C,\u7B49\
    \u5DEE\u6570\u5217\u306E\u548C\u96C6\u5408.\n\n    \u6B21\u3092\u8FD4\u3059:\n\
    \n    \u30FB\u7B49\u5DEE\u6570\u5217\u306E\u5883\u754C\u3068\u306A\u308B x_0,\
    \ x_1, ..., x_n\n    \u30FB\u5404\u5883\u754C\u306E\u9593\u3067\u306E\u4EA4\u5DEE\
    \ dx_0, ..., dx_{n-1}\n    \"\"\"\n    assert 0 <= a < mod\n    assert 0 <= b\
    \ < mod\n    X, DX = [0], []\n    g = math.gcd(a, mod)\n    a, b, mod = a // g,\
    \ b // g, mod // g\n    # p/q <= (mod-a)/mod <= r/s\n    p, q, r, s = 0, 1, 1,\
    \ 1\n    det_l, det_r = mod - a, a\n    x, y = 0, b\n\n    while y:\n        #\
    \ upd r/s\n        k = det_r // det_l\n        det_r %= det_l\n        if det_r\
    \ == 0:\n            k -= 1\n            det_r = det_l\n        r += k * p\n \
    \       s += k * q\n        while True:\n            k = math.ceil((det_l - y)\
    \ / det_r)\n            if k < 0:\n                k = 0\n            if det_l\
    \ - k * det_r <= 0:\n                break\n            det_l -= k * det_r\n \
    \           p += k * r\n            q += k * s\n            # p/q <= a/mod\n \
    \           # (aq - pmod) = det_l \u3092 y \u304B\u3089\u5F15\u304F\n        \
    \    k = y // det_l\n            y -= k * det_l\n            x += q * k\n    \
    \        X.append(x)\n            DX.append(q)\n        k = det_l // det_r\n \
    \       det_l -= k * det_r\n        p += k * r\n        q += k * s\n        #\
    \ assert min(p, q, r, s) >= 0\n    return X, DX\n"
  dependsOn: []
  isVerificationFile: false
  path: math_/min_of_linear.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/math/min_of_linear.test.py
documentation_of: math_/min_of_linear.py
layout: document
title: Min of linear
---

### `min_of_linear(L: int, R: int, A: int, B: int, M: int)`

以下の値を計算する.

$$\min(Ax+B\bmod M | L <= x < R )$$
