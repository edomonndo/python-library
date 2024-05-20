---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: tree/lca.py
    title: "\u6700\u8FD1\u5171\u901A\u7956\u5148(Lowest Common Ancestor)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/jump_on_tree
    links:
    - https://judge.yosupo.jp/problem/jump_on_tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/jump_on_tree\n\
    \nfrom tree.lca import LcaDoubling\n\nN, Q = map(int, input().split())\nG = [[]\
    \ for _ in range(N)]\nfor _ in range(N - 1):\n    a, b = map(int, input().split())\n\
    \    G[a].append(b)\n    G[b].append(a)\n\nlca = LcaDoubling(N, G)\nfor _ in range(Q):\n\
    \    s, t, i = map(int, input().split())\n    print(lca.jump(s, t, i))\n"
  dependsOn:
  - tree/lca.py
  isVerificationFile: true
  path: test/library_checker/tree/jump_on_tree.test.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/tree/jump_on_tree.test.py
layout: document
redirect_from:
- /verify/test/library_checker/tree/jump_on_tree.test.py
- /verify/test/library_checker/tree/jump_on_tree.test.py.html
title: test/library_checker/tree/jump_on_tree.test.py
---
