---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: str/longest_common_substring.py
    title: Longest Common Substring
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/longest_common_substring
    links:
    - https://judge.yosupo.jp/problem/longest_common_substring
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/longest_common_substring


    from str.longest_common_substring import find_lcs_idx


    S = input()

    T = input()

    print(*find_lcs_idx(S, T))

    '
  dependsOn:
  - str/longest_common_substring.py
  isVerificationFile: true
  path: test/library_checker/string/longeset_common_substring.test.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/string/longeset_common_substring.test.py
layout: document
redirect_from:
- /verify/test/library_checker/string/longeset_common_substring.test.py
- /verify/test/library_checker/string/longeset_common_substring.test.py.html
title: test/library_checker/string/longeset_common_substring.test.py
---
