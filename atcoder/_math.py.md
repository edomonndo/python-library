---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import typing\n\n\ndef _is_prime(n: int) -> bool:\n    '''\n    Reference:\n\
    \    M. Forisek and J. Jancina,\n    Fast Primality Testing for Integers That\
    \ Fit into a Machine Word\n    '''\n\n    if n <= 1:\n        return False\n \
    \   if n == 2 or n == 7 or n == 61:\n        return True\n    if n % 2 == 0:\n\
    \        return False\n\n    d = n - 1\n    while d % 2 == 0:\n        d //= 2\n\
    \n    for a in (2, 7, 61):\n        t = d\n        y = pow(a, t, n)\n        while\
    \ t != n - 1 and y != 1 and y != n - 1:\n            y = y * y % n\n         \
    \   t <<= 1\n        if y != n - 1 and t % 2 == 0:\n            return False\n\
    \    return True\n\n\ndef _inv_gcd(a: int, b: int) -> typing.Tuple[int, int]:\n\
    \    a %= b\n    if a == 0:\n        return (b, 0)\n\n    # Contracts:\n    #\
    \ [1] s - m0 * a = 0 (mod b)\n    # [2] t - m1 * a = 0 (mod b)\n    # [3] s *\
    \ |m1| + t * |m0| <= b\n    s = b\n    t = a\n    m0 = 0\n    m1 = 1\n\n    while\
    \ t:\n        u = s // t\n        s -= t * u\n        m0 -= m1 * u  # |m1 * u|\
    \ <= |m1| * s <= b\n\n        # [3]:\n        # (s - t * u) * |m1| + t * |m0 -\
    \ m1 * u|\n        # <= s * |m1| - t * u * |m1| + t * (|m0| + |m1| * u)\n    \
    \    # = s * |m1| + t * |m0| <= b\n\n        s, t = t, s\n        m0, m1 = m1,\
    \ m0\n\n    # by [3]: |m0| <= b/g\n    # by g != b: |m0| < b/g\n    if m0 < 0:\n\
    \        m0 += b // s\n\n    return (s, m0)\n\n\ndef _primitive_root(m: int) ->\
    \ int:\n    if m == 2:\n        return 1\n    if m == 167772161:\n        return\
    \ 3\n    if m == 469762049:\n        return 3\n    if m == 754974721:\n      \
    \  return 11\n    if m == 998244353:\n        return 3\n\n    divs = [2] + [0]\
    \ * 19\n    cnt = 1\n    x = (m - 1) // 2\n    while x % 2 == 0:\n        x //=\
    \ 2\n\n    i = 3\n    while i * i <= x:\n        if x % i == 0:\n            divs[cnt]\
    \ = i\n            cnt += 1\n            while x % i == 0:\n                x\
    \ //= i\n        i += 2\n\n    if x > 1:\n        divs[cnt] = x\n        cnt +=\
    \ 1\n\n    g = 2\n    while True:\n        for i in range(cnt):\n            if\
    \ pow(g, (m - 1) // divs[i], m) == 1:\n                break\n        else:\n\
    \            return g\n        g += 1\n"
  dependsOn: []
  isVerificationFile: false
  path: atcoder/_math.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: atcoder/_math.py
layout: document
redirect_from:
- /library/atcoder/_math.py
- /library/atcoder/_math.py.html
title: atcoder/_math.py
---
