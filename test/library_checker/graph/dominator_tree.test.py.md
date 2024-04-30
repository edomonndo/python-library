---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: tree/dominator_tree.py
    title: Dominator Tree
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/dominatortree
    links:
    - https://judge.yosupo.jp/problem/dominatortree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/dominatortree\n\
    \nfrom tree.dominator_tree import dominator_tree\n\nn, m, r = map(int, input().split())\n\
    g = [[] for _ in range(n)]\nfor _ in range(m):\n    u, v = map(int, input().split())\n\
    \    g[u].append(v)\n\nprint(*dominator_tree(g, r))\n"
  dependsOn:
  - tree/dominator_tree.py
  isVerificationFile: true
  path: test/library_checker/graph/dominator_tree.test.py
  requiredBy: []
  timestamp: '2024-04-30 09:44:21+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/dominator_tree.test.py
layout: document
redirect_from:
- /verify/test/library_checker/graph/dominator_tree.test.py
- /verify/test/library_checker/graph/dominator_tree.test.py.html
title: test/library_checker/graph/dominator_tree.test.py
---
