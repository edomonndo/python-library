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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def inv_gcd(a, b):\n    a = a % b\n    if a == 0:\n        return (b, 0)\n\
    \    s = b\n    t = a\n    m0 = 0\n    m1 = 1\n    while t:\n        u = s //\
    \ t\n        s -= t * u\n        m0 -= m1 * u\n        s, t = t, s\n        m0,\
    \ m1 = m1, m0\n    if m0 < 0:\n        m0 += b // s\n    return (s, m0)\n\n\n\
    def inv_mod(x, m):\n    assert 1 <= m\n    z = inv_gcd(x, m)\n    assert z[0]\
    \ == 1\n    return z[1]\n\n\ndef crt(r, m):\n    assert len(r) == len(m)\n   \
    \ n = len(r)\n    r0 = 0\n    m0 = 1\n    for i in range(n):\n        assert 1\
    \ <= m[i]\n        r1 = r[i] % m[i]\n        m1 = m[i]\n        if m0 < m1:\n\
    \            r0, r1 = r1, r0\n            m0, m1 = m1, m0\n        if m0 % m1\
    \ == 0:\n            if r0 % m1 != r1:\n                return (0, 0)\n      \
    \      continue\n        g, im = inv_gcd(m0, m1)\n        u1 = m1 // g\n     \
    \   if (r1 - r0) % g:\n            return (0, 0)\n        x = (r1 - r0) // g %\
    \ u1 * im % u1\n        r0 += x * m0\n        m0 *= u1\n        if r0 < 0:\n \
    \           r0 += m0\n    return (r0, m0)\n"
  dependsOn: []
  isVerificationFile: false
  path: number_theory/chinese_remainder_theorem.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: number_theory/chinese_remainder_theorem.py
layout: document
redirect_from:
- /library/number_theory/chinese_remainder_theorem.py
- /library/number_theory/chinese_remainder_theorem.py.html
title: number_theory/chinese_remainder_theorem.py
---
