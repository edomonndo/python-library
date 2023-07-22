---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: geometory/convex_layers.py
    title: geometory/convex_layers.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/convex_layers
    links:
    - https://judge.yosupo.jp/problem/convex_layers
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/convex_layers


    from geometory.convex_layers import convex_layers


    N = int(input())

    A = [tuple(map(int, input().split())) for _ in range(N)]


    ans = convex_layers(A)

    print(*ans, sep="\n")

    '
  dependsOn:
  - geometory/convex_layers.py
  isVerificationFile: true
  path: library_checker/geometory/convex_layers.test.py
  requiredBy: []
  timestamp: '2023-07-23 01:42:59+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: library_checker/geometory/convex_layers.test.py
layout: document
redirect_from:
- /verify/library_checker/geometory/convex_layers.test.py
- /verify/library_checker/geometory/convex_layers.test.py.html
title: library_checker/geometory/convex_layers.test.py
---
