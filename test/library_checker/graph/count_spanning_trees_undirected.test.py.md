---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: graph/matrix_tree_theorem.py
    title: "\u884C\u5217\u6728\u5B9A\u7406"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/counting_spanning_tree_undirected
    links:
    - https://judge.yosupo.jp/problem/counting_spanning_tree_undirected
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/counting_spanning_tree_undirected\n\
    \n\nfrom graph.matrix_tree_theorem import MatrixTreeTheorem\n\nn, m, r = map(int,\
    \ input().split())\ng = MatrixTreeTheorem(n, True)\nfor _ in range(m):\n    u,\
    \ v = map(int, input().split())\n    g.add_edge(u, v)\n\nprint(g.solve())\n"
  dependsOn:
  - graph/matrix_tree_theorem.py
  isVerificationFile: true
  path: test/library_checker/graph/count_spanning_trees_undirected.test.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/graph/count_spanning_trees_undirected.test.py
layout: document
title: Counting Spanning Trees (Undirected)
---

