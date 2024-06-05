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
    PROBLEM: https://judge.yosupo.jp/problem/segment_add_get_min
    links:
    - https://judge.yosupo.jp/problem/segment_add_get_min
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/segment_add_get_min\n\
    \nfrom data_structure.li_chao_tree import LiChaoTree\n\nn, q = map(int, input().split())\n\
    lines = [tuple(map(int, input().split())) for _ in range(n)]\nqs = []\ninf = 1\
    \ << 60\nxs = []\nfor _ in range(q):\n    t, *qu = map(int, input().split())\n\
    \    if t == 0:\n        l, r, a, b = qu\n        qs.append((0, a, b, l, r))\n\
    \    else:\n        x = qu[0]\n        xs.append(x)\n        qs.append((1, x))\n\
    \nLCT = LiChaoTree(xs, inf)\nfor l, r, a, b in lines:\n    LCT.add_segment(a,\
    \ b, l, r - 1)\nfor i in range(q):\n    if qs[i][0] == 0:\n        _, a, b, l,\
    \ r = qs[i]\n        LCT.add_segment(a, b, l, r - 1)\n    else:\n        x = qs[i][1]\n\
    \        res = LCT.query(x)\n        if res == inf:\n            print(\"INFINITY\"\
    )\n        else:\n            print(res)\n"
  dependsOn:
  - data_structure/li_chao_tree.py
  isVerificationFile: true
  path: test/library_checker/data_structure/segment_add_get_min.test.py
  requiredBy: []
  timestamp: '2024-06-05 09:56:18+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/segment_add_get_min.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/segment_add_get_min.test.py
- /verify/test/library_checker/data_structure/segment_add_get_min.test.py.html
title: test/library_checker/data_structure/segment_add_get_min.test.py
---
