---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: number_theory/factorize.py
    title: number_theory/factorize.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/number_theory/primitive_root.test.py
    title: Primitive Root
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from random import randrange\n\nfrom number_theory.factorize import factorize\n\
    \n\ndef primitive_root(p: int) -> int:\n    # assert is_prime(p)\n    if p ==\
    \ 2:\n        return 1\n    pf = factorize(p - 1)\n    res = 2\n    cnt = 0\n\
    \    while True:\n        for pi in pf.keys():\n            if pow(res, (p - 1)\
    \ // pi, p) != 1:\n                cnt += 1\n            else:\n             \
    \   cnt = 0\n                break\n        if cnt == len(pf):\n            break\n\
    \        res = randrange(3, p - 1)\n    return res\n"
  dependsOn:
  - number_theory/factorize.py
  isVerificationFile: false
  path: number_theory/primitive_root.py
  requiredBy: []
  timestamp: '2024-07-02 07:37:15+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/number_theory/primitive_root.test.py
documentation_of: number_theory/primitive_root.py
layout: document
redirect_from:
- /library/number_theory/primitive_root.py
- /library/number_theory/primitive_root.py.html
title: number_theory/primitive_root.py
---
