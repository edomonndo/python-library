---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/shortest_paths.py
    title: Shortest paths
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/k_shortest_walk
    links:
    - https://judge.yosupo.jp/problem/k_shortest_walk
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/k_shortest_walk\n\
    \nfrom graph.shortest_paths import shortest_paths\n\nn, m, s, t, k = map(int,\
    \ input().split())\nes = [tuple(map(int, input().split())) for _ in range(m)]\n\
    ans = shortest_paths(n, es, s, t, k)\nwhile len(ans) < k:\n    ans.append(-1)\n\
    print(*ans, sep=\"\\n\")\n"
  dependsOn:
  - graph/shortest_paths.py
  isVerificationFile: true
  path: test/library_checker/graph/k_shortest_walk.test.py
  requiredBy: []
  timestamp: '2024-06-04 09:09:32+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/k_shortest_walk.test.py
layout: document
redirect_from:
- /verify/test/library_checker/graph/k_shortest_walk.test.py
- /verify/test/library_checker/graph/k_shortest_walk.test.py.html
title: test/library_checker/graph/k_shortest_walk.test.py
---
