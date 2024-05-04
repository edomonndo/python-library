---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: tree/rooted_tree.py
    title: "\u6839\u4ED8\u304D\u6728"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from tree.rooted_tree import rooted_tree\n\n\ndef max_stable_set(adj: list[list[int]],\
    \ weight=list[int]) -> int:\n    n = len(adj)\n    children, par = rooted_tree(adj,\
    \ 0)\n\n    deg = [0] * n\n    stack = []\n    for v in range(n):\n        deg[v]\
    \ = len(children[v])\n        if deg[v] == 0:\n            stack.append(v)\n\n\
    \    # dp[0][v] := \u9802\u70B9v\u3092\u6839\u3068\u3059\u308B\u90E8\u5206\u6728\
    \u306B\u3064\u3044\u3066\u3001\u9802\u70B9v\u3092\u542B\u3080\u5B89\u5B9A\u96C6\
    \u5408\u306E\u3046\u3061\u3001\u91CD\u307F\u306E\u6700\u5927\u5024\n    # dp[1][v]\
    \ := \u9802\u70B9v\u3092\u6839\u3068\u3059\u308B\u90E8\u5206\u6728\u306B\u3064\
    \u3044\u3066\u3001\u9802\u70B9v\u3092\u542B\u307E\u306A\u3044\u5B89\u5B9A\u96C6\
    \u5408\u306E\u3046\u3061\u3001\u91CD\u307F\u306E\u6700\u5927\u5024\n    dp = [[0]\
    \ * n for _ in range(2)]\n    while stack:\n        v = stack.pop()\n\n      \
    \  dp[0][v] = weight[v]\n        for u in children[v]:\n            # \u9802\u70B9\
    v\u3092\u9078\u3076\u5834\u5408\u3001\u5B50\u9802\u70B9\u306F\u3069\u308C\u3082\
    \u9078\u3076\u3053\u3068\u304C\u3067\u304D\u306A\u3044\n            dp[0][v] +=\
    \ dp[1][u]\n            # \u9802\u70B9v\u3092\u9078\u3070\u306A\u3044\u5834\u5408\
    \u3001\u5B50\u9802\u70B9\u306F\u9078\u3093\u3067\u3082\u9078\u3070\u306A\u304F\
    \u3066\u3082\u69CB\u308F\u306A\u3044\n            dp[1][v] += max(dp[0][u], dp[1][u])\n\
    \n        p = par[v]\n        deg[p] -= 1\n        if deg[p] == 0:\n         \
    \   stack.append(p)\n\n    return max(dp[0][0], dp[1][0])\n"
  dependsOn:
  - tree/rooted_tree.py
  isVerificationFile: false
  path: tree/maximum_weighted_stable_set.py
  requiredBy: []
  timestamp: '2024-05-04 16:25:31+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tree/maximum_weighted_stable_set.py
layout: document
title: "\u6728\u306E\u91CD\u307F\u4ED8\u304D\u6700\u5927\u5B89\u5B9A\u96C6\u5408"
---

[参考](https://algo-method.com/tasks/982)