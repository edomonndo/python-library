---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/sort_points_by_argument
    links:
    - https://judge.yosupo.jp/problem/sort_points_by_argument
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sort_points_by_argument\n\
    \nfrom geometory.sort_points_by_argument import sortPointsByArgument\n\nN = int(input())\n\
    A = [tuple(map(int, input().split())) for _ in range(N)]\n\nans = sortPointsByArgument(A)\n\
    for x, y in ans:\n    print(x, y)\n"
  dependsOn: []
  isVerificationFile: true
  path: test/library_checker/geometory/sort_points_by_argument.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/geometory/sort_points_by_argument.test.py
layout: document
redirect_from:
- /verify/test/library_checker/geometory/sort_points_by_argument.test.py
- /verify/test/library_checker/geometory/sort_points_by_argument.test.py.html
title: test/library_checker/geometory/sort_points_by_argument.test.py
---
