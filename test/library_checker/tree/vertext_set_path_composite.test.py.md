---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: data_structure/segtree/segment_tree.py
    title: "\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Segment Tree)"
  - icon: ':question:'
    path: graph/tree/heavy_light_decomposition.py
    title: "HL\u5206\u89E3"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/vertex_set_path_composite
    links:
    - https://judge.yosupo.jp/problem/vertex_set_path_composite
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_set_path_composite\n\
    \nfrom data_structure.segtree.segment_tree import Segtree\nfrom graph.tree.heavy_light_decomposition\
    \ import HeavyLightDecomposition\n\nMOD = 998244353\nmsk = (1 << 32) - 1\n\n\n\
    def op1(x, y):\n    x1, x2 = x >> 32, x & msk\n    y1, y2 = y >> 32, y & msk\n\
    \    z1 = x1 * y1 % MOD\n    z2 = (x2 * y1 % MOD + y2) % MOD\n    return (z1 <<\
    \ 32) + z2\n\n\ndef op2(x, y):\n    x1, x2 = x >> 32, x & msk\n    y1, y2 = y\
    \ >> 32, y & msk\n    z1 = x1 * y1 % MOD\n    z2 = (x1 * y2 % MOD + x2) % MOD\n\
    \    return (z1 << 32) + z2\n\n\ndef f(x, y):\n    global ans\n    if x <= y:\n\
    \        res = seg1.prod(x, y)\n    else:\n        res = seg2.prod(y, x)\n   \
    \ s, t = res >> 32, res & msk\n    ans = (s * ans % MOD + t) % MOD\n\n\nn, q =\
    \ map(int, input().split())\nA = [0] * n\nB = [0] * n\nfor i in range(n):\n  \
    \  A[i], B[i] = map(int, input().split())\nedges = [tuple(map(int, input().split()))\
    \ for _ in range(n - 1)]\nH = HeavyLightDecomposition(n, edges, 0)\nP = [None]\
    \ * n\nfor h, a, b in zip(H.into, A, B):\n    P[h] = (a << 32) + b\n\nseg1 = Segtree(P,\
    \ op1, 1 << 32)\nseg2 = Segtree(P, op2, 1 << 32)\n\nfor _ in range(q):\n    t,\
    \ a, b, c = map(int, input().split())\n    if t == 0:\n        p = H.into[a]\n\
    \        seg1.set(p, (b << 32) + c)\n        seg2.set(p, (b << 32) + c)\n    else:\n\
    \        ans = c\n        H.path_noncommutative_query(a, b, f)\n        print(ans)\n"
  dependsOn:
  - data_structure/segtree/segment_tree.py
  - graph/tree/heavy_light_decomposition.py
  isVerificationFile: true
  path: test/library_checker/tree/vertext_set_path_composite.test.py
  requiredBy: []
  timestamp: '2024-09-01 09:34:08+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/tree/vertext_set_path_composite.test.py
layout: document
title: Vertex Set Path Composite
---
