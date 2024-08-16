---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: number_theory/primitive_root.py
    title: "\u539F\u59CB\u6839"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/primitive_root
    links:
    - https://judge.yosupo.jp/problem/primitive_root
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/primitive_root\n\
    \nfrom number_theory.primitive_root import primitive_root\n\n\nq = int(input())\n\
    for _ in range(q):\n    p = int(input())\n    print(primitive_root(p))\n"
  dependsOn:
  - number_theory/primitive_root.py
  isVerificationFile: true
  path: test/library_checker/number_theory/primitive_root.test.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/number_theory/primitive_root.test.py
layout: document
title: Primitive Root
---