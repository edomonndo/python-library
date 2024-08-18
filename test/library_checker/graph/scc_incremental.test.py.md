---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/connectivity/unionfind.py
    title: Union Find
  - icon: ':heavy_check_mark:'
    path: graph/scc_incremental.py
    title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3(Incremental)"
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
    \nfrom collections import defaultdict\n\nfrom graph.scc_incremental import incremental_scc\n\
    from graph.connectivity.unionfind import UnionFind\n\nMOD = 998244353\n\nn, m\
    \ = map(int, input().split())\nX = [int(x) for x in input().split()]\nedges =\
    \ [tuple(map(int, input().split())) for _ in range(m)]\ntime = incremental_scc(n,\
    \ edges)\nids = defaultdict(list)\nfor ei in range(m):\n    if time[ei] <= m:\n\
    \        ids[time[ei]].append(ei)\n\nuf = UnionFind(n)\nans = [0] * m\nfor t in\
    \ sorted(ids.keys()):\n    for ei in ids[t]:\n        u, v = edges[ei]\n     \
    \   u, v = uf.leader(u), uf.leader(v)\n        if u == v:\n            continue\n\
    \        ans[t - 1] += X[u] * X[v] % MOD\n        ans[t - 1] %= MOD\n        uf.merge(u,\
    \ v)\n        X[uf.leader(u)] = (X[u] + X[v]) % MOD\nfor i in range(m - 1):\n\
    \    ans[i + 1] = (ans[i + 1] + ans[i]) % MOD\nprint(*ans, sep=\"\\n\")\n"
  dependsOn:
  - graph/scc_incremental.py
  - graph/connectivity/unionfind.py
  isVerificationFile: true
  path: test/library_checker/graph/scc_incremental.test.py
  requiredBy: []
  timestamp: '2024-08-18 17:02:41+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/scc_incremental.test.py
layout: document
title: Strongly Connected Components (Incremental)
---

