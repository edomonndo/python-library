---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: dynamic_programming/edit_distance.py
    title: "\u7DE8\u96C6\u8DDD\u96E2"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/abc185/tasks/abc185_e
    links:
    - https://atcoder.jp/contests/abc185/tasks/abc185_e
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://atcoder.jp/contests/abc185/tasks/abc185_e


    from dynamic_programming.edit_distance import edit_distance


    n, m = map(int, input().split())

    S = [int(x) for x in input().split()]

    T = [int(x) for x in input().split()]

    print(edit_distance(S, T, 1, 1, 1))

    '
  dependsOn:
  - dynamic_programming/edit_distance.py
  isVerificationFile: true
  path: test/atcoder/abc100-199/abc185e.test.py
  requiredBy: []
  timestamp: '2024-06-24 17:29:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/abc100-199/abc185e.test.py
layout: document
title: E - Sequence Matching
---
