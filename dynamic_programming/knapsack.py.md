---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    IGNORE: https://atcoder.jp/contests/abc032/tasks/abc032_d
    links:
    - https://atcoder.jp/contests/abc032/tasks/abc032_d
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: IGNORE https://atcoder.jp/contests/abc032/tasks/abc032_d\n\
    \n\ndef solve1(n: int, w: int, vs: list[int], ws: list[int]) -> int:\n    \"\"\
    \"\u534A\u5206\u524D\u5217\u6319 n <= 30\"\"\"\n    n1 = n // 2\n    n2 = n -\
    \ n1\n\n    cands1 = set()\n    for bit in range(1 << n1):\n        vw = [0, 0]\n\
    \        for i in range(n1):\n            if (bit >> i) & 1:\n               \
    \ vw[0] += vs[i]\n                vw[1] += ws[i]\n            if vw[1] <= w:\n\
    \                cands1.add(tuple(vw))\n    cands2 = set()\n    for bit in range(1\
    \ << n2):\n        vw = [0, 0]\n        for i in range(n2):\n            if (bit\
    \ >> i) & 1:\n                vw[0] += vs[i + n1]\n                vw[1] += ws[i\
    \ + n1]\n            if vw[1] <= w:\n                cands2.add(tuple(vw))\n \
    \   res = 0\n    for v1, w1 in cands1:\n        for v2, w2 in cands2:\n      \
    \      if w1 + w2 <= w:\n                res = max(res, v1 + v2)\n    return res\n\
    \n\ndef solve2(n: int, w: int, vs: list[int], ws: list[int]) -> int:\n    \"\"\
    \"\u91CD\u3055\u3092\u914D\u5217\u3067\u7BA1\u7406\u3067\u304D\u308B\u3068\u304D\
    (w <= 10**5)\"\"\"\n    dp = [0] * (w + 1)\n    for v1, w1 in zip(vs, ws):\n \
    \       nex = [0] * (w + 1)\n        for j in range(w + 1):\n            nex[j]\
    \ = max(nex[j], dp[j])\n            if j + w1 <= w:\n                nex[j + w1]\
    \ = max(nex[j + w1], dp[j] + v1)\n        dp = nex\n    return dp[w]\n\n\ndef\
    \ solve3(n: int, w: int, vs: list[int], ws: list[int]) -> int:\n    \"\"\"\u4FA1\
    \u5024\u306E\u5408\u8A08\u3092\u914D\u5217\u3067\u7BA1\u7406\u3067\u304D\u308B\
    \u3068\u304D(mv <= 10**5)\"\"\"\n    mv = sum(vs)\n    inf = float(\"inf\")\n\
    \    dp = [inf] * (mv + 1)\n    dp[0] = 0\n    for v1, w1 in zip(vs, ws):\n  \
    \      nex = [inf] * (mv + 1)\n        for j in range(mv + 1):\n            if\
    \ dp[j] == inf:\n                continue\n            nex[j] = min(nex[j], dp[j])\n\
    \            if j + v1 <= mv:\n                nex[j + v1] = min(nex[j + v1],\
    \ dp[j] + w1)\n        dp = nex\n    for j in range(mv, -1, -1):\n        if dp[j]\
    \ <= w:\n            return j\n"
  dependsOn: []
  isVerificationFile: false
  path: dynamic_programming/knapsack.py
  requiredBy: []
  timestamp: '2024-05-20 11:42:23+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: dynamic_programming/knapsack.py
layout: document
redirect_from:
- /library/dynamic_programming/knapsack.py
- /library/dynamic_programming/knapsack.py.html
title: dynamic_programming/knapsack.py
---
