---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/hungarian.py
    title: graph/hungarian.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/assignment
    links:
    - https://judge.yosupo.jp/problem/assignment
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/assignment


    from graph.hungarian import hungarian


    N = int(input())

    A = [[int(x) for x in input().split()] for _ in range(N)]

    total, row = hungarian(A)

    print(total)

    print(*row)

    '
  dependsOn:
  - graph/hungarian.py
  isVerificationFile: true
  path: test/library_checker/graph/assignment.test.py
  requiredBy: []
  timestamp: '2024-02-09 16:12:14+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/assignment.test.py
layout: document
redirect_from:
- /verify/test/library_checker/graph/assignment.test.py
- /verify/test/library_checker/graph/assignment.test.py.html
title: test/library_checker/graph/assignment.test.py
---
