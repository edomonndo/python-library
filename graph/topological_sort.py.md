---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_4_a_cycle_detection.test.py
    title: "GRL4A \u6709\u5411\u30B0\u30E9\u30D5\u306E\u9589\u8DEF\u691C\u67FB"
  - icon: ':grey_question:'
    path: test/aoj/grl/grl_4_b_topological_sort.test.py
    title: "GRL4B \u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\u30C8"
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import deque\n\n\ndef topological_sort(G, deg):\n    n =\
    \ len(G)\n    cands = [v for v in range(n) if deg[v] == 0]\n    ans = []\n   \
    \ que = deque(cands)\n    while que:\n        v = que.popleft()\n        if v\
    \ in cands:\n            ans.append(v)\n        for u in G[v]:\n            deg[u]\
    \ -= 1\n            if deg[u] == 0:\n                que.append(u)\n         \
    \       ans.append(u)\n    if len(ans) == n:\n        return ans\n    return -1\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/topological_sort.py
  requiredBy: []
  timestamp: '2023-12-04 22:53:06+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_4_a_cycle_detection.test.py
  - test/aoj/grl/grl_4_b_topological_sort.test.py
documentation_of: graph/topological_sort.py
layout: document
redirect_from:
- /library/graph/topological_sort.py
- /library/graph/topological_sort.py.html
title: graph/topological_sort.py
---
