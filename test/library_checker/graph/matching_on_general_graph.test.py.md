---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/general_matching.py
    title: "\u6700\u5927\u30DE\u30C3\u30C1\u30F3\u30B0"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/general_matching
    links:
    - https://judge.yosupo.jp/problem/general_matching
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/general_matching\n\
    \nfrom graph.general_matching import GeneralMatching\n\nn, m = map(int, input().split())\n\
    edges = [tuple(map(int, input().split())) for _ in range(m)]\nsolver = GeneralMatching(n,\
    \ edges)\nans = solver.solve()\nprint(len(ans))\nfor u, v in ans:\n    print(u,\
    \ v)\n"
  dependsOn:
  - graph/general_matching.py
  isVerificationFile: true
  path: test/library_checker/graph/matching_on_general_graph.test.py
  requiredBy: []
  timestamp: '2024-06-12 17:23:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/matching_on_general_graph.test.py
layout: document
redirect_from:
- /verify/test/library_checker/graph/matching_on_general_graph.test.py
- /verify/test/library_checker/graph/matching_on_general_graph.test.py.html
title: test/library_checker/graph/matching_on_general_graph.test.py
---
