---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: convolution/product_tree.py
    title: convolution/product_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/polynomial_interpolation
    links:
    - https://judge.yosupo.jp/problem/polynomial_interpolation
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/polynomial_interpolation

    from convolution.product_tree import ProductTree



    n = int(input())

    xs = [int(x) for x in input().split()]

    ys = [int(x) for x in input().split()]

    T = ProductTree(xs)

    print(*T.polynomial_interpolation(ys))

    '
  dependsOn:
  - convolution/product_tree.py
  isVerificationFile: true
  path: test/library_checker/polynomial/polynomial_interpolation.test.py
  requiredBy: []
  timestamp: '2024-06-20 12:15:41+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/polynomial/polynomial_interpolation.test.py
layout: document
redirect_from:
- /verify/test/library_checker/polynomial/polynomial_interpolation.test.py
- /verify/test/library_checker/polynomial/polynomial_interpolation.test.py.html
title: test/library_checker/polynomial/polynomial_interpolation.test.py
---
