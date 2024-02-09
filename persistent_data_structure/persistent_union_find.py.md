---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: persistent_data_structure/persistent_array.py
    title: persistent_data_structure/persistent_array.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library_checker/data_structure/persistent_unionfind2.test.py
    title: test/library_checker/data_structure/persistent_unionfind2.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from persistent_data_structure.persistent_array import PersistentArray\n\n\
    \nclass PersistentUnionFind:\n    def __init__(self, n: int):\n        self.n\
    \ = n\n        self.parent_or_size = PersistentArray(n, -1, False)\n\n    def\
    \ leader(self, t: int, a) -> int:\n        assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\"\
    .format(a, self.n)\n        cur = a\n        while True:\n            nxt = self.parent_or_size.get(t,\
    \ cur)\n            if nxt < 0:\n                return cur\n            cur =\
    \ nxt\n\n    def same(self, t: int, a: int, b: int) -> bool:\n        assert 0\
    \ <= a < self.n, \"0<=a<n,a={0},n={1}\".format(a, self.n)\n        assert 0 <=\
    \ b < self.n, \"0<=b<n,b={0},n={1}\".format(b, self.n)\n        return self.leader(t,\
    \ a) == self.leader(t, b)\n\n    def merge(self, t: int, a: int, b: int) -> int:\n\
    \        assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\".format(a, self.n)\n  \
    \      assert 0 <= b < self.n, \"0<=b<n,b={0},n={1}\".format(b, self.n)\n    \
    \    x = self.leader(t, a)\n        y = self.leader(t, b)\n        if x == y:\n\
    \            return x\n        px = self.parent_or_size.get(t, x)\n        py\
    \ = self.parent_or_size.get(t, y)\n        if -px < -py:\n            x, y = y,\
    \ x\n            px, py = py, px\n        self.parent_or_size.set(t, x, px + py)\n\
    \        self.parent_or_size.set(t, y, x)\n        return x\n\n    def update(self):\n\
    \        return self.parent_or_size.update()\n"
  dependsOn:
  - persistent_data_structure/persistent_array.py
  isVerificationFile: false
  path: persistent_data_structure/persistent_union_find.py
  requiredBy: []
  timestamp: '2024-02-09 17:45:13+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/library_checker/data_structure/persistent_unionfind2.test.py
documentation_of: persistent_data_structure/persistent_union_find.py
layout: document
redirect_from:
- /library/persistent_data_structure/persistent_union_find.py
- /library/persistent_data_structure/persistent_union_find.py.html
title: persistent_data_structure/persistent_union_find.py
---
