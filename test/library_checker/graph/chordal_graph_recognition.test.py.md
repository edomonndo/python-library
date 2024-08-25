---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: graph/chordal_graph.py
    title: graph/chordal_graph.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/chordal_graph_recognition
    links:
    - https://judge.yosupo.jp/problem/chordal_graph_recognition
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/chordal_graph_recognition\n\
    \nfrom graph.chordal_graph import ChordalGraph\n\nn, m = map(int, input().split())\n\
    edges = [tuple(map(int, input().split())) for _ in range(m)]\nCG = ChordalGraph(n,\
    \ edges)\nif CG.is_chordal_graph():\n    print(\"YES\")\n    print(*CG.get_perfect_elimination_order())\n\
    else:\n    print(\"NO\")\n    ans = CG.find_induced_cycle()\n    print(len(ans))\n\
    \    print(*ans)\n"
  dependsOn:
  - graph/chordal_graph.py
  isVerificationFile: true
  path: test/library_checker/graph/chordal_graph_recognition.test.py
  requiredBy: []
  timestamp: '2024-08-25 18:10:26+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/graph/chordal_graph_recognition.test.py
layout: document
title: Chordal Graph Recognition
---

