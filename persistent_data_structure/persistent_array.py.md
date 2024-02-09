---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':x:'
    path: persistent_data_structure/persistent_union_find.py
    title: persistent_data_structure/persistent_union_find.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class PersistentArray:\n    \"\"\"64\u5206\u6728\"\"\"\n\n    def __init__(self,\
    \ n: int, init_val: int = 0, auto_update: bool = True):\n        self.n = n\n\
    \        self.auto_update = auto_update\n        self.data = []\n        self.children\
    \ = []\n        self.last = -1\n        self.depth = 0\n        self.offset =\
    \ 0\n        while n > 1:\n            n = (n + 64 - 1) // 64  # \u5207\u308A\u4E0A\
    \u3052\u9664\u7B97\n            self.offset += 64**self.depth\n            self.depth\
    \ += 1\n        self.roots = []\n        self._build([init_val] * self.n)\n\n\
    \    def _build(self, V):\n        assert len(V) == self.n\n        self.roots.append(0)\n\
    \        offset = 0\n        for d in range(self.depth):\n            for i in\
    \ range(offset, offset + 64**d):\n                self.data.append(None)\n   \
    \             self.children.append([0] * 64)\n                for j in range(64):\n\
    \                    self.children[i][j] = i * 64 + j + 1\n            offset\
    \ += 64**d\n        for i in range(offset, offset + 64 * self.depth):\n      \
    \      if i - self.offset < self.n:\n                self.data.append(V[i - self.offset])\n\
    \            else:\n                self.data.append(None)\n            self.children.append(None)\n\
    \        self._update()\n\n    def get(self, t: int, p):\n        assert -1 <=\
    \ t <= self.last\n        assert 0 <= p < self.n\n        v = self.roots[t + 1]\n\
    \        cur = p + self.offset\n        order = []\n        for _ in range(self.depth):\n\
    \            cur, r = divmod(cur - 1, 64)\n            order.append(r)\n     \
    \   for r in order[::-1]:\n            v = self.children[v][r]\n        return\
    \ self.data[v]\n\n    def set(self, t: int, p: int, x) -> int:\n        assert\
    \ -1 <= t <= self.last\n        assert 0 <= p < self.n\n        pv = self.roots[t\
    \ + 1]\n        nv = len(self.data)\n        self.roots[self.last + 1] = nv\n\
    \        cur = p + self.offset\n        order = []\n        for _ in range(self.depth):\n\
    \            cur, r = divmod(cur - 1, 64)\n            order.append(r)\n     \
    \   for r in order[::-1]:\n            self.data.append(None)\n            self.children.append(self.children[pv][:])\n\
    \            self.children[nv][r] = nv = len(self.data)\n            pv = self.children[pv][r]\n\
    \        self.data.append(x)\n        self.children.append(None)\n        if self.auto_update:\n\
    \            self.update()\n        return self.last\n\n    def update(self) ->\
    \ int:\n        self.roots.append(self.roots[-1])\n        self.last += 1\n  \
    \      return self.last\n"
  dependsOn: []
  isVerificationFile: false
  path: persistent_data_structure/persistent_array.py
  requiredBy:
  - persistent_data_structure/persistent_union_find.py
  timestamp: '2024-02-09 16:12:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: persistent_data_structure/persistent_array.py
layout: document
redirect_from:
- /library/persistent_data_structure/persistent_array.py
- /library/persistent_data_structure/persistent_array.py.html
title: persistent_data_structure/persistent_array.py
---
