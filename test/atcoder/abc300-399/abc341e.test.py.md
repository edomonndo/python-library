---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/lazy_segment_tree.py
    title: data_structure/segtree/lazy_segment_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/abc341/tasks/abc341_e
    links:
    - https://atcoder.jp/contests/abc341/tasks/abc341_e
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc341/tasks/abc341_e\n\
    \nfrom data_structure.segtree.lazy_segment_tree import LazySegtree\n\n\ndef op(x,\
    \ y):\n    if x == -1:\n        return y\n    if y == -1:\n        return x\n\
    \    ok1, l1, r1 = x >> 2 & 1, x >> 1 & 1, x & 1\n    ok2, l2, r2 = y >> 2 & 1,\
    \ y >> 1 & 1, y & 1\n    if ok1 and ok2 and r1 != l2:\n        ok = 1\n    else:\n\
    \        ok = 0\n    return ok << 2 | l1 << 1 | r2\n\n\ndef mapping(f: int, x):\n\
    \    if f and x != -1:\n        ok, l, r = x >> 2 & 1, x >> 1 & 1, x & 1\n   \
    \     l ^= 1\n        r ^= 1\n        return ok << 2 | l << 1 | r\n    else:\n\
    \        return x\n\n\ndef composition(g: int, f: int):\n    return g ^ f\n\n\n\
    n, q = map(int, input().split())\nS = [int(x) for x in input()]\ng = LazySegtree(\n\
    \    [1 << 2 | 1 << 1 | 1 if s else 1 << 2 for s in S], op, -1, mapping, composition,\
    \ 0\n)\nfor _ in range(q):\n    t, l, r = map(int, input().split())\n    l -=\
    \ 1\n    if t == 1:\n        g.apply(l, r, 1)\n    else:\n        res = g.prod(l,\
    \ r)\n        print(\"Yes\" if (res >> 2) & 1 else \"No\")\n"
  dependsOn:
  - data_structure/segtree/lazy_segment_tree.py
  isVerificationFile: true
  path: test/atcoder/abc300-399/abc341e.test.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/abc300-399/abc341e.test.py
layout: document
redirect_from:
- /verify/test/atcoder/abc300-399/abc341e.test.py
- /verify/test/atcoder/abc300-399/abc341e.test.py.html
title: test/atcoder/abc300-399/abc341e.test.py
---
