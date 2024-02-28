---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: atcoder/_bit.py
    title: atcoder/_bit.py
  - icon: ':warning:'
    path: atcoder/_math.py
    title: atcoder/_math.py
  - icon: ':warning:'
    path: atcoder/modint.py
    title: atcoder/modint.py
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
  code: "import typing\n\nimport atcoder._bit\nimport atcoder._math\nfrom atcoder.modint\
    \ import ModContext, Modint\n\n\n_sum_e = {}  # _sum_e[i] = ies[0] * ... * ies[i\
    \ - 1] * es[i]\n\n\ndef _butterfly(a: typing.List[Modint]) -> None:\n    g = atcoder._math._primitive_root(a[0].mod())\n\
    \    n = len(a)\n    h = atcoder._bit._ceil_pow2(n)\n\n    if a[0].mod() not in\
    \ _sum_e:\n        es = [Modint(0)] * 30  # es[i]^(2^(2+i)) == 1\n        ies\
    \ = [Modint(0)] * 30\n        cnt2 = atcoder._bit._bsf(a[0].mod() - 1)\n     \
    \   e = Modint(g) ** ((a[0].mod() - 1) >> cnt2)\n        ie = e.inv()\n      \
    \  for i in range(cnt2, 1, -1):\n            # e^(2^i) == 1\n            es[i\
    \ - 2] = e\n            ies[i - 2] = ie\n            e = e * e\n            ie\
    \ = ie * ie\n        sum_e = [Modint(0)] * 30\n        now = Modint(1)\n     \
    \   for i in range(cnt2 - 2):\n            sum_e[i] = es[i] * now\n          \
    \  now *= ies[i]\n        _sum_e[a[0].mod()] = sum_e\n    else:\n        sum_e\
    \ = _sum_e[a[0].mod()]\n\n    for ph in range(1, h + 1):\n        w = 1 << (ph\
    \ - 1)\n        p = 1 << (h - ph)\n        now = Modint(1)\n        for s in range(w):\n\
    \            offset = s << (h - ph + 1)\n            for i in range(p):\n    \
    \            left = a[i + offset]\n                right = a[i + offset + p] *\
    \ now\n                a[i + offset] = left + right\n                a[i + offset\
    \ + p] = left - right\n            now *= sum_e[atcoder._bit._bsf(~s)]\n\n\n_sum_ie\
    \ = {}  # _sum_ie[i] = es[0] * ... * es[i - 1] * ies[i]\n\n\ndef _butterfly_inv(a:\
    \ typing.List[Modint]) -> None:\n    g = atcoder._math._primitive_root(a[0].mod())\n\
    \    n = len(a)\n    h = atcoder._bit._ceil_pow2(n)\n\n    if a[0].mod() not in\
    \ _sum_ie:\n        es = [Modint(0)] * 30  # es[i]^(2^(2+i)) == 1\n        ies\
    \ = [Modint(0)] * 30\n        cnt2 = atcoder._bit._bsf(a[0].mod() - 1)\n     \
    \   e = Modint(g) ** ((a[0].mod() - 1) >> cnt2)\n        ie = e.inv()\n      \
    \  for i in range(cnt2, 1, -1):\n            # e^(2^i) == 1\n            es[i\
    \ - 2] = e\n            ies[i - 2] = ie\n            e = e * e\n            ie\
    \ = ie * ie\n        sum_ie = [Modint(0)] * 30\n        now = Modint(1)\n    \
    \    for i in range(cnt2 - 2):\n            sum_ie[i] = ies[i] * now\n       \
    \     now *= es[i]\n        _sum_ie[a[0].mod()] = sum_ie\n    else:\n        sum_ie\
    \ = _sum_ie[a[0].mod()]\n\n    for ph in range(h, 0, -1):\n        w = 1 << (ph\
    \ - 1)\n        p = 1 << (h - ph)\n        inow = Modint(1)\n        for s in\
    \ range(w):\n            offset = s << (h - ph + 1)\n            for i in range(p):\n\
    \                left = a[i + offset]\n                right = a[i + offset +\
    \ p]\n                a[i + offset] = left + right\n                a[i + offset\
    \ + p] = Modint(\n                    (a[0].mod() + left.val() - right.val())\
    \ * inow.val())\n            inow *= sum_ie[atcoder._bit._bsf(~s)]\n\n\ndef convolution_mod(a:\
    \ typing.List[Modint],\n                    b: typing.List[Modint]) -> typing.List[Modint]:\n\
    \    n = len(a)\n    m = len(b)\n\n    if n == 0 or m == 0:\n        return []\n\
    \n    if min(n, m) <= 60:\n        if n < m:\n            n, m = m, n\n      \
    \      a, b = b, a\n        ans = [Modint(0) for _ in range(n + m - 1)]\n    \
    \    for i in range(n):\n            for j in range(m):\n                ans[i\
    \ + j] += a[i] * b[j]\n        return ans\n\n    z = 1 << atcoder._bit._ceil_pow2(n\
    \ + m - 1)\n\n    while len(a) < z:\n        a.append(Modint(0))\n    _butterfly(a)\n\
    \n    while len(b) < z:\n        b.append(Modint(0))\n    _butterfly(b)\n\n  \
    \  for i in range(z):\n        a[i] *= b[i]\n    _butterfly_inv(a)\n    a = a[:n\
    \ + m - 1]\n\n    iz = Modint(z).inv()\n    for i in range(n + m - 1):\n     \
    \   a[i] *= iz\n\n    return a\n\n\ndef convolution(mod: int, a: typing.List[typing.Any],\n\
    \                b: typing.List[typing.Any]) -> typing.List[typing.Any]:\n   \
    \ n = len(a)\n    m = len(b)\n\n    if n == 0 or m == 0:\n        return []\n\n\
    \    with ModContext(mod):\n        a2 = list(map(Modint, a))\n        b2 = list(map(Modint,\
    \ b))\n\n        return list(map(lambda c: c.val(), convolution_mod(a2, b2)))\n\
    \n\ndef convolution_int(\n        a: typing.List[int], b: typing.List[int]) ->\
    \ typing.List[int]:\n    n = len(a)\n    m = len(b)\n\n    if n == 0 or m == 0:\n\
    \        return []\n\n    mod1 = 754974721  # 2^24\n    mod2 = 167772161  # 2^25\n\
    \    mod3 = 469762049  # 2^26\n    m2m3 = mod2 * mod3\n    m1m3 = mod1 * mod3\n\
    \    m1m2 = mod1 * mod2\n    m1m2m3 = mod1 * mod2 * mod3\n\n    i1 = atcoder._math._inv_gcd(mod2\
    \ * mod3, mod1)[1]\n    i2 = atcoder._math._inv_gcd(mod1 * mod3, mod2)[1]\n  \
    \  i3 = atcoder._math._inv_gcd(mod1 * mod2, mod3)[1]\n\n    c1 = convolution(mod1,\
    \ a, b)\n    c2 = convolution(mod2, a, b)\n    c3 = convolution(mod3, a, b)\n\n\
    \    c = [0] * (n + m - 1)\n    for i in range(n + m - 1):\n        c[i] += (c1[i]\
    \ * i1) % mod1 * m2m3\n        c[i] += (c2[i] * i2) % mod2 * m1m3\n        c[i]\
    \ += (c3[i] * i3) % mod3 * m1m2\n        c[i] %= m1m2m3\n\n    return c\n"
  dependsOn:
  - atcoder/_bit.py
  - atcoder/_math.py
  - atcoder/modint.py
  isVerificationFile: false
  path: atcoder/convolution.py
  requiredBy: []
  timestamp: '2024-02-05 08:23:41+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: atcoder/convolution.py
layout: document
redirect_from:
- /library/atcoder/convolution.py
- /library/atcoder/convolution.py.html
title: atcoder/convolution.py
---
