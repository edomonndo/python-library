---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: string_/suffix_array.py
    title: Suffix array
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/suffixarray
    links:
    - https://judge.yosupo.jp/problem/suffixarray
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/suffixarray


    from string_.suffix_array import suffix_array


    S = input()

    sa = suffix_array(S)

    print(*sa)

    '
  dependsOn:
  - string_/suffix_array.py
  isVerificationFile: true
  path: test/library_checker/string/suffix_array.test.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/string/suffix_array.test.py
layout: document
redirect_from:
- /verify/test/library_checker/string/suffix_array.test.py
- /verify/test/library_checker/string/suffix_array.test.py.html
title: test/library_checker/string/suffix_array.test.py
---