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
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_C
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_C\n\
    \nfrom graph.scc import scc\n\nn, m = map(int, input().split())\nedges = [tuple(map(int,\
    \ input().split())) for _ in range(m)]\n\ngroups, comp_num = scc(n, edges)\n\n\
    q = int(input())\nfor _ in range(q):\n    s, t = map(int, input().split())\n \
    \   print(1 if comp_num[s] == comp_num[t] else 0)\n"
  dependsOn:
  - graph/scc.py
  isVerificationFile: true
  path: test/aoj/grl/grl_3_c_strongly_connected_components.test.py
  requiredBy: []
  timestamp: '2024-08-18 09:11:40+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_3_c_strongly_connected_components.test.py
layout: document
title: "GRL3C \u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3"
---
