---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/range_set_range_composite.py
    title: data_structure/segtree/range_set_range_composite.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/range_set_range_composite
    links:
    - https://judge.yosupo.jp/problem/range_set_range_composite
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_set_range_composite\n\
    \nfrom data_structure.segtree.range_set_range_composite import RangeSetRangeComposite\n\
    \nMOD = 998244353\nmask = (1 << 30) - 1\n\n\ndef op(x, y):\n    x0, x1 = x >>\
    \ 30, x & mask\n    y0, y1 = y >> 30, y & mask\n    return (x0 * y0 % MOD) <<\
    \ 30 | ((y0 * x1 + y1) % MOD)\n\n\ndef pow_(x: int, y: int):\n    x0, x1 = x >>\
    \ 30, x & mask\n    a = pow(x0, y, MOD)\n    if x0 <= 1:\n        b = y * x0 *\
    \ x1 % MOD\n    else:\n        b = (a - 1) * pow(x0 - 1, -1, MOD) * x1 % MOD\n\
    \    return a << 30 | b\n\n\nn, q = map(int, input().split())\nA = []\nfor _ in\
    \ range(n):\n    a, b = map(int, input().split())\n    A.append(a << 30 | b)\n\
    seg = RangeSetRangeComposite(op, 1 << 30, pow_, 1 << 30, A)\nfor _ in range(q):\n\
    \    t, *qu = map(int, input().split())\n    if t == 0:\n        l, r, c, d =\
    \ qu\n        seg.apply(l, r, c << 30 | d)\n    else:\n        l, r, x = qu\n\
    \        res = seg.prod(l, r)\n        a, b = res >> 30, res & mask\n        print((a\
    \ * x + b) % MOD)\n"
  dependsOn:
  - data_structure/segtree/range_set_range_composite.py
  isVerificationFile: true
  path: test/library_checker/data_structure/range_set_range_composite.test.py
  requiredBy: []
  timestamp: '2024-08-14 05:50:48+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/range_set_range_composite.test.py
layout: document
title: Range Set Range Composite
---
