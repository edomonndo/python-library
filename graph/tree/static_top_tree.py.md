---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc300-399/abc351g.test.py
    title: G - Hash on Tree
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import TypeVar, Callable\n\nPath = TypeVar(\"Path\")\nPoint =\
    \ TypeVar(\"Point\")\n\n\nclass StaticTopTree:\n    def __init__(\n        self,\n\
    \        # \u9802\u70B9 v \u306E\u307F\u304B\u3089\u306A\u308B path cluster \u3092\
    \u751F\u6210\u3059\u308B.\n        vertex: Callable[[int], Path],\n        # path\
    \ cluster t \u306B virtual \u306A\u6839\u3092\u751F\u3084\u3057\u3066 point cluster\
    \ \u306B\u3059\u308B.\n        add_edge: Callable[[Path], Point],\n        # point\
    \ cluster t \u306E\u6839\u306B\u9802\u70B9 v \u3092\u4EE3\u5165\u3057\u3066 path\
    \ cluster \u306B\u3059\u308B.\n        add_vertex: Callable[[Path], Point],\n\
    \        # path cluster p,c (p \u304C\u6839\u306B\u8FD1\u3044\u5074\u306B\u3042\
    \u308B) \u3092\u30DE\u30FC\u30B8\u3059\u308B.\n        compress: Callable[[Path,\
    \ Path], Path],\n        # point cluster x,y \u3092\u30DE\u30FC\u30B8\u3059\u308B\
    .\n        rake: Callable[[Point, Point], Point],\n        e_path: Path,\n   \
    \     e_point: Point,\n        children: list[list[int]],\n    ):\n        \"\"\
    \"\n        vertex:0\n        add_edge:1\n        add_vertex:2\n        compress:3\n\
    \        rake:4\n        \"\"\"\n        self.vertex = vertex\n        self.add_edge\
    \ = add_edge\n        self.add_vertex = add_vertex\n        self.compress = compress\n\
    \        self.rake = rake\n\n        self.n = n = len(children)\n        self.children\
    \ = children\n        self.parent = [-1] * (4 * n)\n        self.L = [-1] * (4\
    \ * n)\n        self.R = [-1] * (4 * n)\n        self.add_buff = n\n        self.vtype\
    \ = [-1] * (4 * n)\n        self.stt_root = -1\n        self.path_cluster_val\
    \ = [e_path for _ in range(4 * n)]\n        self.point_cluster_val = [e_point\
    \ for _ in range(4 * n)]\n\n        self.__build()\n\n    def __calc_heavy_edge(self)\
    \ -> None:\n        n = self.n\n        children = self.children\n        st =\
    \ [0]\n        sz = [1] * n\n        while st:\n            v = st.pop()\n   \
    \         if v >= 0:\n                st.append(~v)\n                for nv in\
    \ children[v]:\n                    st.append(nv)\n            else:\n       \
    \         v = ~v\n                max_size = 0\n                for i in range(len(children[v])):\n\
    \                    nv = children[v][i]\n                    sz[v] += sz[nv]\n\
    \                    if sz[nv] > max_size:\n                        max_size =\
    \ sz[nv]\n                        children[v][0], children[v][i] = children[v][i],\
    \ children[v][0]\n\n    def __add_stt_vertex(self, vid: int, lid: int, rid: int,\
    \ vtype: int) -> int:\n        if vid == -1:\n            vid = self.add_buff\n\
    \            self.add_buff += 1\n        self.L[vid] = lid\n        self.R[vid]\
    \ = rid\n        self.vtype[vid] = vtype\n\n        if lid != -1:\n          \
    \  self.parent[lid] = vid\n        if rid != -1:\n            self.parent[rid]\
    \ = lid\n\n        return vid\n\n    def __merge(self, chs: list[int], vtype:\
    \ int) -> tuple[int, int]:\n        if len(chs) == 1:\n            return chs[0]\n\
    \n        sz_sum = sum(sz for _, sz in chs)\n        left_chs, right_chs = [],\
    \ []\n        for i, sz in chs:\n            if sz < sz_sum:\n               \
    \ left_chs.append((i, sz))\n            else:\n                right_chs.append((i,\
    \ sz))\n            sz_sum -= 2 * sz\n\n        i, si = self.__merge(left_chs,\
    \ vtype)\n        j, sj = self.__merge(right_chs, vtype)\n        return (self.__add_stt_vertex(-1,\
    \ i, j, vtype), si + sj)\n\n    def __compress(self, v: int) -> tuple[int, int]:\n\
    \        chs = [self.__add_vertex(v)]\n        children = self.children\n    \
    \    while children[v]:\n            v = children[v][0]\n            chs.append(self.__add_vertex(v))\n\
    \n        return self.__merge(chs, 3)\n\n    def __rake(self, v: int) -> tuple[int,\
    \ int]:\n        chs = [self.__add_edge(cv) for cv in self.children[v][1:]]\n\
    \        if len(chs) == 0:\n            return (-1, 0)\n        else:\n      \
    \      return self.__merge(chs, 4)\n\n    def __add_edge(self, v: int) -> tuple[int,\
    \ int]:\n        j, sj = self.__compress(v)\n        return (self.__add_stt_vertex(-1,\
    \ j, -1, 1), sj)\n\n    def __add_vertex(self, v) -> tuple[int, int]:\n      \
    \  j, sj = self.__rake(v)\n        if j == -1:\n            return (self.__add_stt_vertex(v,\
    \ j, -1, 0), sj + 1)\n        else:\n            return (self.__add_stt_vertex(v,\
    \ j, -1, 2), sj + 1)\n\n    def __build(self) -> None:\n        self.__calc_heavy_edge()\n\
    \        i, _ = self.__compress(0)\n        self.stt_root = i\n\n        L, R\
    \ = self.L, self.R\n        stack = [~i, i]\n        while stack:\n          \
    \  k = stack.pop()\n            if k < 0:\n                self.update(~k)\n \
    \               continue\n            l, r = L[k], R[k]\n            if l != -1:\n\
    \                stack += [~l, l]\n            if r != -1:\n                stack\
    \ += [~r, r]\n\n    def update(self, k: int) -> None:\n        t = self.vtype[k]\n\
    \        if t == 0:\n            self.path_cluster_val[k] = self.vertex(k)\n \
    \       elif t == 1:\n            self.point_cluster_val[k] = self.add_edge(self.path_cluster_val[self.L[k]])\n\
    \        elif t == 2:\n            self.path_cluster_val[k] = self.add_vertex(\n\
    \                self.point_cluster_val[self.L[k]], k\n            )\n       \
    \ elif t == 3:\n            self.path_cluster_val[k] = self.compress(\n      \
    \          self.path_cluster_val[self.L[k]], self.path_cluster_val[self.R[k]]\n\
    \            )\n        elif t:\n            self.point_cluster_val[k] = self.rake(\n\
    \                self.point_cluster_val[self.L[k]], self.point_cluster_val[self.R[k]]\n\
    \            )\n\n    def solve(self) -> Path:\n        return self.path_cluster_val[self.stt_root]\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/tree/static_top_tree.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc300-399/abc351g.test.py
documentation_of: graph/tree/static_top_tree.py
layout: document
title: Static Top Tree
---

頂点の１点更新と区間演算を木上で行う.
木を分解し，二分木状である二分木をマージしていくことで，深さが$O(logN)$で抑えられ,効率良く木DPを再計算できる．


[解説](https://atcoder.jp/contests/abc351/editorial/9868)