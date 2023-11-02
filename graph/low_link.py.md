---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl_3_a_articulation_points.test.py
    title: test/aoj/grl_3_a_articulation_points.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl_3_b_bridges.test.py
    title: test/aoj/grl_3_b_bridges.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import sys\n\nsys.setrecursionlimit(10**5)\n\n\ndef low_link(\n    N: int,\
    \ G: list[list[int]], start: int = 0\n) -> tuple[list[int], list[tuple[int, int]]]:\n\
    \    INF = float(\"inf\")\n    articulation = []\n    bridge = []\n    order =\
    \ [None] * N\n    low = [INF] * N\n\n    def _dfs(cur, pre, k):\n        order[cur]\
    \ = low[cur] = k\n        is_articulation = False\n        cnt = 0\n        for\
    \ nxt in G[cur]:\n            if order[nxt] is None:\n                cnt += 1\n\
    \                _dfs(nxt, cur, k + 1)\n                if low[cur] > low[nxt]:\n\
    \                    low[cur] = low[nxt]\n                is_articulation |= pre\
    \ >= 0 and low[nxt] >= order[cur]\n                if order[cur] < low[nxt]:\n\
    \                    if cur < nxt:\n                        bridge.append((cur,\
    \ nxt))\n                    else:\n                        bridge.append((nxt,\
    \ cur))\n            elif nxt != pre and low[cur] > order[nxt]:\n            \
    \    low[cur] = order[nxt]\n        is_articulation |= pre < 0 and cnt > 1\n \
    \       if is_articulation:\n            articulation.append(cur)\n\n    _dfs(start,\
    \ -1, 0)\n\n    return articulation, bridge\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/low_link.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl_3_a_articulation_points.test.py
  - test/aoj/grl_3_b_bridges.test.py
documentation_of: graph/low_link.py
layout: document
title: "\u9593\u63A5\u70B9\uFF0C\u6A4B"
---

グラフから取り除くと連結でなくなる頂点(間接点)と辺(橋)を求める．