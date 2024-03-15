---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/bipartitematching.test.py
    title: test/library_checker/graph/bipartitematching.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class BipartiteMatching:\n    def __init__(self, n1: int, n2: int):\n   \
    \     self.n = n1\n        self.m = n2\n        self.adj = [[] for _ in range(n1)]\n\
    \n    def add_edge(self, a: int, b: int):\n        self.adj[a].append(b)\n\n \
    \   def solve(self):\n        n, m, adj = self.n, self.m, self.adj\n        prev\
    \ = [-1] * n\n        root = [-1] * n\n        p = [-1] * n\n        q = [-1]\
    \ * m\n        updated = True\n        while updated:\n            updated = False\n\
    \            s = []\n            for v in range(n):\n                if p[v] ==\
    \ -1:\n                    root[v] = v\n                    s.append(v)\n    \
    \        i = 0\n            while i < len(s):\n                v = s[i]\n    \
    \            i += 1\n                if p[root[v]] != -1:\n                  \
    \  continue\n                for u in adj[v]:\n                    if q[u] ==\
    \ -1:\n                        while u != -1:\n                            q[u]\
    \ = v\n                            p[v], u = u, p[v]\n                       \
    \     v = prev[v]\n                        updated = True\n                  \
    \      break\n                    u = q[u]\n                    if prev[u] !=\
    \ -1:\n                        continue\n                    prev[u] = v\n   \
    \                 root[u] = root[v]\n                    s.append(u)\n       \
    \     if updated:\n                for v in range(n):\n                    prev[v]\
    \ = -1\n                    root[v] = -1\n        return [(v, p[v]) for v in range(n)\
    \ if p[v] != -1]\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/bipartite_matching.py
  requiredBy: []
  timestamp: '2024-02-09 16:12:14+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/bipartitematching.test.py
documentation_of: graph/bipartite_matching.py
layout: document
redirect_from:
- /library/graph/bipartite_matching.py
- /library/graph/bipartite_matching.py.html
title: graph/bipartite_matching.py
---
