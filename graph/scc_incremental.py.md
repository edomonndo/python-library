---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/scc.py
    title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/scc_incremental.test.py
    title: Strongly Connected Components (Incremental)
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from graph.scc import scc\n\n\ndef incremental_scc(n: int, edges: list[tuple[int,\
    \ int]]) -> list[int]:\n    m = len(edges)\n    inf = float(\"inf\")\n    merge_time\
    \ = [inf] * m\n    dat = [(ei, u, v) for ei, (u, v) in enumerate(edges)]\n\n \
    \   new_idx = [-1] * n\n    cnt = 1\n    st = [(0, m, dat)]\n    while st:\n \
    \       l, r, dat = st.pop()\n        mid = (l + r + 1) >> 1\n        start =\
    \ cnt\n        for i in range(len(dat)):\n            ei, u, v = dat[i]\n    \
    \        if new_idx[u] < start:\n                new_idx[u] = cnt\n          \
    \      cnt += 1\n            if new_idx[v] < start:\n                new_idx[v]\
    \ = cnt\n                cnt += 1\n            dat[i] = (ei, new_idx[u] - start,\
    \ new_idx[v] - start)\n\n        _, comp = scc(cnt - start, [(u, v) for ei, u,\
    \ v in dat if ei < mid])\n        if l + 1 == r:\n            for ei, u, v in\
    \ dat:\n                if comp[u] == comp[v]:\n                    merge_time[ei]\
    \ = r\n            continue\n        j = 0\n        k = len(dat)\n        for\
    \ _ in range(len(dat)):\n            ei, u, v = dat[j]\n            if ei < mid\
    \ and comp[u] == comp[v]:\n                j += 1\n            else:\n       \
    \         dat[j] = (ei, comp[u], comp[v])\n                k -= 1\n          \
    \      dat[j], dat[k] = dat[k], dat[j]\n        st.append((mid, r, dat[j:]))\n\
    \        st.append((l, mid, dat[:j]))\n    return merge_time\n"
  dependsOn:
  - graph/scc.py
  isVerificationFile: false
  path: graph/scc_incremental.py
  requiredBy: []
  timestamp: '2024-08-18 17:02:41+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/scc_incremental.test.py
documentation_of: graph/scc_incremental.py
layout: document
title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3(Incremental)"
---
