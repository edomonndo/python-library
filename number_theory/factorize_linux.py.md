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
  code: "def factorize(n: int):\n    from subprocess import run\n\n    out = run(\"\
    factor \" + str(n), shell=True, capture_output=True).stdout\n    # n: p1 p1 p1\
    \ p2 p2 p3 ...\n    res = dict()\n    for p in out.split()[1:]:\n        if p\
    \ not in res:\n            res[p] = 0\n        res[p] += 1\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: number_theory/factorize_linux.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: number_theory/factorize_linux.py
layout: document
redirect_from:
- /library/number_theory/factorize_linux.py
- /library/number_theory/factorize_linux.py.html
title: number_theory/factorize_linux.py
---
