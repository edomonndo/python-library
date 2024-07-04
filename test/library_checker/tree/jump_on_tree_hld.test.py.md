---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: graph/tree/heavy_light_decomposition.py
    title: "HL\u5206\u89E3"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/jump_on_tree
    links:
    - https://judge.yosupo.jp/problem/jump_on_tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/jump_on_tree\n\
    \nfrom graph.tree.heavy_light_decomposition import HeavyLightDecomposition\n\n\
    n, q = map(int, input().split())\nedges = [tuple(map(int, input().split())) for\
    \ _ in range(n)]\n\nT = HeavyLightDecomposition(n, edges)\nfor _ in range(q):\n\
    \    s, t, k = map(int, input().split())\n    print(T.jump(s, t, k))\n"
  dependsOn:
  - graph/tree/heavy_light_decomposition.py
  isVerificationFile: true
  path: test/library_checker/tree/jump_on_tree_hld.test.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/tree/jump_on_tree_hld.test.py
layout: document
redirect_from:
- /verify/test/library_checker/tree/jump_on_tree_hld.test.py
- /verify/test/library_checker/tree/jump_on_tree_hld.test.py.html
title: test/library_checker/tree/jump_on_tree_hld.test.py
---
