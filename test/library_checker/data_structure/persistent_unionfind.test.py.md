---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/rollback_unionfind.py
    title: Rollback Union Find
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
    \nfrom data_structure.rollback_unionfind import RollbackUnionFind\n\nN, Q = map(int,\
    \ input().split())\nG = [[] for _ in range(Q + 1)]\n\nfor i in range(1, Q + 1):\n\
    \    t, k, u, v = map(int, input().split())\n    k += 1\n    G[k].append((t, i,\
    \ u, v, 1))\n\nuf = RollbackUnionFind(N)\nans = [-1] * (Q + 1)\nstack = [(-1,\
    \ 0, -1, 0, 1)]\nwhile stack:\n    t, k, u, v, flag = stack.pop()\n    if t ==\
    \ 1:\n        ans[k] = uf.same(u, v)\n        continue\n    if flag:\n       \
    \ stack.append((t, k, u, v, 0))\n        if t == 0:\n            uf.merge(u, v)\n\
    \        for item in G[k]:\n            stack.append(item)\n        continue\n\
    \    if t == 0:\n        uf.undo()\n\nfor x in ans:\n    if x != -1:\n       \
    \ print(1 if x else 0)\n"
  dependsOn:
  - data_structure/rollback_unionfind.py
  isVerificationFile: true
  path: test/library_checker/data_structure/persistent_unionfind.test.py
  requiredBy: []
  timestamp: '2024-04-30 11:25:39+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/persistent_unionfind.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/persistent_unionfind.test.py
- /verify/test/library_checker/data_structure/persistent_unionfind.test.py.html
title: test/library_checker/data_structure/persistent_unionfind.test.py
---
