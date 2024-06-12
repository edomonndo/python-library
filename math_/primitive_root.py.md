---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: math_/factorize.py
    title: "\u7D20\u56E0\u6570\u5206\u89E3"
  _extendedRequiredBy:
  - icon: ':warning:'
    path: test/library_checker/math/primitive_root.py
    title: test/library_checker/math/primitive_root.py
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
  code: "from random import randrange\n\nfrom math_.factorize import factorize\n\n\
    \ndef primitive_root(p: int) -> int:\n    # assert is_prime(p)\n    if p == 2:\n\
    \        return 1\n    pf = factorize(p - 1)\n    res = 2\n    cnt = 0\n    while\
    \ True:\n        for pi in pf.keys():\n            if pow(res, (p - 1) // pi,\
    \ p) != 1:\n                cnt += 1\n            else:\n                cnt =\
    \ 0\n                break\n        if cnt == len(pf):\n            break\n  \
    \      res = randrange(3, p - 1)\n    return res\n"
  dependsOn:
  - math_/factorize.py
  isVerificationFile: false
  path: math_/primitive_root.py
  requiredBy:
  - test/library_checker/math/primitive_root.py
  timestamp: '2024-06-12 17:23:04+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: math_/primitive_root.py
layout: document
title: "\u539F\u59CB\u6839"
---

（3以上の）素数$p$と$1$以上$p$未満の整数$r$が以下の性質を満たすとき，$r$を法$p$に対する原始根と呼ぶ.


$r,r^2,⋯ ,r^{p−2}のいずれもがpで割って余り1でない$

（また，$r=1$は $p=2$に対する原始根である，とする.）