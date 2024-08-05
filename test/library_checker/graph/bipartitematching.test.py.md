---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/bipartite_matching.py
    title: "\u4E8C\u90E8\u30B0\u30E9\u30D5\u30DE\u30C3\u30C1\u30F3\u30B0"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bipartitematching
    links:
    - https://judge.yosupo.jp/problem/bipartitematching
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bipartitematching\n\
    \nfrom graph.bipartite_matching import bipartite_matching\n\n\nL, R, m = map(int,\
    \ input().split())\nedges = [tuple(map(int, input().split())) for _ in range(m)]\n\
    ans = bipartite_matching(L, R, edges)\nprint(len(ans))\nfor u, v in ans:\n   \
    \ print(u, v)\n"
  dependsOn:
  - graph/bipartite_matching.py
  isVerificationFile: true
  path: test/library_checker/graph/bipartitematching.test.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/bipartitematching.test.py
layout: document
title: Matching on Bipartite Graph
---

