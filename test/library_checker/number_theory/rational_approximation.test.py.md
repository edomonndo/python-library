---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: number_theory/stern_brocot_tree.py
    title: Stern Brocot tree
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/https://judge.yosupo.jp/problem/rational_approximation
    links:
    - https://judge.yosupo.jp/problem/https://judge.yosupo.jp/problem/rational_approximation
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/https://judge.yosupo.jp/problem/rational_approximation\n\
    \n\nfrom number_theory.stern_brocot_tree import SternBrocotTree\n\nt = int(input())\n\
    for _ in range(t):\n    n, x, y = map(int, input().split())\n    a, b, c, d =\
    \ SternBrocotTree.approx(n, x, y)\n    print(a, b, c, d)\n"
  dependsOn:
  - number_theory/stern_brocot_tree.py
  isVerificationFile: true
  path: test/library_checker/number_theory/rational_approximation.test.py
  requiredBy: []
  timestamp: '2024-08-22 11:09:04+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/number_theory/rational_approximation.test.py
layout: document
title: Rational Approximation
---
