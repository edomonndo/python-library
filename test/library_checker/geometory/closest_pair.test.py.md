---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/closest_pair.py
    title: geometory/closest_pair.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/closest_pair
    links:
    - https://judge.yosupo.jp/problem/closest_pair
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/closest_pair\n\
    \nfrom geometory.closest_pair import closest_pair\n\nt = int(input())\nfor _ in\
    \ range(t):\n    n = int(input())\n    ps = [tuple(map(int, input().split()))\
    \ for _ in range(n)]\n    _, p, q = closest_pair(ps)\n    i = j = -1\n    for\
    \ k, (x, y) in enumerate(ps):\n        if p.x == x and p.y == y and i == -1:\n\
    \            i = k\n        elif q.x == x and q.y == y and j == -1:\n        \
    \    j = k\n    print(i, j)\n"
  dependsOn:
  - geometory/closest_pair.py
  isVerificationFile: true
  path: test/library_checker/geometory/closest_pair.test.py
  requiredBy: []
  timestamp: '2024-08-15 10:59:11+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/geometory/closest_pair.test.py
layout: document
title: Closest Pair of Points
---
