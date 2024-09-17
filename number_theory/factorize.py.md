---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: number_theory/miller_rabin.py
    title: number_theory/miller_rabin.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: number_theory/primitive_root.py
    title: number_theory/primitive_root.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/number_theory/factorize.test.py
    title: Factorize
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import math\nimport random\n\nfrom number_theory.miller_rabin import miller_rabin\n\
    \n\ndef find_prime_factor(n):\n    b = n.bit_length() - 1\n    b = (b >> 2) <<\
    \ 2\n    m = 2 * int(2 ** (b / 8))\n\n    while True:\n        c = random.randrange(1,\
    \ n)\n        f = lambda a: (pow(a, 2, n) + c) % n\n        y = 0\n        g =\
    \ q = r = 1\n        while g == 1:\n            x = y\n            for _ in range(r):\n\
    \                y = f(y)\n            k = 0\n            while k < r and g ==\
    \ 1:\n                ys = y\n                for _ in range(min(m, r - k)):\n\
    \                    y = f(y)\n                    q = q * abs(x - y) % n\n  \
    \              g = math.gcd(q, n)\n                k += m\n            r <<= 1\n\
    \        if g == n:\n            g = 1\n            y = ys\n            while\
    \ g == 1:\n                y = f(y)\n                g = math.gcd(abs(x - y),\
    \ n)\n        if g == n:\n            continue\n        if miller_rabin(g):\n\
    \            return g\n        elif miller_rabin(n // g):\n            return\
    \ n // g\n        else:\n            n = g\n\n\ndef factorize(n):\n    res = {}\n\
    \    for p in range(2, 1000):\n        if p * p > n:\n            break\n    \
    \    if n % p:\n            continue\n        s = 0\n        while n % p == 0:\n\
    \            n //= p\n            s += 1\n        res[p] = s\n\n    while not\
    \ miller_rabin(n) and n > 1:\n        p = find_prime_factor(n)\n        s = 0\n\
    \        while n % p == 0:\n            n //= p\n            s += 1\n        res[p]\
    \ = s\n    if n > 1:\n        res[n] = 1\n    return res\n"
  dependsOn:
  - number_theory/miller_rabin.py
  isVerificationFile: false
  path: number_theory/factorize.py
  requiredBy:
  - number_theory/primitive_root.py
  timestamp: '2024-07-02 07:37:15+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/number_theory/factorize.test.py
documentation_of: number_theory/factorize.py
layout: document
redirect_from:
- /library/number_theory/factorize.py
- /library/number_theory/factorize.py.html
title: number_theory/factorize.py
---
