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
    PROBLEM: https://judge.yosupo.jp/problem/vertex_add_path_sum
    links:
    - https://judge.yosupo.jp/problem/vertex_add_path_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum\n\
    \nfrom tree.euler_tour import EulerTour\n\nn, q = map(int, input().split())\n\
    A = [int(x) for x in input().split()]\ng = [[] for _ in range(n)]\nfor _ in range(n\
    \ - 1):\n    u, v = map(int, input().split())\n    g[u].append((v, 1))\n    g[v].append((u,\
    \ 1))\net = EulerTour(g, 0, A)\nans = []\nfor _ in range(q):\n    t, a, b = map(int,\
    \ input().split())\n    if t == 0:\n        cur = A[a]\n        et.update_verticle(a,\
    \ cur + b)\n        A[a] = cur + b\n    else:\n        ans.append(et.path_verticle_sum(a,\
    \ b))\nprint(*ans, sep=\"\\n\")\n"
  dependsOn:
  - tree/euler_tour.py
  isVerificationFile: true
  path: test/library_checker/data_structure/vertex_add_path_sum_et.test.py
  requiredBy: []
  timestamp: '2024-06-07 10:09:10+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/vertex_add_path_sum_et.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/vertex_add_path_sum_et.test.py
- /verify/test/library_checker/data_structure/vertex_add_path_sum_et.test.py.html
title: test/library_checker/data_structure/vertex_add_path_sum_et.test.py
---
