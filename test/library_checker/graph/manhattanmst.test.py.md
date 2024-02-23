---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/manhattanmst
    links:
    - https://judge.yosupo.jp/problem/manhattanmst
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/manhattanmst\n\
    \nfrom geometory.manhattan_mst import ManhattanMST\nfrom atcoder.dsu import DSU\n\
    \nn = int(input())\nps = [tuple(map(int, input().split())) for _ in range(n)]\n\
    \nmt = ManhattanMST()\nfor x, y in ps:\n    mt.add_point(x, y)\nmt.solve()\n\n\
    uf = DSU(n)\ntot = 0\nans = []\nfor w, x, y in mt.edges:\n    if uf.same(x, y):\n\
    \        continue\n    uf.merge(x, y)\n    tot += w\n    ans.append(f\"{x} {y}\"\
    )\nprint(tot)\nprint(*ans, sep=\"\\n\")\n"
  dependsOn: []
  isVerificationFile: true
  path: test/library_checker/graph/manhattanmst.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/manhattanmst.test.py
layout: document
redirect_from:
- /verify/test/library_checker/graph/manhattanmst.test.py
- /verify/test/library_checker/graph/manhattanmst.test.py.html
title: test/library_checker/graph/manhattanmst.test.py
---
