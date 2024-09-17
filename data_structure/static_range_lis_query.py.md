---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/static_range_lis_query.test.py
    title: Static Range LIS Query
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import sys\n\nsys.setrecursionlimit(10**6)\n\n\ndef StaticRangeLISQuery(P:\
    \ list[int], queries: list[tuple[int, int]]) -> list[int]:\n    \"\"\"\n    P\
    \ \u306F 1 <= P_i <= N\u306E\u9806\u5217.\n    \u533A\u9593[l,r)\u306ELIS\u6700\
    \u9577\u5897\u52A0\u90E8\u5206\u5217\u3092\u6C42\u3081\u308B.\n    \"\"\"\n  \
    \  n, q = len(P), len(queries)\n    mn = [0] * (1 << 20)\n    size = [0] * (n\
    \ + 1)\n\n    def build(x: int, L: int, R: int) -> None:\n        st = [(x, L,\
    \ R)]\n        while st:\n            x, L, R = st.pop()\n            mn[x] =\
    \ n + 1\n            if L == R:\n                size[L] = n + 1\n           \
    \     continue\n            m = (L + R) >> 1\n            st += [(x << 1, L, m),\
    \ (x << 1 | 1, m + 1, R)]\n\n    def update(x: int, L: int, R: int, p: int) ->\
    \ None:\n        st = [(x, ~L, R), (x, L, R)]\n        while st:\n           \
    \ x, L, R = st.pop()\n            if L >= 0:\n                if L == R:\n   \
    \                 mn[x] = size[p] = 0\n                    continue\n        \
    \        m = (L + R) >> 1\n                if p <= m:\n                    nx\
    \ = x << 1\n                    st += [(nx, ~L, m), (nx, L, m)]\n            \
    \    else:\n                    nx = x << 1 | 1\n                    st += [(nx,\
    \ ~(m + 1), R), (nx, m + 1, R)]\n                continue\n            mn[x] =\
    \ min(mn[x << 1], mn[x << 1 | 1])\n\n    def dfs(x: int, L: int, R: int, l: int,\
    \ r: int) -> None:\n        \"\"\"ToDo \u975E\u518D\u5E30\u5316\uFF08cur\u306E\
    \u51E6\u7406\uFF09\"\"\"\n        nonlocal cur\n        if cur <= mn[x]:\n   \
    \         return\n        if L == R:\n            size[L] = cur\n            mn[x],\
    \ cur = cur, mn[x]\n            return\n        m = (L + R) >> 1\n        if l\
    \ <= m:\n            dfs(x * 2, L, m, l, r)\n        if r > m:\n            dfs(x\
    \ * 2 + 1, m + 1, R, l, r)\n        mn[x] = min(mn[x * 2], mn[x * 2 + 1])\n\n\
    \    ql = [0] * (q + 1)\n    qry = [[] for _ in range(n + 1)]\n    for i, (l,\
    \ r) in enumerate(queries, 1):\n        ql[i] = l + 1\n        qry[r].append(i)\n\
    \n    build(1, 1, n)\n\n    ip = [0] * (n + 1)\n    for i, a in enumerate(P, 1):\n\
    \        ip[a] = i\n    for p in ip:\n        update(1, 1, n, p)\n        if p\
    \ < n:\n            cur = p\n            dfs(1, 1, n, p + 1, n)\n\n    ans = [0]\
    \ * q\n    cnt = [0] * (n + 1)\n    for i in range(1, n + 1):\n        p = size[i]\
    \ + 1\n        while p <= n:\n            cnt[p - 1] += 1\n            p += p\
    \ & -p\n        for u in qry[i]:\n            ret = 1 - ql[u]\n            p =\
    \ ql[u]\n            while p:\n                ret += cnt[p - 1]\n           \
    \     p -= p & -p\n            ans[u - 1] = ret\n    return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/static_range_lis_query.py
  requiredBy: []
  timestamp: '2024-05-28 15:29:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/static_range_lis_query.test.py
documentation_of: data_structure/static_range_lis_query.py
layout: document
redirect_from:
- /library/data_structure/static_range_lis_query.py
- /library/data_structure/static_range_lis_query.py.html
title: data_structure/static_range_lis_query.py
---
