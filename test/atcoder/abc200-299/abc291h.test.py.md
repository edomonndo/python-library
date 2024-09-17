---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: graph/tree/centroid_decomposition.py
    title: graph/tree/centroid_decomposition.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':grey_question:'
  attributes:
    IGNORE: https://atcoder.jp/contests/abc291/tasks/abc291_h
    links:
    - https://atcoder.jp/contests/abc291/tasks/abc291_h
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: IGNORE https://atcoder.jp/contests/abc291/tasks/abc291_h\n\
    \n\nfrom graph.tree.centroid_decomposition import CentroidDecomposition\n\nn =\
    \ int(input())\ng = [[] for _ in range(n)]\nfor _ in range(n - 1):\n    u, v =\
    \ map(lambda x: int(x) - 1, input().split())\n    g[u].append(v)\n    g[v].append(u)\n\
    \ntree = CentroidDecomposition(g)\nprint(*[v + 1 if v >= 0 else v for v in tree.belong])\n"
  dependsOn:
  - graph/tree/centroid_decomposition.py
  isVerificationFile: true
  path: test/atcoder/abc200-299/abc291h.test.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: TEST_IGNORED
  verifiedWith: []
documentation_of: test/atcoder/abc200-299/abc291h.test.py
layout: document
redirect_from:
- /verify/test/atcoder/abc200-299/abc291h.test.py
- /verify/test/atcoder/abc200-299/abc291h.test.py.html
title: test/atcoder/abc200-299/abc291h.test.py
---
