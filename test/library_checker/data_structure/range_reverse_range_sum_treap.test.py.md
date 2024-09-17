---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/binary_search_tree/implicit_treap.py
    title: data_structure/binary_search_tree/implicit_treap.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/range_reverse_range_sum
    links:
    - https://judge.yosupo.jp/problem/range_reverse_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_reverse_range_sum\n\
    \nfrom data_structure.binary_search_tree.implicit_treap import ImplicitTreap\n\
    \nn, q = map(int, input().split())\nA = [int(x) for x in input().split()]\n\n\
    T = ImplicitTreap(lambda x, y: x + y, 0, lambda f, x: x, lambda f, g: g, 0, A)\n\
    \nans = []\nfor _ in range(q):\n    t, l, r = map(int, input().split())\n    if\
    \ t == 0:\n        T.reverse(l, r)\n    else:\n        ans.append(T.prod(l, r))\n\
    print(*ans, sep=\"\\n\")\n"
  dependsOn:
  - data_structure/binary_search_tree/implicit_treap.py
  isVerificationFile: true
  path: test/library_checker/data_structure/range_reverse_range_sum_treap.test.py
  requiredBy: []
  timestamp: '2024-06-07 10:09:10+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/range_reverse_range_sum_treap.test.py
layout: document
title: Range Reverse Range Sum (Treap)
---
