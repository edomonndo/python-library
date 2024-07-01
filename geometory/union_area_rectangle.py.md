---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: atcoder/lazysegtree.py
    title: atcoder/lazysegtree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl/dsl_4_a_union_of_rectangles_lst.test.py
    title: "DSL4A Union of Rectangles (\u9045\u5EF6\u30BB\u30B0\u6728)"
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/area_of_union_of_rectangles.test.py
    title: Area of Union of Rectangles
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from atcoder.lazysegtree import LazySegTree\n\nmask = (1 << 31) - 1\n\n\n\
    def op(x, y):\n    x0, x1 = x >> 31, x & mask\n    y0, y1 = y >> 31, y & mask\n\
    \    if x0 < y0:\n        return x\n    elif x0 > y0:\n        return y\n    else:\n\
    \        return (x0 << 31) + x1 + y1\n\n\ndef mapping(x, y):\n    y0, y1 = y >>\
    \ 31, y & mask\n    return ((y0 + x) << 31) + y1\n\n\ndef composition(x, y):\n\
    \    return x + y\n\n\ndef union_area(rectangles: list[tuple[int, int, int, int]]):\n\
    \    \"\"\"\n    Rectangle := [x1, y1, x2, y2], where (x1,y1) is top-left, (x2,y2)\
    \ is bottom-right of rectangle.\n    O(nlogn)\n    \"\"\"\n    A, X, Y = [], [],\
    \ []\n    for x1, y1, x2, y2 in rectangles:\n        X += [x1, x2]\n        Y\
    \ += [y1, y2]\n    X = list(set(X))\n    X.sort()\n    dX = {x: i for i, x in\
    \ enumerate(X)}\n    Y = list(set(Y))\n    Y.sort()\n    dY = {y: i for i, y in\
    \ enumerate(Y)}\n    L = [[] for _ in range(len(Y))]\n    R = [[] for _ in range(len(Y))]\n\
    \    for x1, y1, x2, y2 in rectangles:\n        x1, x2, y1, y2 = dX[x1], dX[x2],\
    \ dY[y1], dY[y2]\n        L[y1].append((x1, x2))\n        R[y2].append((x1, x2))\n\
    \n    v = [(X[i + 1] - X[i]) for i in range(len(X) - 1)]\n    lst = LazySegTree(op,\
    \ 1 << 61, mapping, composition, 0, v)\n    s = X[-1] - X[0]\n    res = 0\n  \
    \  for i in range(len(Y) - 1):\n        for l, r in L[i]:\n            lst.apply(l,\
    \ r, 1)\n        z = lst.all_prod()\n        z0, z1 = z >> 31, z & mask\n    \
    \    z = s - z1 if z0 == 0 else s\n        res += z * (Y[i + 1] - Y[i])\n    \
    \    for l, r in R[i + 1]:\n            lst.apply(l, r, -1)\n    return res\n"
  dependsOn:
  - atcoder/lazysegtree.py
  isVerificationFile: false
  path: geometory/union_area_rectangle.py
  requiredBy: []
  timestamp: '2024-06-05 17:57:14+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/dsl/dsl_4_a_union_of_rectangles_lst.test.py
  - test/library_checker/data_structure/area_of_union_of_rectangles.test.py
documentation_of: geometory/union_area_rectangle.py
layout: document
title: "\u9577\u65B9\u5F62\u306E\u548C\u96C6\u5408\u306E\u9762\u7A4D"
---
