---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/bipartite_matching.py
    title: graph/bipartite_matching.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bipartitematching
    links:
    - https://judge.yosupo.jp/problem/bipartitematching
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bipartitematching\n\
    \nfrom graph.bipartite_matching import BipartiteMatching\n\n\nL, R, K = map(int,\
    \ input().split())\nbm = BipartiteMatching(L, R)\nfor _ in range(K):\n    a, b\
    \ = map(int, input().split())\n    bm.add_edge(a, b)\nres = bm.solve()\nprint(len(res))\n\
    for a, b in res:\n    print(a, b)\n"
  dependsOn:
  - graph/bipartite_matching.py
  isVerificationFile: true
  path: test/library_checker/graph/bipartitematching.test.py
  requiredBy: []
  timestamp: '2024-02-09 16:12:14+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/bipartitematching.test.py
layout: document
redirect_from:
- /verify/test/library_checker/graph/bipartitematching.test.py
- /verify/test/library_checker/graph/bipartitematching.test.py.html
title: test/library_checker/graph/bipartitematching.test.py
---
