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
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_A\n\
    \nfrom data_structure.basic.FoldableDeque import FoldableDeque\n\nque = FoldableDeque(lambda\
    \ x, y: x + y, 0)\nN, S = map(int, input().split())\nA = list(map(int, input().split()))\n\
    INF = float(\"inf\")\nans = INF\nn = 0\nfor i in range(N):\n    que.push(A[i])\n\
    \    n += 1\n    if que.fold() < S:\n        continue\n    while que:\n      \
    \  que.popleft()\n        n -= 1\n        if que.fold() < S:\n            ans\
    \ = min(ans, n + 1)\n            break\nprint(ans if ans != INF else 0)\n"
  dependsOn:
  - data_structure/basic/FoldableDeque.py
  isVerificationFile: true
  path: test/aoj/dsl/dsl_3_a_smallest_window1.test.py
  requiredBy: []
  timestamp: '2024-06-19 13:18:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/dsl/dsl_3_a_smallest_window1.test.py
layout: document
redirect_from:
- /verify/test/aoj/dsl/dsl_3_a_smallest_window1.test.py
- /verify/test/aoj/dsl/dsl_3_a_smallest_window1.test.py.html
title: test/aoj/dsl/dsl_3_a_smallest_window1.test.py
---
