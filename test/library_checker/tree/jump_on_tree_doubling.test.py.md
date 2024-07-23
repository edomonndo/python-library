---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/tree/lca.py
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
    \nfrom graph.tree.lca import LcaDoubling\n\nn, q = map(int, input().split())\n\
    g = [[] for _ in range(n)]\nfor _ in range(n - 1):\n    a, b = map(int, input().split())\n\
    \    g[a].append(b)\n    g[b].append(a)\n\nlca = LcaDoubling(n, g)\nfor _ in range(q):\n\
    \    s, t, i = map(int, input().split())\n    print(lca.jump(s, t, i))\n"
  dependsOn:
  - graph/tree/lca.py
  isVerificationFile: true
  path: test/library_checker/tree/jump_on_tree_doubling.test.py
  requiredBy: []
  timestamp: '2024-07-04 13:09:35+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/tree/jump_on_tree_doubling.test.py
layout: document
title: Jump on Tree (Doubling)
---
