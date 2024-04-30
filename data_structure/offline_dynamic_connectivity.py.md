---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/rollback_unionfind.py
    title: Rollback Union Find
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/dynamic_graph_vertex_add_component_sum.test.py
    title: test/library_checker/data_structure/dynamic_graph_vertex_add_component_sum.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Callable\nfrom collections import defaultdict\n\nfrom\
    \ data_structure.rollback_unionfind import RollbackUnionFind\n\n\nclass OfflineDynamicConnectivity:\n\
    \n    def __init__(self, n: int, q: int):\n        self.n = n\n        self.q\
    \ = q\n        self.bit = n.bit_length() + 1\n        self.msk = (1 << self.bit)\
    \ - 1\n        self.query_count = 0\n        self.log = (self.q - 1).bit_length()\n\
    \        self.size = 1 << self.log\n        self.data = [[] for _ in range(self.size\
    \ + self.size)]\n        self.edge = defaultdict(list)\n        self.uf = RollbackUnionFind(n)\n\
    \n    def add_value(self, u: int, w: int) -> None:\n        self.uf.add(u, w)\n\
    \n    def add_edge(self, u: int, v: int) -> None:\n        assert 0 <= u < self.n\
    \ and 0 <= v < self.n\n        if u > v:\n            u, v = v, u\n        self.edge[u\
    \ << self.bit | v].append(self.query_count << 1)\n        self.query_count +=\
    \ 1\n\n    def delete_edge(self, u: int, v: int) -> None:\n        assert 0 <=\
    \ u < self.n and 0 <= v < self.n\n        if u > v:\n            u, v = v, u\n\
    \        self.edge[u << self.bit | v].append(self.query_count << 1 | 1)\n    \
    \    self.query_count += 1\n\n    def add_relax(self) -> None:\n        self.query_count\
    \ += 1\n\n    def run(self, out: Callable[[int], None]) -> None:\n        # O(qlogqlogn)\n\
    \        assert (\n            self.query_count == self.q\n        ), f\"query_count=({self.query_count})\
    \ is not equal to q=({self.q})\"\n        data, uf, bit, msk, size, q = (\n  \
    \          self.data,\n            self.uf,\n            self.bit,\n         \
    \   self.msk,\n            self.size,\n            self.q,\n        )\n      \
    \  for k, v in self.edge.items():\n            LR = []\n            i = 0\n  \
    \          cnt = 0\n            while i < len(v):\n                if v[i] & 1\
    \ == 0:\n                    cnt += 1\n                if cnt > 0:\n         \
    \           LR.append(v[i] >> 1)\n                    i += 1\n               \
    \     while i < len(v) and cnt > 0:\n                        if v[i] & 1 == 0:\n\
    \                            cnt += 1\n                        else:\n       \
    \                     cnt -= 1\n                            if cnt == 0:\n   \
    \                             LR.append(v[i] >> 1)\n                        i\
    \ += 1\n                    i -= 1\n                i += 1\n            if cnt\
    \ > 0:\n                LR.append(q)\n            LR.reverse()\n            while\
    \ LR:\n                l = LR.pop() + size\n                r = LR.pop() + size\n\
    \                while l < r:\n                    if l & 1:\n               \
    \         data[l].append(k)\n                        l += 1\n                \
    \    if r & 1:\n                        data[r ^ 1].append(k)\n              \
    \      l >>= 1\n                    r >>= 1\n\n        todo = [1]\n        while\
    \ todo:\n            v = todo.pop()\n            if v >= 0:\n                for\
    \ uv in data[v]:\n                    uf.merge(uv >> bit, uv & msk)\n        \
    \        todo.append(~v)\n                if v << 1 | 1 < size + size:\n     \
    \               todo.append(v << 1 | 1)\n                    todo.append(v <<\
    \ 1)\n                elif v - size < q:\n                    out(v - size)\n\
    \            else:\n                for _ in data[~v]:\n                    uf.undo()\n\
    \n    def __repr__(self):\n        return f\"OfflineDynamicConnectivity({self.n},\
    \ {self.q})\"\n"
  dependsOn:
  - data_structure/rollback_unionfind.py
  isVerificationFile: false
  path: data_structure/offline_dynamic_connectivity.py
  requiredBy: []
  timestamp: '2024-04-30 11:25:39+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/dynamic_graph_vertex_add_component_sum.test.py
documentation_of: data_structure/offline_dynamic_connectivity.py
layout: document
redirect_from:
- /library/data_structure/offline_dynamic_connectivity.py
- /library/data_structure/offline_dynamic_connectivity.py.html
title: data_structure/offline_dynamic_connectivity.py
---