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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "MOD = 998244353\n\n\ndef count_stable_set(adj: list[list[int]], r: int =\
    \ 0) -> int:\n    n = len(adj)\n\n    # dp[0][v] := \u9802\u70B9v\u3092\u6839\u3068\
    \u3059\u308B\u90E8\u5206\u6728\u306B\u3064\u3044\u3066\u3001\u9802\u70B9v\u3092\
    \u542B\u3080\u5B89\u5B9A\u96C6\u5408\u306E\u500B\u6570\n    # dp[1][v] := \u9802\
    \u70B9v\u3092\u6839\u3068\u3059\u308B\u90E8\u5206\u6728\u306B\u3064\u3044\u3066\
    \u3001\u9802\u70B9v\u3092\u542B\u307E\u306A\u3044\u5B89\u5B9A\u96C6\u5408\u306E\
    \u500B\u6570\n    dp = [[0] * n for _ in range(2)]\n    stack = [(r, -1)]\n  \
    \  while stack:\n        v, p = stack.pop()\n        if v >= 0:\n            dp[0][v]\
    \ = dp[1][v] = 1\n            for u in adj[v]:\n                if u != p:\n \
    \                   stack += [(~u, v), (u, v)]\n            continue\n       \
    \ if p == -1:\n            continue\n        v = ~v\n        # \u9802\u70B9v\u3092\
    \u9078\u3076\u5834\u5408\u3001\u5B50\u9802\u70B9\u306F\u3069\u308C\u3082\u9078\
    \u3076\u3053\u3068\u304C\u3067\u304D\u306A\u3044\n        dp[0][p] = (dp[0][p]\
    \ * dp[1][v]) % MOD\n        # \u9802\u70B9v\u3092\u9078\u3070\u306A\u3044\u5834\
    \u5408\u3001\u5B50\u9802\u70B9\u306F\u9078\u3093\u3067\u3082\u9078\u3070\u306A\
    \u304F\u3066\u3082\u69CB\u308F\u306A\u3044\n        dp[1][p] = (dp[1][p] * (dp[0][v]\
    \ + dp[1][v]) % MOD) % MOD\n\n    return (dp[0][r] + dp[1][r]) % MOD\n"
  dependsOn: []
  isVerificationFile: false
  path: tree/count_stable_set.py
  requiredBy: []
  timestamp: '2024-05-09 09:04:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tree/count_stable_set.py
layout: document
title: "\u6728\u306E\u5B89\u5B9A\u96C6\u5408\u306E\u500B\u6570"
---

[参考](https://algo-method.com/tasks/983)