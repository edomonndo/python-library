---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/lca
    links:
    - https://judge.yosupo.jp/problem/lca
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca\n\nfrom\
    \ tree.lca import LcaDoubling\n\nN, Q = map(int, input().split())\nparent = list(map(int,\
    \ input().split()))\nG = [[] for _ in range(N)]\nfor v, p in enumerate(parent,\
    \ start=1):\n    G[v].append(p)\n    G[p].append(v)\n\nlca = LcaDoubling(N, G)\n\
    for _ in range(Q):\n    u, v = map(int, input().split())\n    print(lca.lca(u,\
    \ v))\n"
  dependsOn: []
  isVerificationFile: true
  path: library_checker/tree/lowest_common_ancestor.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: library_checker/tree/lowest_common_ancestor.test.py
layout: document
redirect_from:
- /verify/library_checker/tree/lowest_common_ancestor.test.py
- /verify/library_checker/tree/lowest_common_ancestor.test.py.html
title: library_checker/tree/lowest_common_ancestor.test.py
---
