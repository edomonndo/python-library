---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: atcoder/segtree.py
    title: atcoder/segtree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':grey_question:'
    path: test/atcoder/arc008d_segtree.test.py
    title: test/atcoder/arc008d_segtree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from atcoder.segtree import SegTree\nfrom typing import TypeVar, Callable\n\
    \nT = TypeVar(\"T\")\n\n\nclass CompressedSegtree:\n    def __init__(self, op:\
    \ Callable[[int, int], T], e: T, V: dict[int, T]):\n        self.V = V\n     \
    \   self.toIdx = {v: i for i, v in enumerate(sorted(set(V.keys())))}\n       \
    \ toV = list(self.toIdx.keys())\n        self.n = len(self.toIdx)\n        self.seg\
    \ = SegTree(op, e, [V[toV[i]] for i in range(self.n)])\n\n    def set(self, p:\
    \ int, x: T) -> None:\n        p = self.toIdx[p]\n        self.seg.set(p, x)\n\
    \n    __setitem__ = set\n\n    def get(self, p: int) -> T:\n        p = self.toIdx[p]\n\
    \        return self.seg.get(p)\n\n    __getitem__ = get\n\n    def prod(self,\
    \ l: int, r: int) -> None:\n        l, r = self.toIdx[l], self.toIdx[r]\n    \
    \    return self.seg(l, r)\n\n    def all_prod(self):\n        return self.seg.all_prod()\n"
  dependsOn:
  - atcoder/segtree.py
  isVerificationFile: false
  path: data_structure/compressed_segtree.py
  requiredBy: []
  timestamp: '2024-05-27 17:45:23+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith:
  - test/atcoder/arc008d_segtree.test.py
documentation_of: data_structure/compressed_segtree.py
layout: document
redirect_from:
- /library/data_structure/compressed_segtree.py
- /library/data_structure/compressed_segtree.py.html
title: data_structure/compressed_segtree.py
---
