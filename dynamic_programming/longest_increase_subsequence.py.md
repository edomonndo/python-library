---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: atcoder/segtree.py
    title: atcoder/segtree.py
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
  code: "def naive(A: list[int], less_than: bool = True) -> int:\n    n = len(A)\n\
    \    dp = [0] * n\n    size = 0\n    for i in range(n):\n        dp[i] = 1\n \
    \       for j in range(i):\n            if less_than:\n                if A[j]\
    \ < A[i]:\n                    dp[i] = max(dp[i], dp[j] + 1)\n            else:\n\
    \                if A[j] <= A[i]:\n                    dp[i] = max(dp[i], dp[j]\
    \ + 1)\n        if size < dp[i]:\n            size = dp[i]\n    return size\n\n\
    \ndef calc_lis(\n    A: list[int], less_than: bool = True, restore: bool = False\n\
    ) -> int | tuple[int, list[int]]:\n    from bisect import bisect_left, bisect_right\n\
    \n    n = len(A)\n    inf = float(\"inf\")\n    dp = [inf] * n\n    if restore:\n\
    \        prev = [-1] * n\n\n    size = 0\n    for i, a in enumerate(A):\n    \
    \    j = bisect_left(dp, a) if less_than else bisect_right(dp, a)\n        if\
    \ restore:\n            prev[i] = j\n        dp[j] = a\n        if j + 1 > size:\n\
    \            size = j + 1\n    if not restore:\n        return size\n\n    res\
    \ = [0] * size\n    j = size - 1\n    for i in reversed(range(n)):\n        if\
    \ prev[i] == j:\n            res[j] = i\n            j -= 1\n    return size,\
    \ res\n\n\ndef calc_lis_segtree(\n    A: list[int], less_than: bool = True, restore:\
    \ bool = False\n) -> int | tuple[int, list[int]]:\n    from atcoder.segtree import\
    \ SegTree\n\n    # \u5EA7\u6A19\u5727\u7E2E 1-indexed\n    dic = {e: i for i,\
    \ e in enumerate(sorted(set(A)), 1)}\n    A2 = list(map(dic.__getitem__, A))\n\
    \n    n = len(A2)\n    seg = SegTree(max, -1, [0] * (n + 1))\n    if restore:\n\
    \        prev = [-1] * n\n\n    size = 0\n    for i, a in enumerate(A2):\n   \
    \     j = seg.prod(0, a) if less_than else seg.prod(0, a + 1)\n        if restore:\n\
    \            prev[i] = j\n        if seg.get(a) < j + 1:\n            seg.set(a,\
    \ j + 1)\n            size = max(size, j + 1)\n    if not restore:\n        return\
    \ size\n\n    res = [0] * size\n    j = size - 1\n    for i in reversed(range(n)):\n\
    \        if prev[i] == j:\n            res[j] = i\n            j -= 1\n    return\
    \ size, res\n"
  dependsOn:
  - atcoder/segtree.py
  isVerificationFile: false
  path: dynamic_programming/longest_increase_subsequence.py
  requiredBy: []
  timestamp: '2024-05-20 11:42:23+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: dynamic_programming/longest_increase_subsequence.py
layout: document
redirect_from:
- /library/dynamic_programming/longest_increase_subsequence.py
- /library/dynamic_programming/longest_increase_subsequence.py.html
title: dynamic_programming/longest_increase_subsequence.py
---
