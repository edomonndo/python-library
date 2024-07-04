---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: atcoder/fenwicktree.py
    title: atcoder/fenwicktree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/vertex_add_subtree_sum
    links:
    - https://judge.yosupo.jp/problem/vertex_add_subtree_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_subtree_sum\n\
    \nfrom atcoder.fenwicktree import FenwickTree\nfrom graph.tree.heavy_light_decomposition\
    \ import HeavyLightDecomposition\n\n\ndef f(x, y):\n    global ans\n    ans +=\
    \ bit.sum(x, y)\n\n\nn, q = map(int, input().split())\nA = [int(x) for x in input().split()]\n\
    P = [int(x) for x in input().split()]\nedges = []\nfor i, p in enumerate(P, 1):\n\
    \    edges.append((i, p))\nH = HeavyLightDecomposition(n, edges, 0)\nL = [0] *\
    \ n\nfor i, a in enumerate(A):\n    L[H.into[i]] = a\nbit = FenwickTree(n)\nfor\
    \ i, p in enumerate(L):\n    bit.add(i, p)\n\nfor _ in range(q):\n    t, *a =\
    \ map(int, input().split())\n    if t == 0:\n        v, x = a\n        p = H.into[v]\n\
    \        bit.add(p, x)\n    else:\n        ans = 0\n        H.subtree_query(a[0],\
    \ f)\n        print(ans)\n"
  dependsOn:
  - atcoder/fenwicktree.py
  isVerificationFile: true
  path: test/library_checker/tree/vertex_add_subtree_sum_hld.test.py
  requiredBy: []
  timestamp: '2024-07-03 10:08:38+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/tree/vertex_add_subtree_sum_hld.test.py
layout: document
title: Vertex Add Subtree Sum (HLD)
---