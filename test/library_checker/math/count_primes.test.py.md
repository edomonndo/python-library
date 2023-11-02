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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/counting_primes


    from math_.count_primes import count_primes


    N = int(input())

    print(count_primes(N))

    '
  dependsOn:
  - math_/count_primes.py
  isVerificationFile: true
  path: test/library_checker/math/count_primes.test.py
  requiredBy: []
  timestamp: '2023-08-01 14:51:05+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/math/count_primes.test.py
layout: document
redirect_from:
- /verify/test/library_checker/math/count_primes.test.py
- /verify/test/library_checker/math/count_primes.test.py.html
title: test/library_checker/math/count_primes.test.py
---
