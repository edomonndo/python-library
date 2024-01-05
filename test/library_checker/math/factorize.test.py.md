---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/factorize
    links:
    - https://judge.yosupo.jp/problem/factorize
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/factorize\n\
    \nfrom math_.factorize import factorize\n\nQ = int(input())\nquery = [int(input())\
    \ for _ in range(Q)]\nans = [None] * Q\nfor i in range(Q):\n    x = factorize(query[i])\n\
    \    factors = [i for i, j in sorted(x.items()) for _ in range(j)]\n    ans[i]\
    \ = \" \".join(map(str, [len(factors)] + factors))\n\nprint(*ans, sep=\"\\n\"\
    )\n"
  dependsOn: []
  isVerificationFile: true
  path: test/library_checker/math/factorize.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/math/factorize.test.py
layout: document
redirect_from:
- /verify/test/library_checker/math/factorize.test.py
- /verify/test/library_checker/math/factorize.test.py.html
title: test/library_checker/math/factorize.test.py
---
