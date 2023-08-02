---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/cartesian_tree.test.py
    title: test/library_checker/tree/cartesian_tree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def cartesian_tree(LIST: list) -> list:\n    n = len(LIST)\n    parent =\
    \ [-1] * n\n    stack = []\n    for i in range(n):\n        prv_i = -1\n     \
    \   while stack and LIST[i] < LIST[stack[-1]]:\n            prv_i = stack.pop()\n\
    \        if prv_i != -1:\n            parent[prv_i] = i\n        if stack:\n \
    \           parent[i] = stack[-1]\n        stack.append(i)\n    return parent\n"
  dependsOn: []
  isVerificationFile: false
  path: tree/cartesian_tree.py
  requiredBy: []
  timestamp: '2023-07-23 01:42:59+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/tree/cartesian_tree.test.py
documentation_of: tree/cartesian_tree.py
layout: document
title: Cartesian tree
---

未履修.