---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/cycle_detection
    links:
    - https://judge.yosupo.jp/problem/cycle_detection
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cycle_detection\n\
    from typing import List\n\n\ndef find_cycle(N: int, G: List[List[int]]) -> List[int]:\n\
    \    visited = [False] * N\n    finished = [False] * N\n    stc = []\n    for\
    \ i in range(N):\n        if visited[i]:\n            continue\n        # \u975E\
    \u518D\u5E30dfs\n        que = [(1, i, -1), (0, i, -1)]\n        visited[i] =\
    \ True\n        while que:\n            t, v, idx = que.pop()\n            if\
    \ t == 0:\n                # \u884C\u304D\u304C\u3051\u9806\n                if\
    \ finished[v]:\n                    continue\n                visited[v] = True\n\
    \                stc.append((v, idx))\n                for u, id in G[v]:\n  \
    \                  if finished[v]:\n                        continue\n\n     \
    \               if visited[u] and finished[u] == 0:\n                        cycle\
    \ = [id]\n                        while stc:\n                            v, id\
    \ = stc.pop()\n                            if v == u:\n                      \
    \          break\n                            cycle.append(id)\n             \
    \           return cycle[::-1]\n\n                    elif not visited[u]:\n \
    \                       que.append((1, u, id))\n                        que.append((0,\
    \ u, id))\n            else:\n                # \u5E30\u308A\u304C\u3051\u9806\
    \n                if finished[v]:\n                    continue\n            \
    \    stc.pop()\n                finished[v] = True\n\n    return []\n\n\nN, M\
    \ = map(int, input().split())\nG = [[] for i in range(N)]\nfor i in range(M):\n\
    \    u, v = map(int, input().split())\n    G[u].append((v, i))\n\ncycle = find_cycle(N,\
    \ G)\nif len(cycle) == 0:\n    print(-1)\nelse:\n    print(len(cycle))\n    print(*cycle,\
    \ sep=\"\\n\")\n"
  dependsOn: []
  isVerificationFile: true
  path: test/library_checker/graph/cycle_detection.test.py
  requiredBy: []
  timestamp: '2023-08-01 14:51:05+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/cycle_detection.test.py
layout: document
redirect_from:
- /verify/test/library_checker/graph/cycle_detection.test.py
- /verify/test/library_checker/graph/cycle_detection.test.py.html
title: test/library_checker/graph/cycle_detection.test.py
---