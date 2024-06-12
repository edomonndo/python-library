---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: math_/primitive_root.py
    title: "\u539F\u59CB\u6839"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/primitive_root
    links:
    - https://judge.yosupo.jp/problem/primitive_root
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/primitive_root\n\
    \nfrom math_.primitive_root import primitive_root\n\n\nq = int(input())\nfor _\
    \ in range(q):\n    p = int(input())\n    print(primitive_root(p))\n"
  dependsOn:
  - math_/primitive_root.py
  isVerificationFile: false
  path: test/library_checker/math/primitive_root.py
  requiredBy: []
  timestamp: '2024-06-12 17:23:04+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: test/library_checker/math/primitive_root.py
layout: document
redirect_from:
- /library/test/library_checker/math/primitive_root.py
- /library/test/library_checker/math/primitive_root.py.html
title: test/library_checker/math/primitive_root.py
---
