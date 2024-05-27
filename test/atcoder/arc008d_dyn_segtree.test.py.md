---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: data_structure/dynamic_segtree.py
    title: data_structure/dynamic_segtree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':grey_question:'
  attributes:
    IGNORE: https://atcoder.jp/contests/arc008/tasks/arc008_4
    links:
    - https://atcoder.jp/contests/arc008/tasks/arc008_4
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: IGNORE https://atcoder.jp/contests/arc008/tasks/arc008_4\n\
    \nfrom data_structure.dynamic_segtree import DynamicSegtree\n\n\ndef op(x, y):\n\
    \    a, b = x\n    c, d = y\n    return (a * c, b * c + d)\n\n\ne = (1, 0)\n\n\
    n, m = map(int, input().split())\nseg = DynamicSegtree(n, op, e)\ninf = float(\"\
    inf\")\nmx = 1\nmn = 1\nfor i in range(m):\n    p, a, b = input().split()\n  \
    \  seg[int(p) - 1] = (float(a), float(b))\n    a, b = seg.all_prod()\n    x =\
    \ a + b\n    mx = max(mx, x)\n    mn = min(mn, x)\n\nprint(mn)\nprint(mx)\n"
  dependsOn:
  - data_structure/dynamic_segtree.py
  isVerificationFile: true
  path: test/atcoder/arc008d_dyn_segtree.test.py
  requiredBy: []
  timestamp: '2024-05-27 17:45:23+09:00'
  verificationStatus: TEST_IGNORED
  verifiedWith: []
documentation_of: test/atcoder/arc008d_dyn_segtree.test.py
layout: document
redirect_from:
- /verify/test/atcoder/arc008d_dyn_segtree.test.py
- /verify/test/atcoder/arc008d_dyn_segtree.test.py.html
title: test/atcoder/arc008d_dyn_segtree.test.py
---
