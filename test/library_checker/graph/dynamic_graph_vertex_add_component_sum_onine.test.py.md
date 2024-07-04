---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/connectivity/dynamic_connectivity.py
    title: Dynamic Connectivity (Online)
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
    \nfrom graph.connectivity.dynamic_connectivity import DynamicConnectivity\n\n\
    n, k = map(int, input().split())\ndc = DynamicConnectivity(n, lambda x, y: x +\
    \ y, 0)\nA = [int(x) for x in input().split()]\nfor i, a in enumerate(A):\n  \
    \  dc.update(i, a)\nfor i in range(k):\n    t, *qu = map(int, input().split())\n\
    \    if t == 0:\n        u, v = qu\n        dc.link(u, v)\n    elif t == 1:\n\
    \        u, v = qu\n        dc.cut(u, v)\n    elif t == 2:\n        v, x = qu\n\
    \        dc.update(v, x)\n    else:\n        v = qu[0]\n        print(dc.get_sum(v))\n"
  dependsOn:
  - graph/connectivity/dynamic_connectivity.py
  isVerificationFile: true
  path: test/library_checker/graph/dynamic_graph_vertex_add_component_sum_onine.test.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/dynamic_graph_vertex_add_component_sum_onine.test.py
layout: document
redirect_from:
- /verify/test/library_checker/graph/dynamic_graph_vertex_add_component_sum_onine.test.py
- /verify/test/library_checker/graph/dynamic_graph_vertex_add_component_sum_onine.test.py.html
title: test/library_checker/graph/dynamic_graph_vertex_add_component_sum_onine.test.py
---
