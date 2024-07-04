---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: atcoder/fenwicktree.py
    title: atcoder/fenwicktree.py
  - icon: ':question:'
    path: graph/tree/contour_query.py
    title: "\u7B49\u9AD8\u7DDA\u30AF\u30A8\u30EA"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/vertex_add_range_contour_sum_on_tree
    links:
    - https://judge.yosupo.jp/problem/vertex_add_range_contour_sum_on_tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_range_contour_sum_on_tree\n\
    \n\nfrom atcoder.fenwicktree import FenwickTree\nfrom graph.tree.contour_query\
    \ import ContourQuery\n\n\nn, q = map(int, input().split())\nA = [int(x) for x\
    \ in input().split()]\ng = [[] for _ in range(n)]\nfor _ in range(n - 1):\n  \
    \  u, v = map(int, input().split())\n    g[u].append(v)\n    g[v].append(u)\n\n\
    bit = []\n\n\ndef f(arr):\n    for i in range(len(arr)):\n        B = [0] * len(arr[i])\n\
    \        for j in range(len(arr[i])):\n            B[j] = A[arr[i][j]]\n     \
    \   bit.append(FenwickTree(len(arr[i])))\n        for j in range(len(arr[i])):\n\
    \            bit[-1].add(j, B[j])\n\n\ndef query1(p, r):\n    global ans\n   \
    \ ans += bit[p]._sum(r)\n\n\ndef query2(p, r):\n    global ans\n    ans -= bit[p]._sum(r)\n\
    \n\ncq = ContourQuery(g, f)\n\nfor _ in range(q):\n    t, *qu = map(int, input().split())\n\
    \    if t == 0:\n        p, x = qu\n        cq.vertex(p, lambda a, b: bit[a].add(b,\
    \ x))\n    else:\n        p, l, r = qu\n        ans = 0\n        cq.range_contour(p,\
    \ l, r, query1, query2)\n        print(ans)\n"
  dependsOn:
  - atcoder/fenwicktree.py
  - graph/tree/contour_query.py
  isVerificationFile: true
  path: test/library_checker/tree/vertex_add_range_contour_sum_on_tree.test.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/tree/vertex_add_range_contour_sum_on_tree.test.py
layout: document
title: Vertex Add Range Contour Sum on Tree
---
