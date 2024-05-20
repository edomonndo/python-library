---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: atcoder/_math.py
    title: atcoder/_math.py
  _extendedRequiredBy: []
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
  code: "import typing\n\nimport atcoder._math\n\n\ndef inv_mod(x: int, m: int) ->\
    \ int:\n    assert 1 <= m\n\n    z = atcoder._math._inv_gcd(x, m)\n\n    assert\
    \ z[0] == 1\n\n    return z[1]\n\n\ndef crt(r: typing.List[int], m: typing.List[int])\
    \ -> typing.Tuple[int, int]:\n    assert len(r) == len(m)\n\n    # Contracts:\
    \ 0 <= r0 < m0\n    r0 = 0\n    m0 = 1\n    for r1, m1 in zip(r, m):\n       \
    \ assert 1 <= m1\n        r1 %= m1\n        if m0 < m1:\n            r0, r1 =\
    \ r1, r0\n            m0, m1 = m1, m0\n        if m0 % m1 == 0:\n            if\
    \ r0 % m1 != r1:\n                return (0, 0)\n            continue\n\n    \
    \    # assume: m0 > m1, lcm(m0, m1) >= 2 * max(m0, m1)\n\n        '''\n      \
    \  (r0, m0), (r1, m1) -> (r2, m2 = lcm(m0, m1));\n        r2 % m0 = r0\n     \
    \   r2 % m1 = r1\n        -> (r0 + x*m0) % m1 = r1\n        -> x*u0*g % (u1*g)\
    \ = (r1 - r0) (u0*g = m0, u1*g = m1)\n        -> x = (r1 - r0) / g * inv(u0) (mod\
    \ u1)\n        '''\n\n        # im = inv(u0) (mod u1) (0 <= im < u1)\n       \
    \ g, im = atcoder._math._inv_gcd(m0, m1)\n\n        u1 = m1 // g\n        # |r1\
    \ - r0| < (m0 + m1) <= lcm(m0, m1)\n        if (r1 - r0) % g:\n            return\
    \ (0, 0)\n\n        # u1 * u1 <= m1 * m1 / g / g <= m0 * m1 / g = lcm(m0, m1)\n\
    \        x = (r1 - r0) // g % u1 * im % u1\n\n        '''\n        |r0| + |m0\
    \ * x|\n        < m0 + m0 * (u1 - 1)\n        = m0 + m0 * m1 / g - m0\n      \
    \  = lcm(m0, m1)\n        '''\n\n        r0 += x * m0\n        m0 *= u1  # ->\
    \ lcm(m0, m1)\n        if r0 < 0:\n            r0 += m0\n\n    return (r0, m0)\n\
    \n\ndef floor_sum(n: int, m: int, a: int, b: int) -> int:\n    assert 1 <= n\n\
    \    assert 1 <= m\n\n    ans = 0\n\n    if a >= m:\n        ans += (n - 1) *\
    \ n * (a // m) // 2\n        a %= m\n\n    if b >= m:\n        ans += n * (b //\
    \ m)\n        b %= m\n\n    y_max = (a * n + b) // m\n    x_max = y_max * m -\
    \ b\n\n    if y_max == 0:\n        return ans\n\n    ans += (n - (x_max + a -\
    \ 1) // a) * y_max\n    ans += floor_sum(y_max, a, m, (a - x_max % a) % a)\n\n\
    \    return ans\n"
  dependsOn:
  - atcoder/_math.py
  isVerificationFile: false
  path: atcoder/math.py
  requiredBy: []
  timestamp: '2024-02-05 08:23:41+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: atcoder/math.py
layout: document
redirect_from:
- /library/atcoder/math.py
- /library/atcoder/math.py.html
title: atcoder/math.py
---
