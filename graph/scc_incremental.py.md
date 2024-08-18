---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/scc.py
    title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library_checker/graph/scc_incremental.test.py
    title: Strongly Connected Components (Incremental)
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from graph.scc import scc\n\n\ndef incremental_scc(n: int, edges: list[tuple[int,\
    \ int]]):\n    m = len(edges)\n    inf = float(\"inf\")\n    merge_time = [inf]\
    \ * m\n    dat = [(i, u, v) for i, (u, v) in enumerate(edges)]\n\n    new_idx\
    \ = [-1] * n\n    st = [(0, m + 1, dat)]\n    while st:\n        l, r, dat = st.pop()\n\
    \        mid = (l + r) >> 1\n        n_ = 0\n        for _, u, v in dat:\n   \
    \         if new_idx[u] == -1:\n                new_idx[u] = n_\n            \
    \    n_ += 1\n            if new_idx[v] == -1:\n                new_idx[v] = n_\n\
    \                n_ += 1\n        es = [(new_idx[u], new_idx[v]) for i, u, v in\
    \ dat if i < mid]\n        _, comp = scc(n_, es)\n        dat1, dat2 = [], []\n\
    \        for i, u, v in dat:\n            u, v = new_idx[u], new_idx[v]\n    \
    \        if i < mid:\n                if comp[u] == comp[v]:\n               \
    \     if merge_time[i] > mid:\n                        merge_time[i] = mid\n \
    \                       dat1.append((i, u, v))\n                else:\n      \
    \              dat2.append((i, comp[u], comp[v]))\n            else:\n       \
    \         dat2.append((i, comp[u], comp[v]))\n        if dat2 and r - mid > 1:\n\
    \            st.append((mid, r, dat2))\n        if dat1 and mid - l > 1:\n   \
    \         st.append((l, mid, dat1))\n    return merge_time\n"
  dependsOn:
  - graph/scc.py
  isVerificationFile: false
  path: graph/scc_incremental.py
  requiredBy: []
  timestamp: '2024-08-18 09:11:40+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/library_checker/graph/scc_incremental.test.py
documentation_of: graph/scc_incremental.py
layout: document
title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3(Incremental)"
---
