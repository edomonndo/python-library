---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: linear_algebra/matrix.py
    title: linear_algebra/matrix.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/count_spanning_trees_directed.test.py
    title: Counting Spanning Trees (Directed)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/count_spanning_trees_undirected.test.py
    title: Counting Spanning Trees (Undirected)
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from linear_algebra.matrix import Matrix\n\n\nclass MatrixTreeTheorem:\n\
    \    def __init__(self, n: int, undirected: bool = True, r: int = None):\n   \
    \     self.n = n\n        self.undirected = undirected\n        self.root = r\n\
    \        self.adjugate_lap_mat = [[0] * (n - 1) for _ in range(n - 1)]\n\n   \
    \ def add_edge(self, u: int, v: int) -> None:\n        if u == v:\n          \
    \  return\n        g = self.adjugate_lap_mat\n        if self.undirected:\n  \
    \          if u == self.n - 1 and v == self.n - 1:\n                pass\n   \
    \         if u == self.n - 1:\n                g[v][v] += 1\n            elif\
    \ v == self.n - 1:\n                g[u][u] += 1\n            else:\n        \
    \        g[v][v] += 1\n                g[u][v] -= 1\n                g[u][u] +=\
    \ 1\n                g[v][u] -= 1\n        else:\n            if u == self.root:\n\
    \                dv = v > self.root\n                g[v - dv][v - dv] += 1\n\
    \            elif v == self.root:\n                pass\n            else:\n \
    \               dv, du = v > self.root, u > self.root\n                g[v - dv][v\
    \ - dv] += 1\n                g[u - du][v - dv] -= 1\n\n    def solve(self) ->\
    \ int:\n        mat = Matrix(self.n - 1, self.n - 1, self.adjugate_lap_mat)\n\
    \        return mat.determinant()\n"
  dependsOn:
  - linear_algebra/matrix.py
  isVerificationFile: false
  path: graph/matrix_tree_theorem.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/count_spanning_trees_directed.test.py
  - test/library_checker/graph/count_spanning_trees_undirected.test.py
documentation_of: graph/matrix_tree_theorem.py
layout: document
redirect_from:
- /library/graph/matrix_tree_theorem.py
- /library/graph/matrix_tree_theorem.py.html
title: graph/matrix_tree_theorem.py
---
