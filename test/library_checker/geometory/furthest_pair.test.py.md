---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: geometory/diameter.py
    title: "\u591A\u89D2\u5F62\u306E\u76F4\u5F84"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/furthest_pair
    links:
    - https://judge.yosupo.jp/problem/furthest_pair
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/furthest_pair\n\
    \nfrom geometory.diameter import diameter\n\nt = int(input())\nfor _ in range(t):\n\
    \    n = int(input())\n    ps = [tuple(map(int, input().split())) for _ in range(n)]\n\
    \    _, p, q = diameter(ps)\n    i = j = -1\n    for k, (x, y) in enumerate(ps):\n\
    \        if i == -1:\n            if p.x == x and p.y == y:\n                i\
    \ = k\n            elif q.x == x and q.y == y:\n                i = k\n      \
    \          p, q = q, p\n        else:\n            if i != k and q.x == x and\
    \ q.y == y:\n                j = k\n                break\n    print(i, j)\n"
  dependsOn:
  - geometory/diameter.py
  isVerificationFile: true
  path: test/library_checker/geometory/furthest_pair.test.py
  requiredBy: []
  timestamp: '2024-08-14 14:54:08+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/geometory/furthest_pair.test.py
layout: document
title: Furthest Pair of Points
---
