---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: data_structure/fenwick_tree/value_range_sum.py
    title: data_structure/fenwick_tree/value_range_sum.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    IGNORE: https://atcoder.jp/contests/past17-open/tasks/past17_o
    links:
    - https://atcoder.jp/contests/past17-open/tasks/past17_o
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: IGNORE https://atcoder.jp/contests/past17-open/tasks/past17_o\n\
    \nfrom data_structure.fenwick_tree.value_range_sum import CompressedValueRangeSum\n\
    \nn = int(input())\nA = [int(x) for x in input().split()]\nps = set(A)\nq = int(input())\n\
    qs = [tuple(map(int, input().split())) for _ in range(q)]\nB = A[:]\nfor t, *qu\
    \ in qs:\n    if t == 1:\n        k, d = qu\n        k -= 1\n        B[k] += d\n\
    \        ps.add(B[k])\n    else:\n        ps.add(qu[0])\nS = CompressedValueRangeSum(A,\
    \ ps)\nfor t, *qu in qs:\n    if t == 1:\n        k, d = qu\n        k -= 1\n\
    \        S.add(k, d)\n    else:\n        x = qu[0]\n        print(S.sum_abs_from(x))\n"
  dependsOn:
  - data_structure/fenwick_tree/value_range_sum.py
  isVerificationFile: true
  path: test/atcoder/past17o.test.py
  requiredBy: []
  timestamp: '2024-06-19 11:57:13+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/atcoder/past17o.test.py
layout: document
redirect_from:
- /verify/test/atcoder/past17o.test.py
- /verify/test/atcoder/past17o.test.py.html
title: test/atcoder/past17o.test.py
---
