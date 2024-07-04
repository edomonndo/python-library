---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: graph/connectivity/offline_dynamic_connectivity.py
    title: Dynamic Connectivity (Offline)
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/dynamic_tree_vertex_add_subtree_sum
    links:
    - https://judge.yosupo.jp/problem/dynamic_tree_vertex_add_subtree_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/dynamic_tree_vertex_add_subtree_sum\n\
    \nfrom graph.connectivity.offline_dynamic_connectivity import OfflineDynamicConnectivity\n\
    \nn, q = map(int, input().split())\nA = [int(x) for x in input().split()]\nedges\
    \ = [tuple(map(int, input().split())) for _ in range(n - 1)]\n\ndc = OfflineDynamicConnectivity(n)\n\
    for i, a in enumerate(A):\n    dc.add_value(i, a)\ndc.build(edges)\n\nqs = [list(map(int,\
    \ input().split())) for _ in range(q)]\nfor t, *qu in qs:\n    if t == 0:\n  \
    \      u, v, w, x = qu\n        dc.delete_edge(u, v)\n        dc.add_edge(w, x)\n\
    \    elif t == 1:\n        dc.add_relax()\n        dc.add_relax()\n    else:\n\
    \        v, p = qu\n        dc.delete_edge(v, p)\n        dc.add_edge(v, p)\n\n\
    \ndef out(k):\n    if k == 0:\n        return\n    k -= 1\n    t, *qu = qs[k >>\
    \ 1]\n    if t == 0 or k & 1:\n        return\n    if t == 1:\n        v, x =\
    \ qu\n        dc.add_value(v, x)\n    else:\n        v, _ = qu\n        print(dc.group_sum(v))\n\
    \n\ndc.run(out)\n"
  dependsOn:
  - graph/connectivity/offline_dynamic_connectivity.py
  isVerificationFile: true
  path: test/library_checker/tree/dynamic_tree_vertex_add_subtree_sum.test.py
  requiredBy: []
  timestamp: '2024-07-02 07:37:15+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/tree/dynamic_tree_vertex_add_subtree_sum.test.py
layout: document
title: Dynamic Tree Vertex Add Subtree Sum
---