---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/sortable_segtree.py
    title: data_structure/segtree/sortable_segtree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_set_range_sort_range_composite
    links:
    - https://judge.yosupo.jp/problem/point_set_range_sort_range_composite
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_sort_range_composite\n\
    \nfrom data_structure.segtree.sortable_segtree import SortableSegtree\n\nMOD =\
    \ 998244353\nmask = (1 << 30) - 1\n\n\ndef op(x, y):\n    x1, x2, x3 = x[0], x[1]\
    \ >> 30, x[1] & mask\n    y1, y2, y3 = y[0], y[1] >> 30, y[1] & mask\n    return\
    \ (\n        x1 * y1 % MOD,\n        ((y1 * x2 % MOD + y2) % MOD) << 30 | (x1\
    \ * y3 % MOD + x3) % MOD,\n    )\n\n\ne_ = (1, 0)\n\n\ndef toggle(x):\n    x1,\
    \ x2 = x\n    return (x1, (x2 & mask) << 30 | x2 >> 30)\n\n\nn, q = map(int, input().split())\n\
    P = []\nfor _ in range(n):\n    p, a, b = map(int, input().split())\n    P.append((p,\
    \ (a, b << 30 | b)))\n\nseg = SortableSegtree(op, e_, toggle, P)\nfor _ in range(q):\n\
    \    t, *qu = map(int, input().split())\n    if t == 0:\n        i, p, a, b =\
    \ qu\n        seg.set(i, p, (a, b << 30 | b))\n    elif t == 1:\n        l, r,\
    \ x = qu\n        a, b = seg.prod(l, r)\n        print((a * x + (b >> 30)) % MOD)\n\
    \    else:\n        l, r = qu\n        seg.sort(l, r, t == 3)\n"
  dependsOn:
  - data_structure/segtree/sortable_segtree.py
  isVerificationFile: true
  path: test/library_checker/data_structure/point_set_range_sort_range_composite.test.py
  requiredBy: []
  timestamp: '2024-08-29 22:20:26+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/point_set_range_sort_range_composite.test.py
layout: document
title: Point Set Range Sort Composite
---
