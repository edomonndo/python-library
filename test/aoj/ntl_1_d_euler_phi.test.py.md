---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: math_/euler_phi.py
    title: "\u30AA\u30A4\u30E9\u30FC\u306E\u03C6\u95A2\u6570(\u30C8\u30FC\u30B7\u30A7\
      \u30F3\u30C8\u95A2\u6570)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_D
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_D


    from math_.euler_phi import euler_phi


    N = int(input())

    print(euler_phi(N))

    '
  dependsOn:
  - math_/euler_phi.py
  isVerificationFile: true
  path: test/aoj/ntl_1_d_euler_phi.test.py
  requiredBy: []
  timestamp: '2023-08-26 01:45:36+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/ntl_1_d_euler_phi.test.py
layout: document
redirect_from:
- /verify/test/aoj/ntl_1_d_euler_phi.test.py
- /verify/test/aoj/ntl_1_d_euler_phi.test.py.html
title: test/aoj/ntl_1_d_euler_phi.test.py
---
