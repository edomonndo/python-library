---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/tree/auxiliary_tree.py
    title: graph/tree/auxiliary_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/abc340/tasks/abc340_g
    links:
    - https://atcoder.jp/contests/abc340/tasks/abc340_g
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc340/tasks/abc340_g\n\
    \nfrom collections import defaultdict\nfrom graph.tree.auxiliary_tree import AuxiliaryTree\n\
    \nMOD = 998244353\n\nn = int(input())\nA = [int(x) for x in input().split()]\n\
    g0 = [[] for _ in range(n)]\nfor _ in range(n - 1):\n    u, v = map(lambda x:\
    \ int(x) - 1, input().split())\n    g0[u].append(v)\n    g0[v].append(u)\nAT =\
    \ AuxiliaryTree(g0)\nd = defaultdict(list)\nfor i, a in enumerate(A):\n    d[a].append(i)\n\
    ans = 0\nfor a in d.keys():\n    r, g = AT.build(d[a])\n    dp1 = dict()\n   \
    \ dp2 = dict()\n    stack = [~r, r]\n    while stack:\n        v = stack.pop()\n\
    \        if v >= 0:\n            for u in g[v]:\n                stack.append(~u)\n\
    \                stack.append(u)\n        else:\n            v = ~v\n        \
    \    if A[v] == a:\n                res = 1\n                for u in g[v]:\n\
    \                    res *= dp2[u] + 1\n                    res %= MOD\n     \
    \           dp1[v] = dp2[v] = res\n            else:\n                res = 1\n\
    \                tmp = 0\n                for u in g[v]:\n                   \
    \ res *= dp2[u] + 1\n                    tmp += dp2[u]\n                    res\
    \ %= MOD\n                    tmp %= MOD\n                dp1[v] = res - tmp -\
    \ 1\n                dp2[v] = res - 1\n    for x in dp1.values():\n        ans\
    \ = (ans + x) % MOD\nprint(ans)\n"
  dependsOn:
  - graph/tree/auxiliary_tree.py
  isVerificationFile: true
  path: test/atcoder/abc300-399/abc340g.test.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/abc300-399/abc340g.test.py
layout: document
title: G - Leaf Color
---
