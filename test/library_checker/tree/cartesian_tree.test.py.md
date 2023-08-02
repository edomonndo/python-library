---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: tree/cartesian_tree.py
    title: Cartesian tree
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/cartesian_tree
    links:
    - https://judge.yosupo.jp/problem/cartesian_tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cartesian_tree\n\
    \nfrom tree.cartesian_tree import cartesian_tree\n\nN = int(input())\nA = list(map(int,\
    \ input().split()))\n\nparent = cartesian_tree(A)\n# \u6839\u306F$parent_r$ =\
    \ r\u3068\u3059\u308B\nprint(*[v if v != -1 else i for i, v in enumerate(parent)])\n"
  dependsOn:
  - tree/cartesian_tree.py
  isVerificationFile: true
  path: test/library_checker/tree/cartesian_tree.test.py
  requiredBy: []
  timestamp: '2023-08-01 14:51:05+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/tree/cartesian_tree.test.py
layout: document
redirect_from:
- /verify/test/library_checker/tree/cartesian_tree.test.py
- /verify/test/library_checker/tree/cartesian_tree.test.py.html
title: test/library_checker/tree/cartesian_tree.test.py
---
