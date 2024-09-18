---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: data_structure/basic/SortedSet.py
    title: SortedSet
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/past/past6m.test.py
    title: "M - \u7B49\u3057\u3044\u6570"
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from data_structure.basic.SortedSet import SortedSet\n\n\nclass IntervalManager:\n\
    \    class Node:\n        def __init__(self, l: int, r: int, x: int):\n      \
    \      self.l = l\n            self.r = r\n            self.x = x\n\n        def\
    \ __lt__(self, other):\n            if self.l == other.l:\n                return\
    \ self.r < other.r\n            return self.l < other.l\n\n        def __le__(self,\
    \ other):\n            if self.l == other.l:\n                return self.r <=\
    \ other.r\n            else:\n                return self.l <= other.l\n\n   \
    \     def __ge__(self, other):\n            return not self.__lt__(other)\n\n\
    \        def __repr__(self):\n            return \"[{0},{1})-{2}\".format(self.l,\
    \ self.r, self.x)\n\n    inf = 10**9 + 1\n\n    def __init__(self, arr: list[int],\
    \ add, remove):\n        setter = []\n        n = len(arr)\n        l = 0\n  \
    \      while l < n:\n            r = l\n            while r < n and arr[l] ==\
    \ arr[r]:\n                r += 1\n            setter.append(self.Node(l, r, arr[l]))\n\
    \            add(l, r, arr[l])\n            l = r\n        self.s = SortedSet(setter)\n\
    \        self._add = add\n        self._remove = remove\n\n    def _getNode(self,\
    \ m: int):\n        z = self.s.le(self.Node(m, self.inf, None))\n        if z\
    \ is not None and z.l <= m < z.r:\n            return z\n        return None\n\
    \n    def update(self, l: int, r: int, x: int):\n        s = self.s\n        it\
    \ = s.ge(self.Node(l, 0, x))\n        while it != None and it.l <= r:\n      \
    \      if it.l == r:\n                if it.x == x:\n                    self._remove(r,\
    \ it.r, x)\n                    r = it.r\n                    _, it = s.discard(it),\
    \ s.ge(it)\n                break\n            if it.r <= r:\n               \
    \ self._remove(it.l, it.r, it.x)\n                _, it = s.discard(it), s.ge(it)\n\
    \            else:\n                if it.x == x:\n                    r = it.r\n\
    \                    self._remove(it.l, it.r, it.x)\n                    _, it\
    \ = s.discard(it), s.ge(it)\n                else:\n                    self._remove(it.l,\
    \ r, it.x)\n                    z = self.Node(r, it.r, it.x)\n               \
    \     s.discard(it)\n                    s.add(z)\n                    it = z\n\
    \        idx = s.index(it) if it != None else len(s)\n        if idx:\n      \
    \      it = s[idx - 1]\n            if it.r == l:\n                if it.x ==\
    \ x:\n                    self._remove(it.l, it.r, it.x)\n                   \
    \ l = it.l\n                    _, it = s.discard(it), s.ge(it)\n            elif\
    \ l < it.r:\n                if it.x == x:\n                    self._remove(it.l,\
    \ it.r, it.x)\n                    if it.l < l:\n                        l = it.l\n\
    \                    if it.r > r:\n                        r = it.r\n        \
    \            _, it = s.discard(it), s.ge(it)\n                else:\n        \
    \            if r < it.r:\n                        s.add(self.Node(r, it.r, it.x))\n\
    \                    self._remove(l, min(r, it.r), it.x)\n                   \
    \ s.discard(it)\n                    z = self.Node(it.l, l, it.x)\n          \
    \          s.add(z)\n                    it = z\n        self._add(l, r, x)\n\
    \        s.add(self.Node(l, r, x))\n\n    def __repr__(self):\n        return\
    \ \"\".join(*self.s)\n"
  dependsOn:
  - data_structure/basic/SortedSet.py
  isVerificationFile: false
  path: data_structure/interval_manager.py
  requiredBy: []
  timestamp: '2024-06-24 17:00:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/past/past6m.test.py
documentation_of: data_structure/interval_manager.py
layout: document
redirect_from:
- /library/data_structure/interval_manager.py
- /library/data_structure/interval_manager.py.html
title: data_structure/interval_manager.py
---
