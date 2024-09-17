---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/merge_sort_tree.py
    title: data_structure/segtree/merge_sort_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/abc339/tasks/abc339_g
    links:
    - https://atcoder.jp/contests/abc339/tasks/abc339_g
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc339/tasks/abc339_g\n\
    \nfrom data_structure.segtree.merge_sort_tree import MergeSortTree\n\nn = int(input())\n\
    A = [int(x) for x in input().split()]\nq = int(input())\nt = MergeSortTree(A)\n\
    res = 0\nfor _ in range(q):\n    a, b, c = map(int, input().split())\n    l, r,\
    \ x = a ^ res, b ^ res, c ^ res\n    res = t.sum_le(l - 1, r, x)\n    print(res)\n"
  dependsOn:
  - data_structure/segtree/merge_sort_tree.py
  isVerificationFile: true
  path: test/atcoder/abc300-399/abc339g.test.py
  requiredBy: []
  timestamp: '2024-06-24 17:29:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/abc300-399/abc339g.test.py
layout: document
redirect_from:
- /verify/test/atcoder/abc300-399/abc339g.test.py
- /verify/test/atcoder/abc300-399/abc339g.test.py.html
title: test/atcoder/abc300-399/abc339g.test.py
---
