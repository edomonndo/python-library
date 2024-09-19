---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/biconnected_components.py
    title: "\u4E8C\u9802\u70B9\u9023\u7D50\u6210\u5206\u5206\u89E3/Block Cut Tree"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/biconnected_components
    links:
    - https://judge.yosupo.jp/problem/biconnected_components
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/biconnected_components\n\
    \nfrom graph.biconnected_components import BiconnectedComponents\n\nn, m = map(int,\
    \ input().split())\nedges = [tuple(map(int, input().split())) for _ in range(m)]\n\
    BC = BiconnectedComponents(n, edges)\ngroups = BC.biconnected_components_verticle()\n\
    print(len(groups))\nfor group in groups:\n    print(len(group), *group)\n"
  dependsOn:
  - graph/biconnected_components.py
  isVerificationFile: true
  path: test/library_checker/graph/biconnected_components.test.py
  requiredBy: []
  timestamp: '2024-07-22 09:16:58+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/biconnected_components.test.py
layout: document
title: Biconnected Components
---

