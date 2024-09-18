---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind
    links:
    - https://judge.yosupo.jp/problem/unionfind
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind\n\
    \nfrom data_structure.basic.unionfind import UnionFind\n\nN, Q = map(int, input().split())\n\
    UF = UnionFind(N)\n\nfor _ in range(Q):\n    t, u, v = map(int, input().split())\n\
    \n    if t == 0:\n        UF.merge(u, v)\n\n    elif t == 1:\n        print(1\
    \ if UF.same(u, v) else 0)\n"
  dependsOn: []
  isVerificationFile: true
  path: test/library_checker/data_structure/unionfind.test.py
  requiredBy: []
  timestamp: '2024-05-21 07:51:26+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/unionfind.test.py
layout: document
title: Unionfind
---
