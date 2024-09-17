---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/chromatic_number.py
    title: graph/chromatic_number.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/chromatic_number
    links:
    - https://judge.yosupo.jp/problem/chromatic_number
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/chromatic_number


    from graph.chromatic_number import chromatic_number


    n, m = map(int, input().split())

    es = [tuple(map(int, input().split())) for _ in range(m)]

    print(chromatic_number(n, es))

    '
  dependsOn:
  - graph/chromatic_number.py
  isVerificationFile: true
  path: test/library_checker/graph/chromatic_number.test.py
  requiredBy: []
  timestamp: '2024-06-04 09:09:32+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/chromatic_number.test.py
layout: document
title: Chromatic Number
---

