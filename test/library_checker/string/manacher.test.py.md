---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: string_/manacher.py
    title: Manacher
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/enumerate_palindromes
    links:
    - https://judge.yosupo.jp/problem/enumerate_palindromes
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/enumerate_palindromes\n\
    \nfrom string_.manacher import manacher\n\nS = input()\nN = len(S)\nl1, l2 = manacher(S)\n\
    \nans = [-1] * (2 * N - 1)\nfor i in range(N):\n    ans[2 * i] = 2 * l1[i] + 1\n\
    \    if i < N - 1:\n        ans[2 * i + 1] = 2 * l2[i]\nprint(*ans)\n"
  dependsOn:
  - string_/manacher.py
  isVerificationFile: true
  path: test/library_checker/string/manacher.test.py
  requiredBy: []
  timestamp: '2023-08-06 23:53:12+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/string/manacher.test.py
layout: document
redirect_from:
- /verify/test/library_checker/string/manacher.test.py
- /verify/test/library_checker/string/manacher.test.py.html
title: test/library_checker/string/manacher.test.py
---
