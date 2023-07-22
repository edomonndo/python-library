---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import deque\n\n\ndef topological_sort(N, G, deg):\n   \
    \ \"\"\"\u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\u30C8\n\n    \u6709\u5411\
    \u30B0\u30E9\u30D5\u306E\u9806\u5E8F\u3092\u5B88\u308B\u3088\u3046\u306B\u30BD\
    \u30FC\u30C8\u3059\u308B\n    \u9589\u8DEF\u304C\u3042\u308B\u304B\u5224\u5B9A\
    \u3082\u51FA\u6765\u308B\n    \u8A08\u7B97\u91CF: O(E+V)\n\n    Args:\n      \
    \  G (list): edge[i] = [a, b,...] i\u304B\u3089a,b,...\u306B\u8FBA\u304C\u4F38\
    \u3073\u3066\u3044\u308B\n        deg (list): deg[i] = i\u306E\u5165\u529B\u8FBA\
    \u306E\u672C\u6570\n\n    Returns:\n        list or -1:\u9589\u8DEF\u304C\u5B58\
    \u5728\u3057\u306A\u3044\u3068\u304D\n                      \u30BD\u30FC\u30C8\
    \u6E08\u307F\u306E\u30EA\u30B9\u30C8\n                   \u9589\u8DEF\u304C\u5B58\
    \u5728\u3059\u308B\u6642\n                      -1\n    \"\"\"\n    cands = [v\
    \ for v in range(N) if deg[v] == 0]\n    ans = []\n    que = deque(cands)\n  \
    \  while que:\n        v = que.popleft()\n        if v in cands:\n           \
    \ ans.append(v)\n        for u in G[v]:\n            deg[u] -= 1\n           \
    \ if deg[u] == 0:\n                que.append(u)\n                ans.append(u)\n\
    \    if len(ans) == N:\n        return ans\n    return -1\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/toporogical_sort.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: graph/toporogical_sort.py
layout: document
redirect_from:
- /library/graph/toporogical_sort.py
- /library/graph/toporogical_sort.py.html
title: graph/toporogical_sort.py
---
