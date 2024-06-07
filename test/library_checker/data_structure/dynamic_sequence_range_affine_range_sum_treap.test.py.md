---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/binary_search_tree/implicit_treap.py
    title: "\u5E73\u8861\u4E8C\u5206\u63A2\u7D22\u6728(Implicit Treap)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/dynamic_sequence_range_affine_range_sum
    links:
    - https://judge.yosupo.jp/problem/dynamic_sequence_range_affine_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/dynamic_sequence_range_affine_range_sum\n\
    from typing import TypeVar\nfrom data_structure.binary_search_tree.implicit_treap\
    \ import ImplicitTreap\n\nS = TypeVar(\"S\")\nF = TypeVar(\"F\")\n\nMOD = 998244353\n\
    \nmsk = (1 << 32) - 1\n\n\ndef op(x: S, y: S) -> S:\n    x1, x2 = x >> 32, x &\
    \ msk\n    y1, y2 = y >> 32, y & msk\n    return (((x1 + y1) % MOD) << 32) + ((x2\
    \ + y2) % MOD)\n\n\ndef mapping(f: F, x: S) -> S:\n    f1, f2 = f >> 32, f & msk\n\
    \    x1, x2 = x >> 32, x & msk\n    return (((f1 * x1 % MOD + f2 * x2 % MOD) %\
    \ MOD) << 32) + x2\n\n\ndef composition(f: F, g: F) -> F:\n    f1, f2 = f >> 32,\
    \ f & msk\n    g1, g2 = g >> 32, g & msk\n    return ((f1 * g1 % MOD) << 32) +\
    \ ((f1 * g2 % MOD + f2) % MOD)\n\n\nn, q = map(int, input().split())\nA = [(int(a)\
    \ << 32) + 1 for a in input().split()]\n\nT = ImplicitTreap(op, 0, mapping, composition,\
    \ 1 << 32, A)\n\nans = []\nfor _ in range(q):\n    t, *qu = map(int, input().split())\n\
    \    if t == 0:\n        i, x = qu\n        if i < T.size():\n            T.insert(i,\
    \ (x << 32) + 1)\n        else:\n            T.insert(T.size(), (x << 32) + 1)\n\
    \    elif t == 1:\n        i = qu[0]\n        T.erase(i)\n    elif t == 2:\n \
    \       l, r = qu\n        T.reverse(l, r)\n    elif t == 3:\n        l, r, b,\
    \ c = qu\n        T.apply(l, r, (b << 32) + c)\n    else:\n        l, r = qu\n\
    \        ans.append(T.prod(l, r) >> 32)\nprint(*ans, sep=\"\\n\")\n"
  dependsOn:
  - data_structure/binary_search_tree/implicit_treap.py
  isVerificationFile: true
  path: test/library_checker/data_structure/dynamic_sequence_range_affine_range_sum_treap.test.py
  requiredBy: []
  timestamp: '2024-06-07 10:09:10+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/dynamic_sequence_range_affine_range_sum_treap.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/dynamic_sequence_range_affine_range_sum_treap.test.py
- /verify/test/library_checker/data_structure/dynamic_sequence_range_affine_range_sum_treap.test.py.html
title: test/library_checker/data_structure/dynamic_sequence_range_affine_range_sum_treap.test.py
---
