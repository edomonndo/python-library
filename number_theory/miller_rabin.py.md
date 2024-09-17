---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: number_theory/factorize.py
    title: number_theory/factorize.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def miller_rabin(n: int) -> bool:\n    \"\"\"Miller-Rabin: \u2252 O(1)\"\"\
    \"\n    assert n < 1 << 64\n    if n == 2:\n        return True\n    if n < 2\
    \ or (n & 1) == 0:\n        return False\n    n1 = n - 1\n    d, s = n1, 0\n \
    \   while (d & 1) == 0:\n        d //= 2\n        s += 1\n\n    arr = (\n    \
    \    [2, 7, 61]\n        if n < 1 << 32\n        else [2, 325, 9375, 28178, 450775,\
    \ 9780504, 1795265022]\n    )\n    for a in arr:\n        if a % n == 0:\n   \
    \         continue\n        t = pow(a, d, n)\n        if t == 1 or t == n1:\n\
    \            continue\n        for _ in range(s):\n            t = pow(t, 2, n)\n\
    \            if t == n1:\n                break\n        else:\n            return\
    \ False\n    return True\n"
  dependsOn: []
  isVerificationFile: false
  path: number_theory/miller_rabin.py
  requiredBy:
  - number_theory/factorize.py
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: number_theory/miller_rabin.py
layout: document
redirect_from:
- /library/number_theory/miller_rabin.py
- /library/number_theory/miller_rabin.py.html
title: number_theory/miller_rabin.py
---
