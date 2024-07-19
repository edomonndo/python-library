---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/tree/euler_tour.py
    title: Euler tour
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/vertex_add_subtree_sum
    links:
    - https://judge.yosupo.jp/problem/vertex_add_subtree_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_subtree_sum\n\
    from graph.tree.euler_tour import EulerTour\n\nn, q = map(int, input().split())\n\
    A = [int(x) for x in input().split()]\nP = [int(x) for x in input().split()]\n\
    g = [[] for _ in range(n)]\nfor v, p in enumerate(P, 1):\n    g[p].append((v,\
    \ 1))\n    g[v].append((p, 1))\n\net = EulerTour(g, 0, A)\nans = []\nfor _ in\
    \ range(q):\n    t, *qu = map(int, input().split())\n    if t == 0:\n        a,\
    \ b = qu\n        cur = A[a]\n        et.update_verticle(a, cur + b)\n       \
    \ A[a] = cur + b\n    else:\n        a = qu[0]\n        ans.append(et.subtree_verticle_sum(a))\n\
    print(*ans, sep=\"\\n\")\n"
  dependsOn:
  - graph/tree/euler_tour.py
  isVerificationFile: true
  path: test/library_checker/tree/vertex_add_subtree_sum_et.test.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/tree/vertex_add_subtree_sum_et.test.py
layout: document
title: Vertex Add Subtree Sum (Euler Tour)
---
