---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/cycle_detection_directed.test.py
    title: Cycle Detection (Directed)
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def cycle_detection(N: int, G: list[list[int]]) -> list[int]:\n    visited\
    \ = [False] * N\n    finished = [False] * N\n    stc = []\n    for i in range(N):\n\
    \        if visited[i]:\n            continue\n        # \u975E\u518D\u5E30dfs\n\
    \        que = [(1, i, -1), (0, i, -1)]\n        visited[i] = True\n        while\
    \ que:\n            t, v, idx = que.pop()\n            if t == 0:\n          \
    \      # \u884C\u304D\u304C\u3051\u9806\n                if finished[v]:\n   \
    \                 continue\n                visited[v] = True\n              \
    \  stc.append((v, idx))\n                for u, id in G[v]:\n                \
    \    if finished[v]:\n                        continue\n\n                   \
    \ if visited[u] and finished[u] == 0:\n                        cycle = [id]\n\
    \                        while stc:\n                            v, id = stc.pop()\n\
    \                            if v == u:\n                                break\n\
    \                            cycle.append(id)\n                        return\
    \ cycle[::-1]\n\n                    elif not visited[u]:\n                  \
    \      que.append((1, u, id))\n                        que.append((0, u, id))\n\
    \            else:\n                # \u5E30\u308A\u304C\u3051\u9806\n       \
    \         if finished[v]:\n                    continue\n                stc.pop()\n\
    \                finished[v] = True\n\n    return []\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/find_cycle_directed.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/cycle_detection_directed.test.py
documentation_of: graph/find_cycle_directed.py
layout: document
redirect_from:
- /library/graph/find_cycle_directed.py
- /library/graph/find_cycle_directed.py.html
title: graph/find_cycle_directed.py
---
