---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: graph/tree/hld_lazysegtree.py
    title: "HL\u5206\u89E3\u6728\u4E0A\u306E\u9045\u5EF6\u30BB\u30B0\u6728"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/past202010-open/tasks/past202010_m
    links:
    - https://atcoder.jp/contests/past202010-open/tasks/past202010_m
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/past202010-open/tasks/past202010_m\n\
    \nfrom graph.tree.hld_lazysegtree import HldLazySegTree\n\n\nn, q = map(int, input().split())\n\
    edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n -\
    \ 1)]\n\ninf = float(\"inf\")\nmapping = lambda f, x: x if f == ID else f\ncomposition\
    \ = lambda f, g: g if f == ID else f\nID = inf\nseg = HldLazySegTree(min, inf,\
    \ mapping, composition, ID, [0] * n, n, edges, 0)\n\nfor _ in range(q):\n    u,\
    \ v, c = map(int, input().split())\n    u -= 1\n    v -= 1\n    seg.path_apply(u,\
    \ v, c, True)\n\nfor u, v in edges:\n    print(seg.path_prod(u, v, True))\n"
  dependsOn:
  - graph/tree/hld_lazysegtree.py
  isVerificationFile: true
  path: test/atcoder/past/past4m_hld2.test.py
  requiredBy: []
  timestamp: '2024-09-01 03:12:20+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/past/past4m_hld2.test.py
layout: document
title: "M - \u7B46\u5857\u308A"
---
