---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/lazy_segment_tree.py
    title: "\u9045\u5EF6\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Lazy Segment Tree)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/range_affine_range_sum
    links:
    - https://judge.yosupo.jp/problem/range_affine_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_affine_range_sum\n\
    from data_structure.segtree.lazy_segment_tree import LazySegtree\n\nMOD = 998244353\n\
    mask = (1 << 30) - 1\ne = 0\nID = 1 << 30\n\n\ndef op(x, y):\n    a, b = x >>\
    \ 30, x & mask\n    c, d = y >> 30, y & mask\n    e, f = (a + c) % MOD, b + d\n\
    \    return e << 30 | f\n\n\ndef mapping(F, x):\n    a, b = F >> 30, F & mask\n\
    \    c, d = x >> 30, x & mask\n    e, f = (a * c + b * d) % MOD, d\n    return\
    \ e << 30 | f\n\n\ndef composition(F, G):\n    a, b = F >> 30, F & mask\n    c,\
    \ d = G >> 30, G & mask\n    e, f = a * c % MOD, (a * d + b) % MOD\n    return\
    \ e << 30 | f\n\n\nN, Q = map(int, input().split())\nA = [int(x) for x in input().split()]\n\
    g = LazySegtree([(a << 30) | 1 for a in A], op, e, mapping, composition, ID)\n\
    for _ in range(Q):\n    t, *q = map(int, input().split())\n    if t == 0:\n  \
    \      l, r, b, c = q\n        g.apply(l, r, b << 30 | c)\n    else:\n       \
    \ l, r = q\n        ab = g.prod(l, r)\n        a, b = ab >> 30, ab & mask\n  \
    \      print(a)\n"
  dependsOn:
  - data_structure/segtree/lazy_segment_tree.py
  isVerificationFile: true
  path: test/library_checker/data_structure/range_affine_range_sum.test.py
  requiredBy: []
  timestamp: '2024-05-30 15:25:43+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/range_affine_range_sum.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/range_affine_range_sum.test.py
- /verify/test/library_checker/data_structure/range_affine_range_sum.test.py.html
title: test/library_checker/data_structure/range_affine_range_sum.test.py
---
