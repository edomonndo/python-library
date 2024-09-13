---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: graph/scc.py
    title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_C
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_C\n\
    \nfrom graph.scc import SCC\n\nn, m = map(int, input().split())\nedges = [tuple(map(int,\
    \ input().split())) for _ in range(m)]\n\nscc = SCC(n)\nfor u, v in edges:\n \
    \   scc.add_edge(u, v)\ncc = scc.get_mapping()\nq = int(input())\nfor _ in range(q):\n\
    \    s, t = map(int, input().split())\n    print(1 if cc[s] == cc[t] else 0)\n"
  dependsOn:
  - graph/scc.py
  isVerificationFile: true
  path: test/aoj/grl/grl_3_c_strongly_connected_components.test.py
  requiredBy: []
  timestamp: '2024-09-14 02:22:35+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/aoj/grl/grl_3_c_strongly_connected_components.test.py
layout: document
title: "GRL3C \u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3"
---

