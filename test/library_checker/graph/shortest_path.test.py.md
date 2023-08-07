---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/shortest_path
    links:
    - https://judge.yosupo.jp/problem/shortest_path
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path\n\
    \nfrom graph.dijkstra import dijkstra, get_path\n\nN, M, s, t = map(int, input().split())\n\
    G = [[] for _ in range(N)]\nfor _ in range(M):\n    u, v, c = map(int, input().split())\n\
    \    G[u].append((c, v))\n\ndist, prev = dijkstra(N, G, s)\n\nif dist[t] == 1\
    \ << 60:\n    print(-1)\n    exit()\n\npath = get_path(prev, s, t)\nprint(dist[t],\
    \ len(path) - 1)\nfor i in range(len(path) - 1):\n    print(path[i], path[i +\
    \ 1])\n"
  dependsOn: []
  isVerificationFile: true
  path: test/library_checker/graph/shortest_path.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/graph/shortest_path.test.py
layout: document
redirect_from:
- /verify/test/library_checker/graph/shortest_path.test.py
- /verify/test/library_checker/graph/shortest_path.test.py.html
title: test/library_checker/graph/shortest_path.test.py
---
