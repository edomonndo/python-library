---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: string_/z_algorithm.py
    title: Z algorithm
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/zalgorithm
    links:
    - https://judge.yosupo.jp/problem/zalgorithm
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/zalgorithm


    from string_.z_algorithm import z_algorithm


    S = input()

    array = z_algorithm(S)

    print(*array)

    '
  dependsOn:
  - string_/z_algorithm.py
  isVerificationFile: true
  path: test/library_checker/string/z_algorithm.test.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/string/z_algorithm.test.py
layout: document
redirect_from:
- /verify/test/library_checker/string/z_algorithm.test.py
- /verify/test/library_checker/string/z_algorithm.test.py.html
title: test/library_checker/string/z_algorithm.test.py
---
