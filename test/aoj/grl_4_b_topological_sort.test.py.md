---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    IGNORE: ''
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: IGNORE\n\nfrom graph.topological_sort import topological_sort\n\
    \nN, M = map(int, input().split())\nG = [[] for _ in range(N)]\ndeg = [0] * N\n\
    for _ in range(M):\n    u, v = map(int, input().split())\n    G[u].append(v)\n\
    \    deg[v] += 1\n\nans = topological_sort(N, G, deg)\nprint(*ans, sep=\"\\n\"\
    )\n"
  dependsOn: []
  isVerificationFile: true
  path: test/aoj/grl_4_b_topological_sort.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/aoj/grl_4_b_topological_sort.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl_4_b_topological_sort.test.py
- /verify/test/aoj/grl_4_b_topological_sort.test.py.html
title: test/aoj/grl_4_b_topological_sort.test.py
---