---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: math_/is_prime.py
    title: "\u7D20\u6570\u5224\u5B9A"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/math/factorize.test.py
    title: test/library_checker/math/factorize.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import math\nimport random\n\nfrom math_.is_prime import miller_rabin\n\n\
    \ndef find_prime_factor(n):\n    b = n.bit_length() - 1\n    b = (b >> 2) << 2\n\
    \    m = 2 * int(2 ** (b / 8))\n\n    while True:\n        c = random.randrange(1,\
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
  - math_/is_prime.py
  isVerificationFile: false
  path: math_/factorize.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/math/factorize.test.py
documentation_of: math_/factorize.py
layout: document
title: "\u7D20\u56E0\u6570\u5206\u89E3"
---

### `factorize(n: int)`

$s$を素因数分解する.返り値はdictで,keyが素因数,valueがその素因数で割れる回数.