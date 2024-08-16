---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: data_structure/segtree/compressed_segtree.py
    title: "\u5EA7\u6A19\u5727\u7E2E\u30BB\u30B0\u30E1\u30F3\u30C8\u6728"
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
    \nfrom data_structure.segtree.compressed_segtree import CompressedSegtree\n\n\n\
    def op(x, y):\n    a, b = x\n    c, d = y\n    return (a * c, b * c + d)\n\n\n\
    e = (1, 0)\n\nn, m = map(int, input().split())\nA = []\nPs = dict()\nfor i in\
    \ range(m):\n    p, a, b = input().split()\n    p = int(p) - 1\n    a = float(a)\n\
    \    b = float(b)\n    A.append((p, a, b))\n    Ps[p] = (1, 0)\n\nmx = 1\nmn =\
    \ 1\nseg = CompressedSegtree(op, e, Ps)\nfor p, a, b in A:\n    seg[p] = (a, b)\n\
    \    a, b = seg.all_prod()\n    x = a + b\n    mx = max(mx, x)\n    mn = min(mn,\
    \ x)\nprint(mn)\nprint(mx)\n"
  dependsOn:
  - data_structure/segtree/compressed_segtree.py
  isVerificationFile: true
  path: test/atcoder/arc/arc008d_segtree.test.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: TEST_IGNORED
  verifiedWith: []
documentation_of: test/atcoder/arc/arc008d_segtree.test.py
layout: document
title: "D - \u30BF\u30B3\u30E4\u30AD\u30AA\u30A4\u30B7\u30AF\u30CA\u30FC\u30EB\uFF08\
  \u30BB\u30B0\u6728\uFF09"
---