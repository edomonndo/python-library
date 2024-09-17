---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/connectivity/link_cut_tree.py
    title: graph/connectivity/link_cut_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/dynamic_tree_vertex_set_path_composite
    links:
    - https://judge.yosupo.jp/problem/dynamic_tree_vertex_set_path_composite
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/dynamic_tree_vertex_set_path_composite\n\
    from graph.connectivity.link_cut_tree import LinkCutTree\n\nMOD = 998244353\n\
    N, Q = map(int, input().split())\nA = [(a << 32) | b for a, b in (map(int, input().split())\
    \ for _ in range(N))]\n\nmask = (1 << 32) - 1\n\n\ndef op(x, y):\n    ax, bx =\
    \ x >> 32, x & mask\n    ay, by = y >> 32, y & mask\n    return (ax * ay % MOD)\
    \ << 32 | (ay * bx + by) % MOD\n\n\nT = LinkCutTree(op, 1 << 32, A)\nfor _ in\
    \ range(N - 1):\n    u, v = map(int, input().split())\n    T.evert(u)\n    T.link(u,\
    \ v)\n\nans = []\nfor _ in range(Q):\n    t, *q = map(int, input().split())\n\
    \    if t == 0:\n        u, v, w, x = q\n        T.evert(u)\n        T.cut(v)\n\
    \        T.evert(w)\n        T.link(w, x)\n    elif t == 1:\n        p, c, d =\
    \ q\n        T.set(p, (c << 32) | d)\n    else:\n        u, v, x = q\n       \
    \ c = T.path_query(u, v)\n        a, b = c >> 32, c & mask\n        ans.append((a\
    \ * x + b) % MOD)\n\nprint(*ans, sep=\"\\n\")\n"
  dependsOn:
  - graph/connectivity/link_cut_tree.py
  isVerificationFile: true
  path: test/library_checker/tree/dynamic_tree_vertex_set_path_composite.test.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/tree/dynamic_tree_vertex_set_path_composite.test.py
layout: document
title: Dynamic Tree Vertex Set Path Composite
---
