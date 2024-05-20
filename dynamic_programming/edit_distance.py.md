---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    IGNORE: https://atcoder.jp/contests/abc185/tasks/abc185_e
    links:
    - https://atcoder.jp/contests/abc185/tasks/abc185_e
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: IGNORE https://atcoder.jp/contests/abc185/tasks/abc185_e\n\
    \n\ndef edit_distance(\n    S: str | list[int],\n    T: str | list[int],\n   \
    \ add_cost=None,\n    delete_cost=None,\n    replace_cost=None,\n) -> int:\n \
    \   n = len(S)\n    m = len(T)\n    inf = max(n, m)\n    dp = [[inf] * (m + 1)\
    \ for _ in range(n + 1)]\n    dp[0][0] = 0\n    for i in range(n):\n        dp[i][0]\
    \ = i\n    for j in range(m):\n        dp[0][j] = j\n    for i, s in enumerate(S):\n\
    \        for j, t in enumerate(T):\n            if s == t:\n                dp[i\
    \ + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j])\n            elif replace_cost\
    \ is not None:\n                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j]\
    \ + replace_cost)\n\n            if add_cost is not None:\n                dp[i\
    \ + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j + 1] + add_cost)\n            if\
    \ delete_cost is not None:\n                dp[i + 1][j + 1] = min(dp[i + 1][j\
    \ + 1], dp[i + 1][j] + delete_cost)\n    return dp[n][m]\n"
  dependsOn: []
  isVerificationFile: false
  path: dynamic_programming/edit_distance.py
  requiredBy: []
  timestamp: '2024-05-20 11:42:23+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: dynamic_programming/edit_distance.py
layout: document
redirect_from:
- /library/dynamic_programming/edit_distance.py
- /library/dynamic_programming/edit_distance.py.html
title: dynamic_programming/edit_distance.py
---
