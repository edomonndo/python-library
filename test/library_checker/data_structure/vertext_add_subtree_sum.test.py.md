---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: data_structure/segment_tree.py
    title: Segment Tree
  - icon: ':x:'
    path: tree/euler_tour.py
    title: tree/euler_tour.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/vertex_add_subtree_sum
    links:
    - https://judge.yosupo.jp/problem/vertex_add_subtree_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_subtree_sum\n\
    \nfrom tree.euler_tour import EulerTour\nfrom data_structure.segment_tree import\
    \ Segtree\n\nN, Q = map(int, input().split())\nA = list(map(int, input().split()))\n\
    P = list(map(int, input().split()))\nG = [[] for _ in range(N)]\nfor i, p in enumerate(P,\
    \ 1):\n    G[i].append((1, p))\n    G[p].append((1, i))\n\net = EulerTour(N, G,\
    \ 0, A)\nseg = Segtree(et.vcost_st, (lambda x, y: x + y), 0)\nfor _ in range(Q):\n\
    \    t, *q = map(int, input().split())\n    if t == 0:\n        u, x = q\n   \
    \     cur = seg.get(u)\n        seg.set(u, cur + x)\n    elif t == 1:\n      \
    \  u = q[0]\n        print(seg.prod(et.into[u], et.out[u]))\n"
  dependsOn:
  - tree/euler_tour.py
  - data_structure/segment_tree.py
  isVerificationFile: true
  path: test/library_checker/data_structure/vertext_add_subtree_sum.test.py
  requiredBy: []
  timestamp: '2023-08-02 17:54:14+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/data_structure/vertext_add_subtree_sum.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/vertext_add_subtree_sum.test.py
- /verify/test/library_checker/data_structure/vertext_add_subtree_sum.test.py.html
title: test/library_checker/data_structure/vertext_add_subtree_sum.test.py
---
