---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: string_/manacher.py
    title: string_/manacher.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from string_.manacher import manacher\n\nS = input()\nN = len(S)\nl1, l2\
    \ = manacher(S)\n\nans = [-1] * (2 * N - 1)\nfor i in range(N):\n    ans[2 * i]\
    \ = 2 * l1[i] + 1\n    if i < N - 1:\n        ans[2 * i + 1] = 2 * l2[i]\nprint(*ans)\n"
  dependsOn:
  - string_/manacher.py
  isVerificationFile: true
  path: library_checker/string/manacher.test.py
  requiredBy: []
  timestamp: '2023-07-23 01:42:59+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: library_checker/string/manacher.test.py
layout: document
redirect_from:
- /verify/library_checker/string/manacher.test.py
- /verify/library_checker/string/manacher.test.py.html
title: library_checker/string/manacher.test.py
---
