---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/scc.py
    title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/scc
    links:
    - https://judge.yosupo.jp/problem/scc
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc\n\nfrom\
    \ graph.scc import scc\n\nN, M = map(int, input().split())\nedges = [None] * M\n\
    for i in range(M):\n    edges[i] = tuple(map(int, input().split()))\n\ngroups\
    \ = scc(N, edges)\nprint(len(groups))\nfor group in groups:\n    print(len(group),\
    \ *group)\n"
  dependsOn:
  - graph/scc.py
  isVerificationFile: true
  path: test/library_checker/graph/scc.test.py
  requiredBy: []
  timestamp: '2024-02-09 17:45:13+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/scc.test.py
layout: document
title: Strongly Connected Components
---

