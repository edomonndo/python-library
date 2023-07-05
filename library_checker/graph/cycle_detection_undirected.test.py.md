---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/cycle_detection_undirected
    links:
    - https://judge.yosupo.jp/problem/cycle_detection_undirected
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cycle_detection_undirected\n\
    \nfrom typing import List, Tuple\n\n\ndef find_cycle(\n    N: int, M: int, G:\
    \ List[List[int]]\n) -> Tuple[int, int, int, List[int], List[int]]:\n    visited\
    \ = [0] * N\n    finished = [0] * M\n    par_v = [None] * N\n    par_e = [None]\
    \ * N\n\n    for i in range(N):\n        if visited[i]:\n            continue\n\
    \        stack = [(i, -1, -1)]\n        while stack:\n            v, p, e = stack.pop()\
    \  # v: \u9802\u70B9\u756A\u53F7\uFF64p: v\u306E\u89AA\u9802\u70B9\u3001e: v\u3068\
    \u63A5\u7D9A\u3059\u308B\u8FBA\n            if e != -1 and finished[e]:\n    \
    \            continue\n            if visited[v]:\n                par_v[v] =\
    \ p\n                if e != -1:\n                    par_e[v] = e\n         \
    \       return v, p, e, par_v, par_e\n            visited[v] = 1\n           \
    \ if e != -1:\n                par_e[v] = e\n                finished[e] = 1\n\
    \            par_v[v] = p\n            for u, e in G[v]:\n                if finished[e]:\n\
    \                    continue\n                stack.append((u, v, e))\n\n   \
    \ return -1, -1, -1, par_v, par_e\n\n\ndef cycle_detection(N: int, M: int, G:\
    \ List[int]):\n    v, p, e, par_v, par_e = find_cycle(N, M, G)\n    if p == -1:\n\
    \        return [], []\n    else:\n        cycle_v = [p]\n        cycle_e = [e]\n\
    \        while v != p:\n            e = par_e[p]\n            p = par_v[p]\n \
    \           cycle_v.append(p)\n            cycle_e.append(e)\n        return cycle_v[::-1],\
    \ cycle_e[::-1]\n\n\nN, M = map(int, input().split())\nG = [[] for _ in range(N)]\n\
    \nfor i in range(M):\n    u, v = map(int, input().split())\n    G[u].append((v,\
    \ i))\n    G[v].append((u, i))\n\n\ncycle_v, cycle_e = cycle_detection(N, M, G)\n\
    \nif cycle_v:\n    print(len(cycle_v))\n    print(*cycle_v)\n    print(*cycle_e)\n\
    \nelse:\n    print(-1)\n"
  dependsOn: []
  isVerificationFile: true
  path: library_checker/graph/cycle_detection_undirected.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: library_checker/graph/cycle_detection_undirected.test.py
layout: document
redirect_from:
- /verify/library_checker/graph/cycle_detection_undirected.test.py
- /verify/library_checker/graph/cycle_detection_undirected.test.py.html
title: library_checker/graph/cycle_detection_undirected.test.py
---
