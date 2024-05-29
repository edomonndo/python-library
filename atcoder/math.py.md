---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: atcoder/modint.py
    title: atcoder/modint.py
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
  code: "def _is_prime(n: int) -> bool:\n    \"\"\"\n    Reference:\n    M. Forisek\
    \ and J. Jancina,\n    Fast Primality Testing for Integers That Fit into a Machine\
    \ Word\n    \"\"\"\n\n    if n <= 1:\n        return False\n    if n == 2 or n\
    \ == 7 or n == 61:\n        return True\n    if n % 2 == 0:\n        return False\n\
    \n    d = n - 1\n    while d % 2 == 0:\n        d //= 2\n\n    for a in (2, 7,\
    \ 61):\n        t = d\n        y = pow(a, t, n)\n        while t != n - 1 and\
    \ y != 1 and y != n - 1:\n            y = y * y % n\n            t <<= 1\n   \
    \     if y != n - 1 and t % 2 == 0:\n            return False\n    return True\n\
    \n\ndef _inv_gcd(a: int, b: int) -> tuple[int, int]:\n    a %= b\n    if a ==\
    \ 0:\n        return (b, 0)\n\n    # Contracts:\n    # [1] s - m0 * a = 0 (mod\
    \ b)\n    # [2] t - m1 * a = 0 (mod b)\n    # [3] s * |m1| + t * |m0| <= b\n \
    \   s = b\n    t = a\n    m0 = 0\n    m1 = 1\n\n    while t:\n        u = s //\
    \ t\n        s -= t * u\n        m0 -= m1 * u  # |m1 * u| <= |m1| * s <= b\n\n\
    \        # [3]:\n        # (s - t * u) * |m1| + t * |m0 - m1 * u|\n        # <=\
    \ s * |m1| - t * u * |m1| + t * (|m0| + |m1| * u)\n        # = s * |m1| + t *\
    \ |m0| <= b\n\n        s, t = t, s\n        m0, m1 = m1, m0\n\n    # by [3]: |m0|\
    \ <= b/g\n    # by g != b: |m0| < b/g\n    if m0 < 0:\n        m0 += b // s\n\n\
    \    return (s, m0)\n\n\ndef _primitive_root(m: int) -> int:\n    if m == 2:\n\
    \        return 1\n    if m == 167772161:\n        return 3\n    if m == 469762049:\n\
    \        return 3\n    if m == 754974721:\n        return 11\n    if m == 998244353:\n\
    \        return 3\n\n    divs = [2] + [0] * 19\n    cnt = 1\n    x = (m - 1) //\
    \ 2\n    while x % 2 == 0:\n        x //= 2\n\n    i = 3\n    while i * i <= x:\n\
    \        if x % i == 0:\n            divs[cnt] = i\n            cnt += 1\n   \
    \         while x % i == 0:\n                x //= i\n        i += 2\n\n    if\
    \ x > 1:\n        divs[cnt] = x\n        cnt += 1\n\n    g = 2\n    while True:\n\
    \        for i in range(cnt):\n            if pow(g, (m - 1) // divs[i], m) ==\
    \ 1:\n                break\n        else:\n            return g\n        g +=\
    \ 1\n\n\ndef inv_mod(x: int, m: int) -> int:\n    assert 1 <= m\n\n    z = _inv_gcd(x,\
    \ m)\n\n    assert z[0] == 1\n\n    return z[1]\n\n\ndef crt(r: list[int], m:\
    \ list[int]) -> tuple[int, int]:\n    assert len(r) == len(m)\n\n    # Contracts:\
    \ 0 <= r0 < m0\n    r0 = 0\n    m0 = 1\n    for r1, m1 in zip(r, m):\n       \
    \ assert 1 <= m1\n        r1 %= m1\n        if m0 < m1:\n            r0, r1 =\
    \ r1, r0\n            m0, m1 = m1, m0\n        if m0 % m1 == 0:\n            if\
    \ r0 % m1 != r1:\n                return (0, 0)\n            continue\n\n    \
    \    # assume: m0 > m1, lcm(m0, m1) >= 2 * max(m0, m1)\n\n        \"\"\"\n   \
    \     (r0, m0), (r1, m1) -> (r2, m2 = lcm(m0, m1));\n        r2 % m0 = r0\n  \
    \      r2 % m1 = r1\n        -> (r0 + x*m0) % m1 = r1\n        -> x*u0*g % (u1*g)\
    \ = (r1 - r0) (u0*g = m0, u1*g = m1)\n        -> x = (r1 - r0) / g * inv(u0) (mod\
    \ u1)\n        \"\"\"\n\n        # im = inv(u0) (mod u1) (0 <= im < u1)\n    \
    \    g, im = _inv_gcd(m0, m1)\n\n        u1 = m1 // g\n        # |r1 - r0| < (m0\
    \ + m1) <= lcm(m0, m1)\n        if (r1 - r0) % g:\n            return (0, 0)\n\
    \n        # u1 * u1 <= m1 * m1 / g / g <= m0 * m1 / g = lcm(m0, m1)\n        x\
    \ = (r1 - r0) // g % u1 * im % u1\n\n        \"\"\"\n        |r0| + |m0 * x|\n\
    \        < m0 + m0 * (u1 - 1)\n        = m0 + m0 * m1 / g - m0\n        = lcm(m0,\
    \ m1)\n        \"\"\"\n\n        r0 += x * m0\n        m0 *= u1  # -> lcm(m0,\
    \ m1)\n        if r0 < 0:\n            r0 += m0\n\n    return (r0, m0)\n\n\ndef\
    \ floor_sum(n: int, m: int, a: int, b: int) -> int:\n    assert 1 <= n\n    assert\
    \ 1 <= m\n\n    ans = 0\n\n    if a >= m:\n        ans += (n - 1) * n * (a //\
    \ m) // 2\n        a %= m\n\n    if b >= m:\n        ans += n * (b // m)\n   \
    \     b %= m\n\n    y_max = (a * n + b) // m\n    x_max = y_max * m - b\n\n  \
    \  if y_max == 0:\n        return ans\n\n    ans += (n - (x_max + a - 1) // a)\
    \ * y_max\n    ans += floor_sum(y_max, a, m, (a - x_max % a) % a)\n\n    return\
    \ ans\n"
  dependsOn: []
  isVerificationFile: false
  path: atcoder/math.py
  requiredBy:
  - atcoder/modint.py
  timestamp: '2024-05-29 14:24:11+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: atcoder/math.py
layout: document
redirect_from:
- /library/atcoder/math.py
- /library/atcoder/math.py.html
title: atcoder/math.py
---
