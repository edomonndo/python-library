---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/link_cut_tree.py
    title: data_structure/link_cut_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/dynamic_tree_vertex_add_path_sum
    links:
    - https://judge.yosupo.jp/problem/dynamic_tree_vertex_add_path_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/dynamic_tree_vertex_add_path_sum\n\
    from data_structure.link_cut_tree import LinkCutTree\n\nN, Q = map(int, input().split())\n\
    A = [int(x) for x in input().split()]\nT = LinkCutTree(lambda x, y: x + y, 0,\
    \ A)\n\nfor _ in range(N - 1):\n    u, v = map(int, input().split())\n    T.evert(u)\n\
    \    T.link(u, v)\n\nans = []\nfor i in range(Q):\n    t, *q = map(int, input().split())\n\
    \    if t == 0:\n        u, v, w, x = q\n        T.evert(u)\n        T.cut(v)\n\
    \        T.evert(w)\n        T.link(w, x)\n    elif t == 1:\n        p, x = q\n\
    \        T.add(p, x)\n    else:\n        u, v = q\n        ans.append(str(T.path_query(u,\
    \ v)))\nprint(*ans, sep=\"\\n\")\n"
  dependsOn:
  - data_structure/link_cut_tree.py
  isVerificationFile: true
  path: test/library_checker/data_structure/dynamic_tree_vertex_add_path_sum.test.py
  requiredBy: []
  timestamp: '2024-02-26 12:20:09+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/dynamic_tree_vertex_add_path_sum.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/dynamic_tree_vertex_add_path_sum.test.py
- /verify/test/library_checker/data_structure/dynamic_tree_vertex_add_path_sum.test.py.html
title: test/library_checker/data_structure/dynamic_tree_vertex_add_path_sum.test.py
---
