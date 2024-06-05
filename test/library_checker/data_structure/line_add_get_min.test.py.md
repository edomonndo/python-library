---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/li_chao_tree.py
    title: Li Chao Tree
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/line_add_get_min
    links:
    - https://judge.yosupo.jp/problem/line_add_get_min
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/line_add_get_min\n\
    \nfrom data_structure.li_chao_tree import LiChaoTree\n\nn, q = map(int, input().split())\n\
    lines = [tuple(map(int, input().split())) for _ in range(n)]\nqueries = []\nxs\
    \ = []\nfor _ in range(q):\n    t, *qu = map(int, input().split())\n    if t ==\
    \ 0:\n        a, b = qu\n        queries.append((a, b))\n    else:\n        x\
    \ = qu[0]\n        xs.append(x)\n        queries.append((None, x))\nLCT = LiChaoTree(xs)\n\
    for a, b in lines:\n    LCT.add_line(a, b)\nfor a, b in queries:\n    if a is\
    \ None:\n        print(LCT.query(b))\n    else:\n        LCT.add_line(a, b)\n"
  dependsOn:
  - data_structure/li_chao_tree.py
  isVerificationFile: true
  path: test/library_checker/data_structure/line_add_get_min.test.py
  requiredBy: []
  timestamp: '2024-06-05 09:56:18+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/line_add_get_min.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/line_add_get_min.test.py
- /verify/test/library_checker/data_structure/line_add_get_min.test.py.html
title: test/library_checker/data_structure/line_add_get_min.test.py
---
