---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: polynomial/chirp_z.py
    title: Chirp Z
  - icon: ':heavy_check_mark:'
    path: polynomial/composition.py
    title: Composition
  - icon: ':heavy_check_mark:'
    path: polynomial/formal_power_series.py
    title: "\u5F62\u5F0F\u7684\u51AA\u7D1A\u6570"
  - icon: ':heavy_check_mark:'
    path: polynomial/multipoint_evaluation.py
    title: Multipoint Evaluation
  - icon: ':warning:'
    path: polynomial/multivariate_multiplication.py
    title: Multivariate Multiplication
  - icon: ':heavy_check_mark:'
    path: polynomial/product_tree.py
    title: Product Tree
  - icon: ':heavy_check_mark:'
    path: polynomial/sample_point_shift.py
    title: Sample Point Shift
  - icon: ':heavy_check_mark:'
    path: polynomial/tayler_shift.py
    title: Tayler Shift
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/convolution/convolution_mod.test.py
    title: Convolution Mod
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "MOD = 998244353\n_IMAG = 911660635\n_IIMAG = 86583718\n_rate2 = (\n    0,\n\
    \    911660635,\n    509520358,\n    369330050,\n    332049552,\n    983190778,\n\
    \    123842337,\n    238493703,\n    975955924,\n    603855026,\n    856644456,\n\
    \    131300601,\n    842657263,\n    730768835,\n    942482514,\n    806263778,\n\
    \    151565301,\n    510815449,\n    503497456,\n    743006876,\n    741047443,\n\
    \    56250497,\n    867605899,\n    0,\n)\n_irate2 = (\n    0,\n    86583718,\n\
    \    372528824,\n    373294451,\n    645684063,\n    112220581,\n    692852209,\n\
    \    155456985,\n    797128860,\n    90816748,\n    860285882,\n    927414960,\n\
    \    354738543,\n    109331171,\n    293255632,\n    535113200,\n    308540755,\n\
    \    121186627,\n    608385704,\n    438932459,\n    359477183,\n    824071951,\n\
    \    103369235,\n    0,\n)\n_rate3 = (\n    0,\n    372528824,\n    337190230,\n\
    \    454590761,\n    816400692,\n    578227951,\n    180142363,\n    83780245,\n\
    \    6597683,\n    70046822,\n    623238099,\n    183021267,\n    402682409,\n\
    \    631680428,\n    344509872,\n    689220186,\n    365017329,\n    774342554,\n\
    \    729444058,\n    102986190,\n    128751033,\n    395565204,\n    0,\n)\n_irate3\
    \ = (\n    0,\n    509520358,\n    929031873,\n    170256584,\n    839780419,\n\
    \    282974284,\n    395914482,\n    444904435,\n    72135471,\n    638914820,\n\
    \    66769500,\n    771127074,\n    985925487,\n    262319669,\n    262341272,\n\
    \    625870173,\n    768022760,\n    859816005,\n    914661783,\n    430819711,\n\
    \    272774365,\n    530924681,\n    0,\n)\n\n\ndef _fft(a):\n    n = len(a)\n\
    \    h = (n - 1).bit_length()\n    le = 0\n    for le in range(0, h - 1, 2):\n\
    \        p = 1 << (h - le - 2)\n        rot = 1\n        for s in range(1 << le):\n\
    \            rot2 = rot * rot % MOD\n            rot3 = rot2 * rot % MOD\n   \
    \         offset = s << (h - le)\n            for i in range(p):\n           \
    \     a0 = a[i + offset]\n                a1 = a[i + offset + p] * rot\n     \
    \           a2 = a[i + offset + p * 2] * rot2\n                a3 = a[i + offset\
    \ + p * 3] * rot3\n                a1na3imag = (a1 - a3) % MOD * _IMAG\n     \
    \           a[i + offset] = (a0 + a2 + a1 + a3) % MOD\n                a[i + offset\
    \ + p] = (a0 + a2 - a1 - a3) % MOD\n                a[i + offset + p * 2] = (a0\
    \ - a2 + a1na3imag) % MOD\n                a[i + offset + p * 3] = (a0 - a2 -\
    \ a1na3imag) % MOD\n            rot = rot * _rate3[(~s & -~s).bit_length()] %\
    \ MOD\n    if h - le & 1:\n        rot = 1\n        for s in range(1 << (h - 1)):\n\
    \            offset = s << 1\n            l = a[offset]\n            r = a[offset\
    \ + 1] * rot\n            a[offset] = (l + r) % MOD\n            a[offset + 1]\
    \ = (l - r) % MOD\n            rot = rot * _rate2[(~s & -~s).bit_length()] % MOD\n\
    \n\ndef _ifft(a):\n    n = len(a)\n    h = (n - 1).bit_length()\n    le = h\n\
    \    for le in range(h, 1, -2):\n        p = 1 << (h - le)\n        irot = 1\n\
    \        for s in range(1 << (le - 2)):\n            irot2 = irot * irot % MOD\n\
    \            irot3 = irot2 * irot % MOD\n            offset = s << (h - le + 2)\n\
    \            for i in range(p):\n                a0 = a[i + offset]\n        \
    \        a1 = a[i + offset + p]\n                a2 = a[i + offset + p * 2]\n\
    \                a3 = a[i + offset + p * 3]\n                a2na3iimag = (a2\
    \ - a3) * _IIMAG % MOD\n                a[i + offset] = (a0 + a1 + a2 + a3) %\
    \ MOD\n                a[i + offset + p] = (a0 - a1 + a2na3iimag) * irot % MOD\n\
    \                a[i + offset + p * 2] = (a0 + a1 - a2 - a3) * irot2 % MOD\n \
    \               a[i + offset + p * 3] = (a0 - a1 - a2na3iimag) * irot3 % MOD\n\
    \            irot = irot * _irate3[(~s & -~s).bit_length()] % MOD\n    if le &\
    \ 1:\n        p = 1 << (h - 1)\n        for i in range(p):\n            l = a[i]\n\
    \            r = a[i + p]\n            a[i] = l + r if l + r < MOD else l + r\
    \ - MOD\n            a[i + p] = l - r if l - r >= 0 else l - r + MOD\n\n\ndef\
    \ ntt(a) -> None:\n    if len(a) <= 1:\n        return\n    _fft(a)\n\n\ndef intt(a)\
    \ -> None:\n    if len(a) <= 1:\n        return\n    _ifft(a)\n    iv = pow(len(a),\
    \ MOD - 2, MOD)\n    for i, x in enumerate(a):\n        a[i] = x * iv % MOD\n\n\
    \ndef multiply(s: list, t: list) -> list:\n    n, m = len(s), len(t)\n    l =\
    \ n + m - 1\n    if min(n, m) <= 60:\n        a = [0] * l\n        for i, x in\
    \ enumerate(s):\n            for j, y in enumerate(t):\n                a[i +\
    \ j] += x * y\n        return [x % MOD for x in a]\n    z = 1 << (l - 1).bit_length()\n\
    \    a = s + [0] * (z - n)\n    b = t + [0] * (z - m)\n    _fft(a)\n    _fft(b)\n\
    \    for i, x in enumerate(b):\n        a[i] = a[i] * x % MOD\n    _ifft(a)\n\
    \    a[l:] = []\n    iz = pow(z, MOD - 2, MOD)\n    return [x * iz % MOD for x\
    \ in a]\n\n\ndef pow2(a: list) -> list:\n    l = (len(a) << 1) - 1\n    if len(a)\
    \ <= 60:\n        s = [0] * l\n        for i, x in enumerate(a):\n           \
    \ for j, y in enumerate(a):\n                s[i + j] += x * y\n        return\
    \ [x % MOD for x in s]\n    k = 2\n    M = 4\n    while M < l:\n        M <<=\
    \ 1\n        k += 1\n    s = a + [0] * (M - len(a))\n    _fft(s, k)\n    s = [x\
    \ * x % MOD for x in s]\n    _ifft(s, k)\n    s[l:] = []\n    invm = pow(M, MOD\
    \ - 2, MOD)\n    return [x * invm % MOD for x in s]\n\n\ndef ntt_doubling(a: list)\
    \ -> None:\n    M = len(a)\n    b = a[:]\n    intt(b)\n    r = 1\n    zeta = pow(3,\
    \ (MOD - 1) // (M << 1), MOD)\n    for i, x in enumerate(b):\n        b[i] = x\
    \ * r % MOD\n        r = r * zeta % MOD\n    ntt(b)\n    a += b\n"
  dependsOn: []
  isVerificationFile: false
  path: convolution/convolution.py
  requiredBy:
  - polynomial/composition.py
  - polynomial/multivariate_multiplication.py
  - polynomial/chirp_z.py
  - polynomial/sample_point_shift.py
  - polynomial/multipoint_evaluation.py
  - polynomial/tayler_shift.py
  - polynomial/product_tree.py
  - polynomial/formal_power_series.py
  timestamp: '2024-06-20 10:59:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/convolution/convolution_mod.test.py
documentation_of: convolution/convolution.py
layout: document
title: "\u7573\u307F\u8FBC\u307F $mod=998244353$"
---

多項式 $a_0+a_1x+a_2x^2+a_{n-1}x^{n-1}$ を配列 $[a_0,a_1,...,a_{n-1}]$　で表す.

このとき, $A=[a_0,a_1,...,a_{n-1}]$ と $B=[b_0,b_1,...,b_{m-1}]$ から $C=[c_0,c_1,...,c_{(n-1)+(m-1)}]$ を求める.
ただし,

$$C_k=\displaystyle\sum^{}_{i+j=k}a_ib_j\mod998,244,353$$
