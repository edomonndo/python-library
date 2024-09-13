---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: graph/connectivity/unionfind.py
    title: Union Find
  - icon: ':x:'
    path: graph/scc_incremental.py
    title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3(Incremental)"
  - icon: ':x:'
    path: utility/fastio.py
    title: "\u9AD8\u901F\u5165\u51FA\u529B"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
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
  timestamp: '2024-09-14 02:22:35+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/graph/scc_incremental.test.py
layout: document
title: Strongly Connected Components (Incremental)
---

