---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/scc
    links:
    - https://judge.yosupo.jp/problem/scc
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc\n\nfrom\
    \ graph.scc import scc\n\nN, M = map(int, input().split())\nedges = [None] * M\n\
    for i in range(M):\n    edges[i] = tuple(map(int, input().split()))\n\ngroups\
    \ = scc(N, M, edges)\nprint(len(groups))\nfor group in groups:\n    print(len(group),\
    \ *group)\n"
  dependsOn: []
  isVerificationFile: true
  path: test/library_checker/graph/scc.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/graph/scc.test.py
layout: document
redirect_from:
- /verify/test/library_checker/graph/scc.test.py
- /verify/test/library_checker/graph/scc.test.py.html
title: test/library_checker/graph/scc.test.py
---
