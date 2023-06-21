---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/cartesian_tree
    links:
    - https://judge.yosupo.jp/problem/cartesian_tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cartesian_tree\n\
    \n\ndef cartesian_tree(LIST: list) -> list:\n    n = len(LIST)\n    parent = [-1]\
    \ * n\n    stack = []\n    for i in range(n):\n        prv_i = -1\n        while\
    \ stack and LIST[i] < LIST[stack[-1]]:\n            prv_i = stack.pop()\n    \
    \    if prv_i != -1:\n            parent[prv_i] = i\n        if stack:\n     \
    \       parent[i] = stack[-1]\n        stack.append(i)\n    return parent\n\n\n\
    N = int(input())\nA = list(map(int, input().split()))\n\nparent = cartesian_tree(A)\n\
    # \u6839\u306F$parent_r$ = r\u3068\u3059\u308B\nprint(*[v if v != -1 else i for\
    \ i, v in enumerate(parent)])\n"
  dependsOn: []
  isVerificationFile: true
  path: library_checker/tree/cartesian_tree.test.py
  requiredBy: []
  timestamp: '2023-06-09 12:11:59+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: library_checker/tree/cartesian_tree.test.py
layout: document
redirect_from:
- /verify/library_checker/tree/cartesian_tree.test.py
- /verify/library_checker/tree/cartesian_tree.test.py.html
title: library_checker/tree/cartesian_tree.test.py
---
