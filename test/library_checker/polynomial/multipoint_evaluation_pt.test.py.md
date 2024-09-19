---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: polynomial/product_tree.py
    title: Product Tree
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/multipoint_evaluation
    links:
    - https://judge.yosupo.jp/problem/multipoint_evaluation
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/multipoint_evaluation

    from polynomial.product_tree import ProductTree


    n, m = map(int, input().split())

    C = [int(x) for x in input().split()]

    P = [int(x) for x in input().split()]

    T = ProductTree(P)

    print(*T.multipoint_evaluation(C))

    '
  dependsOn:
  - polynomial/product_tree.py
  isVerificationFile: true
  path: test/library_checker/polynomial/multipoint_evaluation_pt.test.py
  requiredBy: []
  timestamp: '2024-07-02 08:45:17+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/polynomial/multipoint_evaluation_pt.test.py
layout: document
title: Multipoint Evaluation (Product Tree)
---
