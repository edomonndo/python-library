---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/enumerative_combinatorics/number_of_subsequences.test.py
    title: test/library_checker/enumerative_combinatorics/number_of_subsequences.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "MOD = 998244353\n\nfrom collections import defaultdict\n\n\ndef solve(A:\
    \ list[int]) -> int:\n    n = len(A)\n\n    dp = defaultdict(int)\n    ans = 1\n\
    \n    for a in A:\n        tmp = dp[a]\n        dp[a] = ans\n        ans = (ans\
    \ * 2 - tmp) % MOD\n\n    # \u7A7A\u5217\u306F\u542B\u3081\u306A\u3044\n    return\
    \ (ans - 1) % MOD\n"
  dependsOn: []
  isVerificationFile: false
  path: enumerative_combinatorics/number_of_subsequences.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/enumerative_combinatorics/number_of_subsequences.test.py
documentation_of: enumerative_combinatorics/number_of_subsequences.py
layout: document
title: Number of Subsequences
---
