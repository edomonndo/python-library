---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/tree_diameter
    links:
    - https://judge.yosupo.jp/problem/tree_diameter
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/tree_diameter\n\
    \n\ndef diameter(N: int, G: list) -> tuple[int, list]:\n    def dfs(start: int):\n\
    \        dist = [-1 for _ in range(N)]\n        dist[start] = 0\n        stack\
    \ = [start]\n        while stack:\n            v = stack.pop()\n            for\
    \ u, d in G[v]:\n                if dist[u] != -1:\n                    continue\n\
    \                dist[u] = dist[v] + d\n                stack.append(u)\n    \
    \    max_v = -1\n        max_d = -1\n        for v, d in enumerate(dist):\n  \
    \          if d > max_d:\n                max_d = d\n                max_v = v\n\
    \        return max_v, dist\n\n    s, _ = dfs(0)\n    v, dist = dfs(s)\n    diam\
    \ = dist[v]\n    path = [v]\n    while v != s:\n        for u, d in G[v]:\n  \
    \          if dist[u] + d == dist[v]:\n                path.append(u)\n      \
    \          v = u\n                break\n    return diam, path\n\n\nN = int(input())\n\
    G = [[] for _ in range(N)]\nfor _ in range(N - 1):\n    a, b, c = map(int, input().split())\n\
    \    G[a].append((b, c))\n    G[b].append((a, c))\n\ndiam, path = diameter(N,\
    \ G)\nprint(diam, len(path))\nprint(*path)\n"
  dependsOn: []
  isVerificationFile: true
  path: library_checker/tree/tree_diameter.test.py
  requiredBy: []
  timestamp: '2023-06-09 12:42:19+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: library_checker/tree/tree_diameter.test.py
layout: document
redirect_from:
- /verify/library_checker/tree/tree_diameter.test.py
- /verify/library_checker/tree/tree_diameter.test.py.html
title: library_checker/tree/tree_diameter.test.py
---
