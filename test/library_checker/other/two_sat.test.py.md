---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: other/two_sat.py
    title: 2 Sat
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/two_sat
    links:
    - https://judge.yosupo.jp/problem/two_sat
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_sat\n\n\
    from other.two_sat import two_sat\n\np, cnf, N, M = input().split()\nN, M = map(int,\
    \ (N, M))\nclause = []\nfor i in range(M):\n    a, b, z = map(int, input().split())\n\
    \    c, d = (a // abs(a) + 1) // 2, (b // abs(b) + 1) // 2\n    c, d = bool(c),\
    \ bool(d)\n    clause.append((abs(a) - 1, c, abs(b) - 1, d))\nresult = two_sat(N,\
    \ clause)\nif result is None:\n    print(\"s UNSATISFIABLE\")\nelse:\n    print(\"\
    s SATISFIABLE\")\n    print(\"v\", *[(i + 1) if result[i] else (-1 - i) for i\
    \ in range(N)] + [0])\n"
  dependsOn:
  - other/two_sat.py
  isVerificationFile: true
  path: test/library_checker/other/two_sat.test.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/other/two_sat.test.py
layout: document
title: 2 Sat
---
