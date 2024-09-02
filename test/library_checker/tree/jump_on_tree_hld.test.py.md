---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: graph/tree/heavy_light_decomposition.py
    title: "HL\u5206\u89E3"
  - icon: ':heavy_check_mark:'
    path: graph/tree/template.py
    title: graph/tree/template.py
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
    \nfrom graph.tree.template import Tree\nfrom graph.tree.heavy_light_decomposition\
    \ import HeavyLightDecomposition\n\nn, q = map(int, input().split())\ng = Tree.from_input(n,\
    \ 0)\n\nT = HeavyLightDecomposition(n, g)\nfor _ in range(q):\n    s, t, k = map(int,\
    \ input().split())\n    print(T.jump(s, t, k))\n"
  dependsOn:
  - graph/tree/template.py
  - graph/tree/heavy_light_decomposition.py
  isVerificationFile: true
  path: test/library_checker/tree/jump_on_tree_hld.test.py
  requiredBy: []
  timestamp: '2024-09-02 10:45:19+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/tree/jump_on_tree_hld.test.py
layout: document
title: Jump on Tree (HLD)
---
