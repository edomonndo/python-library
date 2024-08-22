---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: number_theory/kth_root.py
    title: Kth Root
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/kth_root_integer
    links:
    - https://judge.yosupo.jp/problem/kth_root_integer
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/kth_root_integer\n\
    \nfrom number_theory.kth_root import KthRoot\n\nt = int(input())\nfor _ in range(t):\n\
    \    a, k = map(int, input().split())\n    print(KthRoot.floor(a, k))\n"
  dependsOn:
  - number_theory/kth_root.py
  isVerificationFile: true
  path: test/library_checker/number_theory/kth_root_integer.test.py
  requiredBy: []
  timestamp: '2024-08-22 11:33:17+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/number_theory/kth_root_integer.test.py
layout: document
title: Kth Root (Integer)
---
