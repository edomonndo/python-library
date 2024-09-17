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
  _verificationStatusIcon: ':grey_question:'
  attributes:
    IGNORE: https://atcoder.jp/contests/abc035/tasks/abc035_c
    links:
    - https://atcoder.jp/contests/abc035/tasks/abc035_c
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: IGNORE https://atcoder.jp/contests/abc035/tasks/abc035_c\n\
    \nfrom data_structure.segtree.lazy_segment_tree import LazySegtree\n\n\ndef mapping(f,\
    \ x):\n    return not x if f else x\n\n\ndef composition(g, f):\n    return g\
    \ ^ f\n\n\nID = 0\n\nn, q = map(int, input().split())\nst = LazySegtree([0] *\
    \ n, max, -1, mapping, composition, ID)\n\nfor _ in range(q):\n    l, r = map(int,\
    \ input().split())\n    st.apply(l - 1, r, 1)\n\nprint(\"\".join(\"1\" if st.get(i)\
    \ else \"0\" for i in range(n)))\n"
  dependsOn:
  - data_structure/segtree/lazy_segment_tree.py
  isVerificationFile: true
  path: test/atcoder/abc001-99/abc035c.test.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: TEST_IGNORED
  verifiedWith: []
documentation_of: test/atcoder/abc001-99/abc035c.test.py
layout: document
title: "C - \u30AA\u30BB\u30ED"
---
