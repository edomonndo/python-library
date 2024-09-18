---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/connectivity/offline_dynamic_connectivity.py
    title: Dynamic Connectivity (Offline)
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/dynamic_graph_vertex_add_component_sum
    links:
    - https://judge.yosupo.jp/problem/dynamic_graph_vertex_add_component_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/dynamic_graph_vertex_add_component_sum\n\
    \nfrom graph.connectivity.offline_dynamic_connectivity import OfflineDynamicConnectivity\n\
    \nn, q = map(int, input().split())\nA = [int(x) for x in input().split()]\ndc\
    \ = OfflineDynamicConnectivity(n)\nfor i, a in enumerate(A):\n    dc.add_value(i,\
    \ a)\nqs = [list(map(int, input().split())) for _ in range(q)]\nfor t, *qu in\
    \ qs:\n    if t == 0:\n        u, v = qu\n        dc.add_edge(u, v)\n    elif\
    \ t == 1:\n        u, v = qu\n        dc.delete_edge(u, v)\n    else:\n      \
    \  dc.add_relax()\n\n\ndef out(k):\n    t, *qu = qs[k]\n    if t == 2:\n     \
    \   v, x = qu\n        dc.uf.add(v, x)\n    elif t == 3:\n        v = qu[0]\n\
    \        print(dc.uf.group_sum(v))\n\n\ndc.run(out)\n"
  dependsOn:
  - graph/connectivity/offline_dynamic_connectivity.py
  isVerificationFile: true
  path: test/library_checker/graph/dynamic_graph_vertex_add_component_sum_offline.test.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/dynamic_graph_vertex_add_component_sum_offline.test.py
layout: document
title: Dynamic Graph Vertex Add Component Sum (Offline)
---
