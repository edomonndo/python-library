---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/connectivity/unionfind.py
    title: graph/connectivity/unionfind.py
  - icon: ':heavy_check_mark:'
    path: graph/scc_incremental.py
    title: graph/scc_incremental.py
  - icon: ':heavy_check_mark:'
    path: utility/fastio.py
    title: utility/fastio.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/incremental_scc
    links:
    - https://judge.yosupo.jp/problem/incremental_scc
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/incremental_scc\n\
    \nfrom utility.fastio import Fastio\nfrom graph.scc_incremental import IncrementalScc\n\
    from graph.connectivity.unionfind import UnionFind\n\nimport sys\n\nsys.setrecursionlimit(1_000_000)\n\
    \nMOD = 998244353\n\nfastio = Fastio()\nrd = fastio.read\nwrtln = fastio.writeln\n\
    \n\nn, m = rd(), rd()\nX = [rd() for _ in range(n)]\nedges = []\nscc = IncrementalScc(n)\n\
    for _ in range(m):\n    u, v = rd(), rd()\n    edges.append((u, v))\n    scc.add_edge(u,\
    \ v)\nres = scc.solve()\nuf = UnionFind(n)\nans = 0\nfor i in range(m):\n    for\
    \ ei in res[i]:\n        u, v = edges[ei]\n        u = uf.leader(u)\n        v\
    \ = uf.leader(v)\n        w = uf.merge(u, v)\n        ans = (X[u] * X[v] + ans)\
    \ % MOD\n        X[w] = X[u] + X[v]\n        if X[w] >= MOD:\n            X[w]\
    \ -= MOD\n    wrtln(ans)\n"
  dependsOn:
  - utility/fastio.py
  - graph/scc_incremental.py
  - graph/connectivity/unionfind.py
  isVerificationFile: true
  path: test/library_checker/graph/scc_incremental.test.py
  requiredBy: []
  timestamp: '2024-09-14 18:35:55+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/scc_incremental.test.py
layout: document
title: Strongly Connected Components (Incremental)
---

