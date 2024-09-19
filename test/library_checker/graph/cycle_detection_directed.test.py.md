---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/find_cycle_directed.py
    title: "\u9589\u8DEF\u691C\u51FA\uFF08\u6709\u5411\u30B0\u30E9\u30D5\uFF09"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/cycle_detection
    links:
    - https://judge.yosupo.jp/problem/cycle_detection
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cycle_detection\n\
    \nfrom graph.find_cycle_directed import cycle_detection\n\nN, M = map(int, input().split())\n\
    G = [[] for i in range(N)]\nfor i in range(M):\n    u, v = map(int, input().split())\n\
    \    G[u].append((v, i))\n\ncycle = cycle_detection(N, G)\nif len(cycle) == 0:\n\
    \    print(-1)\nelse:\n    print(len(cycle))\n    print(*cycle, sep=\"\\n\")\n"
  dependsOn:
  - graph/find_cycle_directed.py
  isVerificationFile: true
  path: test/library_checker/graph/cycle_detection_directed.test.py
  requiredBy: []
  timestamp: '2024-07-19 12:35:18+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/cycle_detection_directed.test.py
layout: document
title: Cycle Detection (Directed)
---

