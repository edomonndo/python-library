---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segment_tree.py
    title: "\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Segment Tree)"
  - icon: ':heavy_check_mark:'
    path: tree/euler_tour.py
    title: Euler tour
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_C
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.12/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.12/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_C\n\
    \nfrom tree.euler_tour import EulerTour\nfrom data_structure.segment_tree import\
    \ Segtree\n\nN = int(input())\nG = [[] for _ in range(N)]\nfor i in range(N):\n\
    \    k, *es = map(int, input().split())\n    for e in es:\n        G[i].append((1,\
    \ e))\n        G[e].append((1, i))\n\net = EulerTour(N, G, 0, [0] * N)\nseg =\
    \ Segtree(et.depth, min, (10**9, -1))\nQ = int(input())\nfor _ in range(Q):\n\
    \    u, v = map(int, input().split())\n    if u == v:\n        print(u)\n    \
    \    continue\n    l, r = et.into[u], et.into[v]\n    if l > r:\n        l, r\
    \ = r, l\n    _, lca = seg.prod(l, r)\n    if lca < 0:\n        print(et.parent[~lca])\n\
    \    else:\n        print(lca)\n"
  dependsOn:
  - tree/euler_tour.py
  - data_structure/segment_tree.py
  isVerificationFile: true
  path: test/aoj/grl_5_c_lowest_common_ancestor.test.py
  requiredBy: []
  timestamp: '2023-08-26 01:45:36+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl_5_c_lowest_common_ancestor.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl_5_c_lowest_common_ancestor.test.py
- /verify/test/aoj/grl_5_c_lowest_common_ancestor.test.py.html
title: test/aoj/grl_5_c_lowest_common_ancestor.test.py
---
