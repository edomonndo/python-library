---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: atcoder/lazysegtree.py
    title: atcoder/lazysegtree.py
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
    from atcoder.lazysegtree import LazySegTree\n\n\ndef mapping(f, x):\n    return\
    \ not x if f else x\n\n\ndef composition(g, f):\n    return g ^ f\n\n\nID = 0\n\
    \nn, q = map(int, input().split())\nst = LazySegTree(max, -1, mapping, composition,\
    \ ID, [0] * n)\n\nfor _ in range(q):\n    l, r = map(int, input().split())\n \
    \   st.apply(l - 1, r, 1)\n\nprint(\"\".join(\"1\" if st.get(i) else \"0\" for\
    \ i in range(n)))\n"
  dependsOn:
  - atcoder/lazysegtree.py
  isVerificationFile: true
  path: test/atcoder/abc035c.test.py
  requiredBy: []
  timestamp: '2024-05-29 14:24:11+09:00'
  verificationStatus: TEST_IGNORED
  verifiedWith: []
documentation_of: test/atcoder/abc035c.test.py
layout: document
redirect_from:
- /verify/test/atcoder/abc035c.test.py
- /verify/test/atcoder/abc035c.test.py.html
title: test/atcoder/abc035c.test.py
---
