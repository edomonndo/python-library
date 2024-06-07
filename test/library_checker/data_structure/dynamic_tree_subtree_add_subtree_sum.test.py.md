---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/offline_dynamic_connectivity.py
    title: "\u9023\u7D50\u6027\u5224\u5B9A\uFF08\u30AA\u30D5\u30E9\u30A4\u30F3\uFF09"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/dynamic_tree_subtree_add_subtree_sum
    links:
    - https://judge.yosupo.jp/problem/dynamic_tree_subtree_add_subtree_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/dynamic_tree_subtree_add_subtree_sum\n\
    \nfrom data_structure.offline_dynamic_connectivity import OfflineDynamicConnectivity\n\
    \nn, q = map(int, input().split())\nA = [int(x) for x in input().split()]\nedges\
    \ = [tuple(map(int, input().split())) for _ in range(n - 1)]\n\ndc = OfflineDynamicConnectivity(n)\n\
    for i, a in enumerate(A):\n    dc.add_value(i, a)\ndc.build(edges)\n\nqs = [list(map(int,\
    \ input().split())) for _ in range(q)]\nfor t, *qu in qs:\n    if t == 0:\n  \
    \      u, v, w, x = qu\n        dc.delete_edge(u, v)\n        dc.add_edge(w, x)\n\
    \    else:\n        v, p = qu[:2]\n        dc.delete_edge(v, p)\n        dc.add_edge(v,\
    \ p)\n\n        \n\n\ndef out(k):\n    if k == 0:\n        return\n    k -= 1\n\
    \    t, *qu = qs[k // 2]\n    if t == 0 or k & 1:\n        return\n    if t ==\
    \ 1:\n        v, p, x = qu\n        dc.add_value_group(v, x)\n    else:\n    \
    \    v, p = qu\n        print(dc.uf.group_sum(v))\n\n\ndc.run(out)\n"
  dependsOn:
  - data_structure/offline_dynamic_connectivity.py
  isVerificationFile: true
  path: test/library_checker/data_structure/dynamic_tree_subtree_add_subtree_sum.test.py
  requiredBy: []
  timestamp: '2024-05-01 09:54:30+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/dynamic_tree_subtree_add_subtree_sum.test.py
layout: document
title: Dynamic Tree Subtree Add Subtree Sum
---
