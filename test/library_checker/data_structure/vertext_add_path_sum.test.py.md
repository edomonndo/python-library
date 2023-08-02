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
    PROBLEM: https://judge.yosupo.jp/problem/vertex_add_path_sum
    links:
    - https://judge.yosupo.jp/problem/vertex_add_path_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum\n\
    \nfrom tree.euler_tour import EulerTour\nfrom data_structure.segment_tree import\
    \ Segtree\n\nN, Q = map(int, input().split())\nA = list(map(int, input().split()))\n\
    G = [[] for _ in range(N)]\nfor _ in range(N - 1):\n    u, v = map(int, input().split())\n\
    \    G[u].append((1, v))\n    G[v].append((1, u))\n\net = EulerTour(N, G, 0, A)\n\
    segPQ = Segtree(et.vcost, (lambda x, y: x + y), 0)\nsegLca = Segtree(et.depth,\
    \ min, (10**9, N))\nfor _ in range(Q):\n    t, *q = map(int, input().split())\n\
    \    if t == 0:\n        p, x = q\n        segPQ.set(p, x)\n    elif t == 1:\n\
    \        u, v = q\n        if u == v:\n            lca = u\n        else:\n  \
    \          l, r = et.into[u], et.into[v]\n            if l > r:\n            \
    \    l, r = r, l\n            _, lca = segLca.prod(l, r + 1)\n        m = et.into[lca]\n\
    \        print(\n            segPQ.prod(0, l + 1)\n            + segPQ.prod(0,\
    \ r + 1)\n            - 2 * segPQ.prod(0, m + 1)\n            + segPQ.get(m)\n\
    \        )\n"
  dependsOn:
  - tree/euler_tour.py
  - data_structure/segment_tree.py
  isVerificationFile: true
  path: test/library_checker/data_structure/vertext_add_path_sum.test.py
  requiredBy: []
  timestamp: '2023-08-02 17:54:14+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/data_structure/vertext_add_path_sum.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/vertext_add_path_sum.test.py
- /verify/test/library_checker/data_structure/vertext_add_path_sum.test.py.html
title: test/library_checker/data_structure/vertext_add_path_sum.test.py
---
