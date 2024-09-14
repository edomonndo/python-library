---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: graph/scc.py
    title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3"
  - icon: ':heavy_check_mark:'
    path: graph/scc_incremental.py
    title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3(Incremental)"
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
  code: "from typing import Optional\n\n\nclass CSR:\n    def __init__(\n        self,\n\
    \        n: int = 0,\n        start: Optional[list[int]] = None,\n        elist:\
    \ Optional[list[int]] = None,\n    ):\n        self.n = n\n        self.start\
    \ = start\n        self.elist = elist\n\n    @staticmethod\n    def build(\n \
    \       n: int,\n        edges: list[tuple[int, int]],\n        directed: bool\
    \ = False,\n    ) -> \"CSR\":\n        start = [0] * (n + 1)\n        m = len(edges)\n\
    \        elist = [0] * (m if directed else m * 2)\n\n        for e in edges:\n\
    \            start[e[0] + 1] += 1\n            if not directed:\n            \
    \    start[e[1] + 1] += 1\n\n        for i in range(1, n + 1):\n            start[i]\
    \ += start[i - 1]\n\n        counter = start[:]\n        for e in edges:\n   \
    \         u, v = e[0], e[1]\n            elist[counter[u]] = v\n            counter[u]\
    \ += 1\n            if not directed:\n                elist[counter[v]] = u\n\
    \                counter[v] += 1\n        return CSR(n, start, elist)\n\n    def\
    \ __len__(self) -> int:\n        return self.n\n\n    def __getitem__(self, i:\
    \ int) -> list[int]:\n        return self.elist[self.start[i] : self.start[i +\
    \ 1]]\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/csr.py
  requiredBy:
  - graph/scc.py
  - graph/scc_incremental.py
  timestamp: '2024-09-14 02:50:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: graph/csr.py
layout: document
title: "CSR\u30B0\u30E9\u30D5(Compressed Spare Row)"
---

疎なグラフを省メモリで表現できる形式．

