---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/basic/point.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u70B9)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from geometory.basic.point import Point\n\n\nimport sys\n\nsys.setrecursionlimit(1_000_000)\n\
    \n\nclass LeftHull:\n    class Node:\n        def __init__(self, bl: int, br:\
    \ int, L: int, R: int, lchd: int, rchd: int):\n            self.bl, self.br =\
    \ bl, br\n            self.L, self.R = L, R\n            self.lchd, self.rchd\
    \ = lchd, rchd\n\n    def __init__(self, ps: list[Point]):\n        self.ps =\
    \ ps\n        self.nodes = [self.Node(0, 0, 0, 0, 0, 0) for _ in range(len(ps)\
    \ << 1)]\n        self.root = 0\n        self._build(0, 0, len(ps))\n\n    def\
    \ _is_leaf(self, idx: int) -> bool:\n        node = self.nodes[idx]\n        return\
    \ node.lchd == node.rchd == -1\n\n    @staticmethod\n    def _cross3(a: Point,\
    \ b: Point, c: Point) -> int:\n        return (b - a).cross(c - a)\n\n    def\
    \ _pull(self, idx: int) -> None:\n        # assert not self._is_leaf(idx)\n  \
    \      nodes, ps = self.nodes, self.ps\n        l, r = nodes[idx].lchd, nodes[idx].rchd\n\
    \        split_y = ps[nodes[r].L].y\n        while not self._is_leaf(l) or not\
    \ self._is_leaf(r):\n            a, b = nodes[l].bl, nodes[l].br\n           \
    \ c, d = nodes[r].bl, nodes[r].br\n            if a != b and self._cross3(ps[a],\
    \ ps[b], ps[c]) > 0:\n                l = nodes[l].lchd\n            elif c !=\
    \ d and self._cross3(ps[b], ps[c], ps[d]) > 0:\n                r = nodes[r].rchd\n\
    \            elif a == b:\n                r = nodes[r].lchd\n            elif\
    \ c == d:\n                l = nodes[l].rchd\n            else:\n            \
    \    s1 = self._cross3(ps[a], ps[b], ps[c])\n                s2 = self._cross3(ps[b],\
    \ ps[a], ps[d])\n                # assert s1 + s2 >= 0\n                if s1\
    \ + s2 == 0 or s1 * ps[d].y + s2 * ps[c].y < split_y * (s1 + s2):\n          \
    \          l = nodes[l].rchd\n                else:\n                    r = nodes[r].lchd\n\
    \n        nodes[idx].bl = nodes[l].L\n        nodes[idx].br = nodes[r].L\n   \
    \     return\n\n    def _build(self, idx: int, L: int, R: int) -> None:\n    \
    \    node = self.nodes[idx]\n        node.L = L\n        node.R = R\n        if\
    \ R - L == 1:\n            node.lchd = node.rchd = -1\n            node.bl = node.br\
    \ = L\n        else:\n            M = (L + R) // 2\n            node.lchd = idx\
    \ + 1\n            node.rchd = idx + 2 * (M - L)\n            self._build(node.lchd,\
    \ L, M)\n            self._build(node.rchd, M, R)\n            self._pull(idx)\n\
    \        return\n\n    def _erase(self, idx: int, L: int, R: int) -> int:\n  \
    \      node = self.nodes[idx]\n        if R <= node.L or L > node.R:\n       \
    \     return idx\n        if L <= node.L and R >= node.R:\n            return\
    \ -1\n        node.lchd = self._erase(node.lchd, L, R)\n        node.rchd = self._erase(node.rchd,\
    \ L, R)\n        if node.lchd == -1:\n            return node.rchd\n        if\
    \ node.rchd == -1:\n            return node.lchd\n        self._pull(idx)\n  \
    \      return idx\n\n    def _get_hull(self, idx: int, l: int, r: int, res: list[int])\
    \ -> None:\n        node = self.nodes[idx]\n        if self._is_leaf(idx):\n \
    \           res.append(node.L)\n        elif r <= node.bl:\n            self._get_hull(node.lchd,\
    \ l, r, res)\n        elif l >= node.br:\n            self._get_hull(node.rchd,\
    \ l, r, res)\n        else:\n            # assert l <= node.bl and node.br <=\
    \ r\n            self._get_hull(node.lchd, l, node.bl, res)\n            self._get_hull(node.rchd,\
    \ node.br, r, res)\n        return\n\n    def get_hull(self) -> list[int]:\n \
    \       if self.root == -1:\n            return []\n        res = []\n       \
    \ self._get_hull(self.root, 0, len(self.ps) - 1, res)\n        return res\n\n\
    \    def erase(self, L: int) -> None:\n        self.root = self._erase(self.root,\
    \ L, L + 1)\n\n\nbs = 20\nmsk = (1 << bs) - 1\n\nn = int(input())\nps = [None]\
    \ * n\nidx = dict()\nfor i in range(n):\n    x, y = map(int, input().split())\n\
    \    ps[i] = Point(x, y)\n    idx[x << bs | y] = i\n\nps.sort(key=lambda p: (p.y,\
    \ p.x))\nleft = LeftHull(ps)\nqs = []\nfor i in range(n):\n    x, y = ps[i].x,\
    \ ps[i].y\n    qs.append(Point(-x, -y))\nqs.sort(key=lambda p: (p.y, p.x))\nright\
    \ = LeftHull(qs)\nl, cnt = 1, 0\nlayer = dict()\nwhile cnt < n:\n    hull = set()\n\
    \    for i in left.get_hull():\n        hull.add(i)\n    for i in right.get_hull():\n\
    \        hull.add(n - 1 - i)\n    for i in hull:\n        cnt += 1\n        layer[i]\
    \ = l\n        left.erase(i)\n        right.erase(n - 1 - i)\n    l += 1\n\nans\
    \ = [0] * n\nfor i, p in enumerate(ps):\n    ans[idx[p.x << bs | p.y]] = layer[i]\n\
    print(*ans, sep=\"\\n\")\n"
  dependsOn:
  - geometory/basic/point.py
  isVerificationFile: false
  path: geometory/convex_layer.py
  requiredBy: []
  timestamp: '2024-08-14 05:50:48+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: geometory/convex_layer.py
layout: document
redirect_from:
- /library/geometory/convex_layer.py
- /library/geometory/convex_layer.py.html
title: geometory/convex_layer.py
---
