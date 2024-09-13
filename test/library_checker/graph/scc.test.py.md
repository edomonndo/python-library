---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/scc.py
    title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/scc
    links:
    - https://judge.yosupo.jp/problem/scc
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc\n\nfrom\
    \ graph.scc import SCC\n\nn, m = map(int, input().split())\nedges = [tuple(map(int,\
    \ input().split())) for _ in range(m)]\n\nscc = SCC(n)\nfor u, v in edges:\n \
    \   scc.add_edge(u, v)\nscc.build()\nnum = scc.count_components()\ncc = scc.get_mapping()\n\
    ans = [[] for _ in range(num)]\nfor i in range(n):\n    ans[cc[i]].append(i)\n\
    print(len(ans))\nfor group in ans:\n    print(len(group), *group)\n"
  dependsOn:
  - graph/scc.py
  isVerificationFile: true
  path: test/library_checker/graph/scc.test.py
  requiredBy: []
  timestamp: '2024-09-14 02:50:27+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/scc.test.py
layout: document
title: Strongly Connected Components
---

