---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: polynomial/product_tree.py
    title: polynomial/product_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/polynomial_interpolation
    links:
    - https://judge.yosupo.jp/problem/polynomial_interpolation
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/polynomial_interpolation

    from polynomial.product_tree import ProductTree



    n = int(input())

    xs = [int(x) for x in input().split()]

    ys = [int(x) for x in input().split()]

    T = ProductTree(xs)

    print(*T.polynomial_interpolation(ys))

    '
  dependsOn:
  - polynomial/product_tree.py
  isVerificationFile: true
  path: test/library_checker/polynomial/polynomial_interpolation.test.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/polynomial/polynomial_interpolation.test.py
layout: document
redirect_from:
- /verify/test/library_checker/polynomial/polynomial_interpolation.test.py
- /verify/test/library_checker/polynomial/polynomial_interpolation.test.py.html
title: test/library_checker/polynomial/polynomial_interpolation.test.py
---
