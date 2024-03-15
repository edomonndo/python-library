---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: persistent_data_structure/persistent_union_find.py
    title: persistent_data_structure/persistent_union_find.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/persistent_unionfind
    links:
    - https://judge.yosupo.jp/problem/persistent_unionfind
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/persistent_unionfind\n\
    from persistent_data_structure.persistent_union_find import PersistentUnionFind\n\
    \nN, Q = map(int, input().split())\nG = PersistentUnionFind(N)\nfor _ in range(Q):\n\
    \    t, k, u, v = map(int, input().split())\n    if t == 0:\n        G.merge(k,\
    \ u, v)\n    else:\n        print(1 if G.same(k, u, v) else 0)\n        G.update()\n"
  dependsOn:
  - persistent_data_structure/persistent_union_find.py
  isVerificationFile: true
  path: test/library_checker/data_structure/persistent_unionfind2.test.py
  requiredBy: []
  timestamp: '2024-02-24 06:05:31+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/persistent_unionfind2.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/persistent_unionfind2.test.py
- /verify/test/library_checker/data_structure/persistent_unionfind2.test.py.html
title: test/library_checker/data_structure/persistent_unionfind2.test.py
---
