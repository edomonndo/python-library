---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/interval_manager.py
    title: data_structure/interval_manager.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/past202104-open/tasks/past202104_m
    links:
    - https://atcoder.jp/contests/past202104-open/tasks/past202104_m
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/past202104-open/tasks/past202104_m\n\
    \nfrom data_structure.interval_manager import IntervalManager\n\nfrom collections\
    \ import defaultdict\n\nn = int(input())\nA = [int(x) for x in input().split()]\n\
    \n\nd = defaultdict(int)\n\n\ndef add(l, r, x):\n    global score\n    score -=\
    \ d[x] * (d[x] - 1) // 2\n    d[x] += r - l\n    score += d[x] * (d[x] - 1) //\
    \ 2\n\n\ndef remove(l, r, x):\n    add(r, l, x)\n\n\nscore = 0\nim = IntervalManager(A,\
    \ add, remove)\n\nQ = int(input())\nfor _ in range(Q):\n    l, r, x = map(int,\
    \ input().split())\n    im.update(l - 1, r, x)\n    print(score)\n"
  dependsOn:
  - data_structure/interval_manager.py
  isVerificationFile: true
  path: test/atcoder/past/past6m.test.py
  requiredBy: []
  timestamp: '2024-06-24 17:00:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/past/past6m.test.py
layout: document
title: "M - \u7B49\u3057\u3044\u6570"
---
