---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: math_/factorial_iter_mod.py
    title: "\u968E\u4E57\u30AF\u30A8\u30EA mod 998244353"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/many_factorials
    links:
    - https://judge.yosupo.jp/problem/many_factorials
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/many_factorials


    from math_.factorial_iter_mod import factorial_iter_mod



    t = int(input())

    qs = [int(input()) for _ in range(t)]

    ans = factorial_iter_mod(qs)

    print(*ans, sep="\n")

    '
  dependsOn:
  - math_/factorial_iter_mod.py
  isVerificationFile: true
  path: test/library_checker/math/many_factorials.test.py
  requiredBy: []
  timestamp: '2024-06-12 17:23:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/math/many_factorials.test.py
layout: document
redirect_from:
- /verify/test/library_checker/math/many_factorials.test.py
- /verify/test/library_checker/math/many_factorials.test.py.html
title: test/library_checker/math/many_factorials.test.py
---
