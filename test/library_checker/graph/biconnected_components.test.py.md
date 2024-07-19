---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: graph/low_link.py
    title: Low Link
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
    \nfrom graph.low_link import LowLink\n\nn, m = map(int, input().split())\ng =\
    \ [[] for _ in range(n)]\nfor _ in range(m):\n    u, v = map(int, input().split())\n\
    \    g[u].append(v)\n    g[v].append(u)\ngroups = LowLink.biconnected_components_verticle(g)\n\
    print(len(groups))\nfor group in groups:\n    print(len(group), *group)\n"
  dependsOn:
  - graph/low_link.py
  isVerificationFile: true
  path: test/library_checker/graph/biconnected_components.test.py
  requiredBy: []
  timestamp: '2024-07-19 12:35:18+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/biconnected_components.test.py
layout: document
title: Biconnected Components
---

