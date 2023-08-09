---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/lca
    links:
    - https://judge.yosupo.jp/problem/lca
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca\n\nfrom\
    \ tree.lca import LcaDoubling\n\nN, Q = map(int, input().split())\nparent = list(map(int,\
    \ input().split()))\nG = [[] for _ in range(N)]\nfor v, p in enumerate(parent,\
    \ start=1):\n    G[v].append(p)\n    G[p].append(v)\n\nlca = LcaDoubling(N, G)\n\
    for _ in range(Q):\n    u, v = map(int, input().split())\n    print(lca.lca(u,\
    \ v))\n"
  dependsOn: []
  isVerificationFile: true
  path: test/library_checker/tree/lowest_common_ancestor.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/tree/lowest_common_ancestor.test.py
layout: document
redirect_from:
- /verify/test/library_checker/tree/lowest_common_ancestor.test.py
- /verify/test/library_checker/tree/lowest_common_ancestor.test.py.html
title: test/library_checker/tree/lowest_common_ancestor.test.py
---