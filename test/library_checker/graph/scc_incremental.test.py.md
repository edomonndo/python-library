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
    \nfrom collections import defaultdict\n\nfrom utility.fastio import Fastio\nfrom\
    \ graph.scc_incremental import incremental_scc\nfrom graph.connectivity.unionfind\
    \ import UnionFind\n\nfastio = Fastio()\nrd = fastio.read\nwrt = fastio.write\n\
    \nMOD = 998244353\n\nn, m = rd(), rd()\nX = []\nfor _ in range(n):\n    X.append(int(rd()))\n\
    edges = []\nfor _ in range(m):\n    u, v = rd(), rd()\n    edges.append((u, v))\n\
    time = incremental_scc(n, edges)\nids = defaultdict(list)\nfor ei in range(m):\n\
    \    if time[ei] <= m:\n        ids[time[ei]].append(ei)\n\nuf = UnionFind(n)\n\
    ans = [0] * m\nfor t in sorted(ids.keys()):\n    for ei in ids[t]:\n        u,\
    \ v = edges[ei]\n        u, v = uf.leader(u), uf.leader(v)\n        if u == v:\n\
    \            continue\n        ans[t - 1] += X[u] * X[v] % MOD\n        ans[t\
    \ - 1] %= MOD\n        uf.merge(u, v)\n        X[uf.leader(u)] = (X[u] + X[v])\
    \ % MOD\nfor i in range(m - 1):\n    ans[i + 1] = (ans[i + 1] + ans[i]) % MOD\n\
    wrt(*ans)\n"
  dependsOn:
  - utility/fastio.py
  - graph/scc_incremental.py
  - graph/connectivity/unionfind.py
  isVerificationFile: true
  path: test/library_checker/graph/scc_incremental.test.py
  requiredBy: []
  timestamp: '2024-09-10 07:31:46+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/graph/scc_incremental.test.py
layout: document
title: Strongly Connected Components (Incremental)
---

