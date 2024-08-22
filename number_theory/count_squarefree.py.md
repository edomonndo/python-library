---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: number_theory/kth_root.py
    title: Kth Root
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/number_theory/counting_squarefrees.test.py
    title: Counting Square-free Integers
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from number_theory.kth_root import KthRoot\n\n\ndef count_squarefree(n: int)\
    \ -> int:\n    def get_mobius(n: int) -> list[int]:\n        sieve = [1] * (n\
    \ + 1)\n        mu = [1] * (n + 1)\n        for i in range(2, n + 1):\n      \
    \      if sieve[i] == 0:\n                continue\n            mu[i] = -1\n \
    \           for j in range(i * i, n + 1, i):\n                sieve[j] = 0\n \
    \           for j in range(i * 2, n + 1, i):\n                mu[j] = -mu[j]\n\
    \            for j in range(i * i, n + 1, i * i):\n                mu[j] = 0\n\
    \        return mu\n\n    res = 0\n    if n <= 4000:\n        mu = get_mobius(n\
    \ + 1)\n        i = 1\n        while i * i <= n:\n            res += n // (i *\
    \ i) * mu[i]\n            i += 1\n        return res\n\n    I = KthRoot.floor(n,\
    \ 5)\n    D = KthRoot.floor(n // (I + 1), 2)\n    mu = get_mobius(D + 1)\n   \
    \ Mf = [0] * (D + 1)\n    for i in range(1, D + 1):\n        Mf[i] = Mf[i - 1]\
    \ + mu[i]\n    Md = [0] * (I + 1)\n    for i in range(I, 0, -1):\n        m =\
    \ 1\n        x = KthRoot.floor(n // i, 2)\n        Dx = KthRoot.floor(x, 2)\n\
    \        Rx = x // (Dx + 1)\n        r = 2\n        while i * r * r <= I:\n  \
    \          m -= Md[i * r * r]\n            r += 1\n        while r <= Rx:\n  \
    \          m -= Mf[x // r]\n            r += 1\n        for d in range(1, Dx +\
    \ 1):\n            m -= mu[d] * (x // d - Rx)\n        Md[i] = m\n        res\
    \ += m\n    for i in range(1, D + 1):\n        res += mu[i] * (n // (i * i) -\
    \ I)\n    return res\n"
  dependsOn:
  - number_theory/kth_root.py
  isVerificationFile: false
  path: number_theory/count_squarefree.py
  requiredBy: []
  timestamp: '2024-08-22 11:33:17+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/number_theory/counting_squarefrees.test.py
documentation_of: number_theory/count_squarefree.py
layout: document
title: "\u7121\u5E73\u65B9\u6570\u306E\u6570\u3048\u4E0A\u3052"
---

制約: $1 <= n <= 10^{18}$