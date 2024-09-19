---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/enumerative_combinatorics/montmort_number_mod.test.py
    title: Montmort Number
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def derangement(n: int, mod: int) -> list[int]:\n    # assert n >= 0\n  \
    \  if n == 0:\n        return [0]\n    elif n == 1:\n        return [0, 0]\n \
    \   elif mod == 1:\n        return [0] * (n + 1)\n    res = [0] * (n + 1)\n  \
    \  res[2] = 1\n    x, y = 0, 1\n    for i in range(3, n + 1):\n        x, y =\
    \ y, (i - 1) * (x + y)\n        y %= mod\n        res[i] = y\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: enumerative_combinatorics/derangement.py
  requiredBy: []
  timestamp: '2024-08-26 12:24:24+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/enumerative_combinatorics/montmort_number_mod.test.py
documentation_of: enumerative_combinatorics/derangement.py
layout: document
title: "\u64B9\u4E71\u9806\u5217"
---
