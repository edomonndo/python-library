---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: math_/count_primes.py
    title: "\u7D20\u6570\u6570\u3048\u4E0A\u3052"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/counting_primes
    links:
    - https://judge.yosupo.jp/problem/counting_primes
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/counting_primes


    from math_.count_primes import count_primes


    N = int(input())

    print(count_primes(N))

    '
  dependsOn:
  - math_/count_primes.py
  isVerificationFile: true
  path: library_checker/math/count_primes.test.py
  requiredBy: []
  timestamp: '2023-06-21 21:40:34+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: library_checker/math/count_primes.test.py
layout: document
redirect_from:
- /verify/library_checker/math/count_primes.test.py
- /verify/library_checker/math/count_primes.test.py.html
title: library_checker/math/count_primes.test.py
---