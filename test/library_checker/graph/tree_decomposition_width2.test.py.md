---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: graph/tree_decomposition_width2.py
    title: "\u6728\u5206\u89E3\uFF08\u6728\u5E45\uFF12\u4EE5\u4E0B\uFF09"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/tree_decomposition_width_2
    links:
    - https://judge.yosupo.jp/problem/tree_decomposition_width_2
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/tree_decomposition_width_2\n\
    \nfrom graph.tree_decomposition_width2 import TreeDecompositionWidth2\n\np, tw,\
    \ n, m = input().split()\nn, m = int(n), int(m)\nedges = [tuple(map(lambda x:\
    \ int(x) - 1, input().split())) for _ in range(m)]\n\ng = TreeDecompositionWidth2(n,\
    \ edges)\nres = g.build()\nif res is None:\n    print(-1)\nelse:\n    bag, edges\
    \ = res\n    k = len(bag)\n    print(\"s\", \"td\", k, 2, n)\n    for i in range(k):\n\
    \        print(\"b\", i + 1, *[v + 1 for v in bag[i]])\n    for u, v in edges:\n\
    \        print(u + 1, v + 1)\n"
  dependsOn:
  - graph/tree_decomposition_width2.py
  isVerificationFile: true
  path: test/library_checker/graph/tree_decomposition_width2.test.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/graph/tree_decomposition_width2.test.py
layout: document
title: Tree Decomposition (Width 2)
---

