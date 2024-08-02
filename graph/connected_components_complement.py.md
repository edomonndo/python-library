---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/connected_components_of_complement_graph.test.py
    title: Connected Components of Complement Graph
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import deque\n\n\ndef get_ccc(adj: list[list[int]]) -> list[list[int]]:\n\
    \    \"\"\"Return conntected components of complement graph of adj graph.\"\"\"\
    \n\n    n = len(adj)\n    idx = [-1] * n\n    flg = [0] * n\n    st = list(range(n))\n\
    \    cnt = 0\n    while st:\n        r = st.pop()\n        idx[r] = cnt\n    \
    \    q = deque([r])\n        while q:\n            v = q.popleft()\n         \
    \   for u in adj[v]:\n                flg[u] = 1\n            nex = []\n     \
    \       for u in st:\n                if flg[u]:\n                    nex.append(u)\n\
    \                elif idx[u] == -1:\n                    idx[u] = cnt\n      \
    \              q.append(u)\n            for u in adj[v]:\n                flg[u]\
    \ = 0\n            st = nex\n        cnt += 1\n\n    res = [[] for _ in range(cnt)]\n\
    \    for v in range(n):\n        res[idx[v]].append(v)\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/connected_components_complement.py
  requiredBy: []
  timestamp: '2024-08-02 11:42:07+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/connected_components_of_complement_graph.test.py
documentation_of: graph/connected_components_complement.py
layout: document
title: "\u88DC\u30B0\u30E9\u30D5\u306E\u9023\u7D50\u6210\u5206\u5206\u89E3"
---
