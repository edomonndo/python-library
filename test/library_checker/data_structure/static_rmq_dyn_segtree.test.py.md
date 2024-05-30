---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/dynamic_segtree.py
    title: data_structure/segtree/dynamic_segtree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/staticrmq
    links:
    - https://judge.yosupo.jp/problem/staticrmq
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq\n\
    \nfrom data_structure.segtree.dynamic_segtree import DynamicSegtree\n\nn, q =\
    \ map(int, input().split())\nA = list(map(int, input().split()))\n\ninf = 1 <<\
    \ 60\nseg = DynamicSegtree(n, min, inf)\nfor i, a in enumerate(A):\n    seg[i]\
    \ = a\n\nfor _ in range(q):\n    l, r = map(int, input().split())\n    print(seg.prod(l,\
    \ r))\n"
  dependsOn:
  - data_structure/segtree/dynamic_segtree.py
  isVerificationFile: true
  path: test/library_checker/data_structure/static_rmq_dyn_segtree.test.py
  requiredBy: []
  timestamp: '2024-05-30 15:25:43+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/static_rmq_dyn_segtree.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/static_rmq_dyn_segtree.test.py
- /verify/test/library_checker/data_structure/static_rmq_dyn_segtree.test.py.html
title: test/library_checker/data_structure/static_rmq_dyn_segtree.test.py
---
