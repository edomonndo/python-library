---
data:
  _extendedDependsOn: []
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
  dependsOn: []
  isVerificationFile: true
  path: library_checker/data_structure/vertext_add_subtree_sum.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: library_checker/data_structure/vertext_add_subtree_sum.test.py
layout: document
redirect_from:
- /verify/library_checker/data_structure/vertext_add_subtree_sum.test.py
- /verify/library_checker/data_structure/vertext_add_subtree_sum.test.py.html
title: library_checker/data_structure/vertext_add_subtree_sum.test.py
---
