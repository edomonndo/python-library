---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/convolution/bitwise_and_convolution.test.py
    title: Bitwise And Convolution
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "MOD = 998244353\n\n\ndef sup_zeta_transform(buf: list[int]) -> None:\n  \
    \  i, n = 1, len(buf)\n    while i < n:\n        for j in range(n):\n        \
    \    if i & j == 0:\n                buf[j] = (buf[j] + buf[i | j]) % MOD\n  \
    \      i <<= 1\n\n\ndef sup_moebius_transform(buf: list[int]) -> None:\n    i,\
    \ n = 1, len(buf)\n    while i < n:\n        for j in range(n):\n            if\
    \ i & j == 0:\n                buf[j] = (buf[j] - buf[i | j]) % MOD\n        i\
    \ <<= 1\n\n\ndef sub_zeta_transform(buf: list[int]) -> None:\n    i, n = 1, len(buf)\n\
    \    while i < n:\n        for j in range(0, n, i << 1):\n            for k in\
    \ range(i):\n                buf[j + k + i] = (buf[j + k + i] + buf[j + k]) %\
    \ MOD\n        i <<= 1\n\n\ndef sub_moebius_transform(buf: list[int]) -> None:\n\
    \    i, n = 1, len(buf)\n    while i < n:\n        for j in range(0, n, i << 1):\n\
    \            for k in range(i):\n                buf[j + k + i] = (buf[j + k +\
    \ i] - buf[j + k]) % MOD\n        i <<= 1\n\n\ndef bitwize_and_conv(f: list[int],\
    \ g: list[int]) -> None:\n    n = len(f)\n    assert n == len(g)\n    sup_zeta_transform(f)\n\
    \    sup_zeta_transform(g)\n    for i in range(n):\n        f[i] = f[i] * g[i]\
    \ % MOD\n    sup_moebius_transform(f)\n\n\ndef bitwize_or_conv(f: list[int], g:\
    \ list[int]) -> None:\n    n = len(f)\n    assert n == len(g)\n    sub_zeta_transform(f)\n\
    \    sub_zeta_transform(g)\n    for i in range(n):\n        f[i] = f[i] * g[i]\
    \ % MOD\n    sub_moebius_transform(f)\n"
  dependsOn: []
  isVerificationFile: false
  path: convolution/zeta_moebius_transform.py
  requiredBy: []
  timestamp: '2024-09-03 09:51:53+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/convolution/bitwise_and_convolution.test.py
documentation_of: convolution/zeta_moebius_transform.py
layout: document
redirect_from:
- /library/convolution/zeta_moebius_transform.py
- /library/convolution/zeta_moebius_transform.py.html
title: convolution/zeta_moebius_transform.py
---
