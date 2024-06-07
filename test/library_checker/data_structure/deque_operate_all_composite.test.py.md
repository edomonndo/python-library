---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/basic/FoldableDeque.py
    title: Foldable Deque(DSWAG)
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/deque_operate_all_composite
    links:
    - https://judge.yosupo.jp/problem/deque_operate_all_composite
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/deque_operate_all_composite\n\
    \nfrom data_structure.basic.FoldableDeque import FoldableDeque\n\nMOD = 998244353\n\
    mask = (1 << 32) - 1\n\n\ndef op(x, y):\n    ax, bx = x >> 32, x & mask\n    ay,\
    \ by = y >> 32, y & mask\n    return (ax * ay % MOD) << 32 | (ay * bx + by) %\
    \ MOD\n\n\nque = FoldableDeque(op, 1 << 32)\nQ = int(input())\nfor _ in range(Q):\n\
    \    t, *q = map(int, input().split())\n    if t == 0:\n        a, b = q\n   \
    \     que.pushleft(a << 32 | b)\n    elif t == 1:\n        a, b = q\n        que.push(a\
    \ << 32 | b)\n    elif t == 2:\n        que.popleft()\n    elif t == 3:\n    \
    \    que.pop()\n    else:\n        x = q[0]\n        c = que.fold()\n        a,\
    \ b = c >> 32, c & mask\n        print((a * x + b) % MOD)\n"
  dependsOn:
  - data_structure/basic/FoldableDeque.py
  isVerificationFile: true
  path: test/library_checker/data_structure/deque_operate_all_composite.test.py
  requiredBy: []
  timestamp: '2024-06-07 11:47:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/deque_operate_all_composite.test.py
layout: document
title: Deque Operate All Composite
---
