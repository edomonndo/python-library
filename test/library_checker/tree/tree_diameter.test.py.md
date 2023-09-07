---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/tree_diameter
    links:
    - https://judge.yosupo.jp/problem/tree_diameter
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/tree_diameter\n\
    \nfrom tree.diameter import diameter\n\nN = int(input())\nG = [[] for _ in range(N)]\n\
    for _ in range(N - 1):\n    a, b, c = map(int, input().split())\n    G[a].append((b,\
    \ c))\n    G[b].append((a, c))\n\ndiam, path = diameter(N, G, True)\nprint(diam,\
    \ len(path))\nprint(*path)\n"
  dependsOn: []
  isVerificationFile: true
  path: test/library_checker/tree/tree_diameter.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/tree/tree_diameter.test.py
layout: document
redirect_from:
- /verify/test/library_checker/tree/tree_diameter.test.py
- /verify/test/library_checker/tree/tree_diameter.test.py.html
title: test/library_checker/tree/tree_diameter.test.py
---
