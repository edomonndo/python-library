---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/fenwick_tree/range_add_point_get.py
    title: "\u533A\u9593\u52A0\u7B97\u30FB1\u70B9\u53D6\u5F97"
  - icon: ':question:'
    path: graph/tree/contour_query.py
    title: "\u7B49\u9AD8\u7DDA\u30AF\u30A8\u30EA"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/vertex_get_range_contour_add_on_tree
    links:
    - https://judge.yosupo.jp/problem/vertex_get_range_contour_add_on_tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_get_range_contour_add_on_tree\n\
    \nfrom data_structure.fenwick_tree.range_add_point_get import RangeAddPointGet\n\
    from graph.tree.contour_query import ContourQuery\n\n\nn, q = map(int, input().split())\n\
    A = [int(x) for x in input().split()]\ng = [[] for _ in range(n)]\nfor _ in range(n\
    \ - 1):\n    u, v = map(int, input().split())\n    g[u].append(v)\n    g[v].append(u)\n\
    \nbit = []\n\n\ndef f(arr):\n    for i in range(len(arr)):\n        bit.append(RangeAddPointGet(len(arr[i])))\n\
    \n\ndef query(p, k):\n    global ans\n    ans += bit[p].get(k)\n\n\ncq = ContourQuery(g,\
    \ f)\n\nfor _ in range(q):\n    t, *qu = map(int, input().split())\n    if t ==\
    \ 0:\n        p, l, r, x = qu\n        cq.range_contour(\n            p, l, r,\
    \ lambda p, r: bit[p].add(0, r, x), lambda p, r: bit[p].add(0, r, -x)\n      \
    \  )\n    else:\n        p = qu[0]\n        ans = A[p]\n        cq.vertex(p, query)\n\
    \        print(ans)\n"
  dependsOn:
  - data_structure/fenwick_tree/range_add_point_get.py
  - graph/tree/contour_query.py
  isVerificationFile: true
  path: test/library_checker/tree/vertex_get_range_contour_add_on_tree.test.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/tree/vertex_get_range_contour_add_on_tree.test.py
layout: document
title: Vertex Get Range Contour Add on Tree
---
