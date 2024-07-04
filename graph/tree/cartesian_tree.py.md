---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def cartesian_tree(LIST: list) -> list:\n    n = len(LIST)\n    parent =\
    \ [-1] * n\n    stack = []\n    for i in range(n):\n        prv_i = -1\n     \
    \   while stack and LIST[i] < LIST[stack[-1]]:\n            prv_i = stack.pop()\n\
    \        if prv_i != -1:\n            parent[prv_i] = i\n        if stack:\n \
    \           parent[i] = stack[-1]\n        stack.append(i)\n    return parent\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/tree/cartesian_tree.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: graph/tree/cartesian_tree.py
layout: document
title: Cartesian tree
---

未履修.