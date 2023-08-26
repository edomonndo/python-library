---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_A\n\
    \nfrom tree.diameter import diameter\n\nN = int(input())\nG = [[] for _ in range(N)]\n\
    for _ in range(N - 1):\n    a, b, c = map(int, input().split())\n    G[a].append((b,\
    \ c))\n    G[b].append((a, c))\n\ndiam = diameter(N, G)\nprint(diam)\n"
  dependsOn: []
  isVerificationFile: true
  path: test/aoj/grl_5_a_diameter.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl_5_a_diameter.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl_5_a_diameter.test.py
- /verify/test/aoj/grl_5_a_diameter.test.py.html
title: test/aoj/grl_5_a_diameter.test.py
---
