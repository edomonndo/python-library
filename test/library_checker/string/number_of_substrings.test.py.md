---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: str/suffix_array.py
    title: Suffix array
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/number_of_substrings
    links:
    - https://judge.yosupo.jp/problem/number_of_substrings
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/number_of_substrings


    from str.suffix_array import suffix_array, lcp_array


    S = "_" + input()

    n = len(S)

    sa = suffix_array(S)

    lcp = lcp_array(S, sa)

    print((n * (n - 1) >> 1) - sum(lcp))

    '
  dependsOn:
  - str/suffix_array.py
  isVerificationFile: true
  path: test/library_checker/string/number_of_substrings.test.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/string/number_of_substrings.test.py
layout: document
title: Number of Substrings
---
