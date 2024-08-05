---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/st_numbering
    links:
    - https://judge.yosupo.jp/problem/st_numbering
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/st_numbering\n\
    \nimport sys\n\nsys.setrecursionlimit(1_000_000)\n\n\ndef st_numbering(adj: list[list[int]],\
    \ s: int, t: int) -> list[int]:\n    n = len(adj)\n    if n == 1:\n        return\
    \ [0]\n    if s == t:\n        return []\n\n    par = [-1] * n\n    pre = [-1]\
    \ * n\n    low = [-1] * n\n\n    def dfs(v: int) -> None:\n        pre[v] = len(vs)\n\
    \        vs.append(v)\n        low[v] = v\n        for u in adj[v]:\n        \
    \    if u == v:\n                continue\n            if pre[u] == -1:\n    \
    \            dfs(u)\n                par[u] = v\n                if pre[low[u]]\
    \ < pre[low[v]]:\n                    low[v] = low[u]\n            elif pre[u]\
    \ < pre[low[v]]:\n                low[v] = u\n\n    pre[s] = 0\n    vs = [s]\n\
    \    dfs(t)\n    if len(vs) < n:\n        return []\n\n    nxt = [-1] * n\n  \
    \  prev = [0] * n\n    nxt[s], prev[t] = t, s\n\n    sgn = [0] * n\n    sgn[s]\
    \ = -1\n    for v in vs[2:]:\n        p = par[v]\n        if sgn[low[v]] == -1:\n\
    \            q = prev[p]\n            if q == -1:\n                return []\n\
    \            nxt[q], nxt[v] = v, p\n            prev[v], prev[p] = q, v\n    \
    \        sgn[p] = 1\n        else:\n            q = nxt[p]\n            if q ==\
    \ -1:\n                return []\n            nxt[p], nxt[v] = v, q\n        \
    \    prev[v], prev[q] = p, v\n            sgn[p] = -1\n\n    path = [s]\n    while\
    \ path[-1] != t:\n        path.append(nxt[path[-1]])\n    if len(path) < n:\n\
    \        return []\n\n    rank = [-1] * n\n    for i, v in enumerate(path):\n\
    \        rank[v] = i\n    # assert min(rank) != -1\n\n    for i, v in enumerate(path):\n\
    \        l, r = 0, 0\n        for u in adj[v]:\n            if rank[u] < rank[v]:\n\
    \                l = 1\n            if rank[v] < rank[u]:\n                r =\
    \ 1\n        if i > 0 and l == 0:\n            return []\n        if i < n - 1\
    \ and r == 0:\n            return []\n    return rank\n\n\nT = int(input())\n\
    for _ in range(T):\n    n, m, s, t = map(int, input().split())\n    g = [[] for\
    \ _ in range(n)]\n    for _ in range(m):\n        u, v = map(int, input().split())\n\
    \        g[u].append(v)\n        g[v].append(u)\n    ans = st_numbering(g, s,\
    \ t)\n    if ans:\n        print(\"Yes\")\n        print(*ans)\n    else:\n  \
    \      print(\"No\")\n"
  dependsOn: []
  isVerificationFile: true
  path: test/library_checker/graph/st_numbering.test.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/st_numbering.test.py
layout: document
redirect_from:
- /verify/test/library_checker/graph/st_numbering.test.py
- /verify/test/library_checker/graph/st_numbering.test.py.html
title: test/library_checker/graph/st_numbering.test.py
---
