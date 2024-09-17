---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/low_link.py
    title: graph/low_link.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/two_edge_connected_components
    links:
    - https://judge.yosupo.jp/problem/two_edge_connected_components
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_edge_connected_components\n\
    \nfrom graph.low_link import LowLink\n\nn, m = map(int, input().split())\ng =\
    \ [[] for _ in range(n)]\nfor _ in range(m):\n    u, v = map(int, input().split())\n\
    \    g[u].append(v)\n    g[v].append(u)\n\nL = LowLink(g)\ncomponents, _ = L.two_edge_connected_components()\n\
    groups = dict()\nfor i, ci in enumerate(components):\n    if ci in groups:\n \
    \       groups[ci].append(i)\n    else:\n        groups[ci] = [i]\n\nprint(len(groups))\n\
    ans = []\nfor group in groups.values():\n    tmp = [len(group)]\n    tmp += group\n\
    \    ans.append(\" \".join(map(str, tmp)))\nprint(*ans, sep=\"\\n\")\n"
  dependsOn:
  - graph/low_link.py
  isVerificationFile: true
  path: test/library_checker/graph/two_edge_connected_components.test.py
  requiredBy: []
  timestamp: '2024-07-22 09:16:58+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/two_edge_connected_components.test.py
layout: document
title: Two-Edge-Connected Components
---

