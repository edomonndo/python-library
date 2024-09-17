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
    ERROR: 1e-6
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/5/CGL_5_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/5/CGL_5_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/5/CGL_5_A\n\
    # verification-helper: ERROR 1e-6\n\nfrom geometory.closest_pair import closest_pair\n\
    \nn = int(input())\nps = []\nfor _ in range(n):\n    x, y = map(float, input().split())\n\
    \    ps.append((x * 10**6, y * 10**6))\nd, _, _ = closest_pair(ps)\nprint(d /\
    \ (10**6))\n"
  dependsOn:
  - geometory/closest_pair.py
  isVerificationFile: true
  path: test/aoj/cgl/cgl_5_a_closest_pair.test.py
  requiredBy: []
  timestamp: '2024-08-16 14:15:07+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/cgl/cgl_5_a_closest_pair.test.py
layout: document
title: "CGL5A \u6700\u8FD1\u70B9\u5BFE"
---

