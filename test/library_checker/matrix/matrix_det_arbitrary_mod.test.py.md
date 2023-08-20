---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: matrix/matrix.py
    title: "\u884C\u5217"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/matrix_det_arbitrary_mod
    links:
    - https://judge.yosupo.jp/problem/matrix_det_arbitrary_mod
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_det_arbitrary_mod


    from matrix.matrix import determinant_arbitrary_mod


    N, M = map(int, input().split())

    A = [list(map(int, input().split())) for _ in range(N)]


    print(determinant_arbitrary_mod(N, A, M))

    '
  dependsOn:
  - matrix/matrix.py
  isVerificationFile: true
  path: test/library_checker/matrix/matrix_det_arbitrary_mod.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/matrix/matrix_det_arbitrary_mod.test.py
layout: document
redirect_from:
- /verify/test/library_checker/matrix/matrix_det_arbitrary_mod.test.py
- /verify/test/library_checker/matrix/matrix_det_arbitrary_mod.test.py.html
title: test/library_checker/matrix/matrix_det_arbitrary_mod.test.py
---
