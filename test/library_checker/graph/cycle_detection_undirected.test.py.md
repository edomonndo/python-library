---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/find_cycle_undirected.py
    title: "\u9589\u8DEF\u691C\u51FA\uFF08\u7121\u5411\u30B0\u30E9\u30D5\uFF09"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/cycle_detection_undirected
    links:
    - https://judge.yosupo.jp/problem/cycle_detection_undirected
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cycle_detection_undirected\n\
    \n\nfrom graph.find_cycle_undirected import cycle_detection\n\nN, M = map(int,\
    \ input().split())\nG = [[] for _ in range(N)]\n\nfor i in range(M):\n    u, v\
    \ = map(int, input().split())\n    G[u].append((v, i))\n    G[v].append((u, i))\n\
    \n\ncycle_v, cycle_e = cycle_detection(N, M, G)\n\nif cycle_v:\n    print(len(cycle_v))\n\
    \    print(*cycle_v)\n    print(*cycle_e)\n\nelse:\n    print(-1)\n"
  dependsOn:
  - graph/find_cycle_undirected.py
  isVerificationFile: true
  path: test/library_checker/graph/cycle_detection_undirected.test.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/cycle_detection_undirected.test.py
layout: document
title: Cycle Detection (Undirected)
---

