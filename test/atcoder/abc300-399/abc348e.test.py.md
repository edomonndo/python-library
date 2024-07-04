---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/tree/centroids.py
    title: "\u91CD\u5FC3\u5224\u5B9A"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/abc348/tasks/abc348_e
    links:
    - https://atcoder.jp/contests/abc348/tasks/abc348_e
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc348/tasks/abc348_e\n\
    \nfrom graph.tree.centroids import centroids\n\nn = int(input())\ng = [[] for\
    \ _ in range(n)]\nfor _ in range(n - 1):\n    u, v = map(int, input().split())\n\
    \    u -= 1\n    v -= 1\n    g[u].append(v)\n    g[v].append(u)\nC = [int(x) for\
    \ x in input().split()]\n\ncenter = centroids(g, C)\n\nans = 0\nstack = [(center[0],\
    \ -1, 1)]\nwhile stack:\n    v, p, d = stack.pop()\n    for u in g[v]:\n     \
    \   if u != p:\n            ans += C[u] * d\n            stack.append((u, v, d\
    \ + 1))\nprint(ans)\n"
  dependsOn:
  - graph/tree/centroids.py
  isVerificationFile: true
  path: test/atcoder/abc300-399/abc348e.test.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/abc300-399/abc348e.test.py
layout: document
title: E - Minimize Sum of Distances
---
