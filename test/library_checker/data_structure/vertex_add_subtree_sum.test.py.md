---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: tree/euler_tour.py
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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_subtree_sum\n\
    from tree.euler_tour import EulerTour\n\nn, q = map(int, input().split())\nA =\
    \ [int(x) for x in input().split()]\nP = [int(x) for x in input().split()]\ng\
    \ = [[] for _ in range(n)]\nfor v, p in enumerate(P, 1):\n    g[p].append((v,\
    \ 1))\n    g[v].append((p, 1))\n\net = EulerTour(g, 0, A)\nans = []\nfor _ in\
    \ range(q):\n    t, *qu = map(int, input().split())\n    if t == 0:\n        a,\
    \ b = qu\n        cur = A[a]\n        et.update_verticle(a, cur + b)\n       \
    \ A[a] = cur + b\n    else:\n        a = qu[0]\n        ans.append(et.subtree_verticle_sum(a))\n\
    print(*ans, sep=\"\\n\")\n"
  dependsOn:
  - tree/euler_tour.py
  isVerificationFile: true
  path: test/library_checker/data_structure/vertex_add_subtree_sum.test.py
  requiredBy: []
  timestamp: '2024-04-24 11:17:49+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/vertex_add_subtree_sum.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/vertex_add_subtree_sum.test.py
- /verify/test/library_checker/data_structure/vertex_add_subtree_sum.test.py.html
title: test/library_checker/data_structure/vertex_add_subtree_sum.test.py
---