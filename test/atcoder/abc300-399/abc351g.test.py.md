---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: tree/static_top_tree.py
    title: Static Top Tree
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/abc351/tasks/abc351_g
    links:
    - https://atcoder.jp/contests/abc351/tasks/abc351_g
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc351/tasks/abc351_g\n\
    \nfrom tree.static_top_tree import StaticTopTree\n\nmod = 998244353\n\n\ndef vertex(k):\n\
    \    return 1 << 30 | A[k]\n\n\ndef add_edge(d):\n    return d & mask\n\n\ndef\
    \ add_vertex(d, i):\n    return d << 30 | A[i]\n\n\ndef compress(p, c):\n    x,\
    \ y = p >> 30, p & mask\n    z, w = c >> 30, c & mask\n    return (x * z % mod)\
    \ << 30 | ((x * w + y) % mod)\n\n\ndef rake(l, r):\n    return l * r % mod\n\n\
    \nn, q = map(int, input().split())\nP = [int(x) - 1 for x in input().split()]\n\
    A = [int(x) for x in input().split()]\n\nchildren = [[] for _ in range(n)]\nfor\
    \ i, p in enumerate(P, 1):\n    children[p].append(i)\n\nmask = (1 << 30) - 1\n\
    T = StaticTopTree(vertex, add_edge, add_vertex, compress, rake, 1 << 30, 1, children)\n\
    \nfor _ in range(q):\n    v, x = map(int, input().split())\n    v -= 1\n    A[v]\
    \ = x\n    while v != -1:\n        T.update(v)\n        v = T.parent[v]\n    print(T.solve()\
    \ & mask)\n"
  dependsOn:
  - tree/static_top_tree.py
  isVerificationFile: true
  path: test/atcoder/abc300-399/abc351g.test.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/abc300-399/abc351g.test.py
layout: document
title: G - Hash on Tree
---
