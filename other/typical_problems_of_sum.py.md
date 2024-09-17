---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/unit_test/typical_problems_of_sum.test.py
    title: "\u5178\u578B\u8DB3\u3057\u4E0A\u3052"
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def solve1(A):\n    n = len(A)\n    Sn = sum(A)\n    res = Si = 0\n    for\
    \ i in range(n - 1):\n        Si += A[i]\n        res += A[i] * (Sn - Si)\n  \
    \  return res\n\n\ndef solve2(A):\n    n = len(A)\n    res = 0\n    for i, a in\
    \ enumerate(sorted(A), 1):\n        res += a * (n - i)\n    return res\n\n\ndef\
    \ solve3(A):\n    n = len(A)\n    Sn1 = Tn1 = 0\n    for i in range(n - 1):\n\
    \        Sn1 += A[i]\n        Tn1 += A[i] * Sn1\n    Sn = Sn1 + A[n - 1]\n   \
    \ Si = Ti = 0\n    res = 0\n    for i in range(n - 2):\n        Si += A[i]\n \
    \       Ti += A[i] * Si\n        res += A[i] * (Sn * (Sn1 - Si) - (Tn1 - Ti))\n\
    \    return res\n\n\ndef solve4(A):\n    n = len(A)\n    res = 0\n    for i, a\
    \ in enumerate(sorted(A), 1):\n        res += a * (n - i) * (n - 1 - i) // 2\n\
    \    return res\n\n\ndef solve5(A):\n    n = len(A)\n    cnt = [0] * 31\n    for\
    \ a in A:\n        for k in range(31):\n            if a >> k & 1:\n         \
    \       cnt[k] += 1\n    res = 0\n    for i, a in enumerate(A, 1):\n        for\
    \ k in range(31):\n            if a >> k & 1:\n                cnt[k] -= 1\n \
    \               res += (n - i - cnt[k]) * (1 << k)\n            else:\n      \
    \          res += cnt[k] * (1 << k)\n    return res\n\n\ndef solve6(A):\n    n\
    \ = len(A)\n    Sn = sum(A)\n    Tn = sum(a**2 for a in A)\n    res = 0\n    Si\
    \ = Ti = 0\n    for i, a in enumerate(A, 1):\n        Si += a\n        Ti += a**2\n\
    \        res += a * a * (n - i) - 2 * a * (Sn - Si) + Tn - Ti\n    return res\n\
    \n\ndef solve7(A):\n    n = len(A)\n    Sn = sum(A)\n    res = n * Sn\n    Si\
    \ = 0\n    for i, a in enumerate(sorted(A), 1):\n        Si += a\n        res\
    \ -= Si + a * (n - i)\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: other/typical_problems_of_sum.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/unit_test/typical_problems_of_sum.test.py
documentation_of: other/typical_problems_of_sum.py
layout: document
redirect_from:
- /library/other/typical_problems_of_sum.py
- /library/other/typical_problems_of_sum.py.html
title: other/typical_problems_of_sum.py
---
