---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: data_structure/interval_manager.py
    title: data_structure/interval_manager.py
  - icon: ':heavy_check_mark:'
    path: geometory/manhattan_mst.py
    title: geometory/manhattan_mst.py
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
  code: "import math\nimport bisect\n\n\nclass SortedSet:\n    BUCKET_RATIO = 50\n\
    \    REBUILD_RATIO = 170\n\n    def _build(self, a=None) -> None:\n        \"\
    Evenly divide `a` into buckets.\"\n        if a is None:\n            a = list(self)\n\
    \        size = self.size = len(a)\n        bucket_size = int(math.ceil(math.sqrt(size\
    \ / self.BUCKET_RATIO)))\n        self.a = [\n            a[size * i // bucket_size\
    \ : size * (i + 1) // bucket_size]\n            for i in range(bucket_size)\n\
    \        ]\n\n    def __init__(self, a=None) -> None:\n        \"Make a new SortedSet\
    \ from iterable. / O(N) if sorted and unique / O(N log N)\"\n        a = list(a)\
    \ if a is not None else []\n        if not all(a[i] < a[i + 1] for i in range(len(a)\
    \ - 1)):\n            a = sorted(set(a))\n        self._build(a)\n\n    def __iter__(self):\n\
    \        for i in self.a:\n            for j in i:\n                yield j\n\n\
    \    def __reversed__(self):\n        for i in reversed(self.a):\n           \
    \ for j in reversed(i):\n                yield j\n\n    def __eq__(self, other)\
    \ -> bool:\n        return list(self) == list(other)\n\n    def __len__(self)\
    \ -> int:\n        return self.size\n\n    def __repr__(self) -> str:\n      \
    \  return \"SortedSet\" + str(self.a)\n\n    def __str__(self) -> str:\n     \
    \   s = str(list(self))\n        return \"{\" + s[1 : len(s) - 1] + \"}\"\n\n\
    \    def _position(self, x) -> tuple[list, int]:\n        \"Find the bucket and\
    \ position which x should be inserted. self must not be empty.\"\n        for\
    \ a in self.a:\n            if x <= a[-1]:\n                break\n        return\
    \ (a, bisect.bisect_left(a, x))\n\n    def __contains__(self, x) -> bool:\n  \
    \      if self.size == 0:\n            return False\n        a, i = self._position(x)\n\
    \        return i != len(a) and a[i] == x\n\n    def add(self, x) -> bool:\n \
    \       \"Add an element and return True if added. / O(\u221AN)\"\n        if\
    \ self.size == 0:\n            self.a = [[x]]\n            self.size = 1\n   \
    \         return True\n        a, i = self._position(x)\n        if i != len(a)\
    \ and a[i] == x:\n            return False\n        a.insert(i, x)\n        self.size\
    \ += 1\n        if len(a) > len(self.a) * self.REBUILD_RATIO:\n            self._build()\n\
    \        return True\n\n    def _pop(self, a: list, i: int):\n        ans = a.pop(i)\n\
    \        self.size -= 1\n        if not a:\n            self._build()\n      \
    \  return ans\n\n    def discard(self, x) -> bool:\n        \"Remove an element\
    \ and return True if removed. / O(\u221AN)\"\n        if self.size == 0:\n   \
    \         return False\n        a, i = self._position(x)\n        if i == len(a)\
    \ or a[i] != x:\n            return False\n        self._pop(a, i)\n        return\
    \ True\n\n    def lt(self, x):\n        \"Find the largest element < x, or None\
    \ if it doesn't exist.\"\n        for a in reversed(self.a):\n            if a[0]\
    \ < x:\n                return a[bisect.bisect_left(a, x) - 1]\n\n    def le(self,\
    \ x):\n        \"Find the largest element <= x, or None if it doesn't exist.\"\
    \n        for a in reversed(self.a):\n            if a[0] <= x:\n            \
    \    return a[bisect.bisect_right(a, x) - 1]\n\n    def gt(self, x):\n       \
    \ \"Find the smallest element > x, or None if it doesn't exist.\"\n        for\
    \ a in self.a:\n            if a[-1] > x:\n                return a[bisect.bisect_right(a,\
    \ x)]\n\n    def ge(self, x):\n        \"Find the smallest element >= x, or None\
    \ if it doesn't exist.\"\n        for a in self.a:\n            if a[-1] >= x:\n\
    \                return a[bisect.bisect_left(a, x)]\n\n    def __getitem__(self,\
    \ i: int):\n        \"Return the i-th element.\"\n        if i < 0:\n        \
    \    for a in reversed(self.a):\n                i += len(a)\n               \
    \ if i >= 0:\n                    return a[i]\n        else:\n            for\
    \ a in self.a:\n                if i < len(a):\n                    return a[i]\n\
    \                i -= len(a)\n        raise IndexError\n\n    def pop(self, i:\
    \ int = -1):\n        \"Pop and return the i-th element.\"\n        if i < 0:\n\
    \            for a in reversed(self.a):\n                i += len(a)\n       \
    \         if i >= 0:\n                    return self._pop(a, i)\n        else:\n\
    \            for a in self.a:\n                if i < len(a):\n              \
    \      return self._pop(a, i)\n                i -= len(a)\n        raise IndexError\n\
    \n    def index(self, x) -> int:\n        \"Count the number of elements < x.\"\
    \n        ans = 0\n        for a in self.a:\n            if a[-1] >= x:\n    \
    \            return ans + bisect.bisect_left(a, x)\n            ans += len(a)\n\
    \        return ans\n\n    def index_right(self, x) -> int:\n        \"Count the\
    \ number of elements <= x.\"\n        ans = 0\n        for a in self.a:\n    \
    \        if a[-1] > x:\n                return ans + bisect.bisect_right(a, x)\n\
    \            ans += len(a)\n        return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/basic/SortedSet.py
  requiredBy:
  - data_structure/interval_manager.py
  - geometory/manhattan_mst.py
  timestamp: '2024-05-21 07:51:26+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/basic/SortedSet.py
layout: document
redirect_from:
- /library/data_structure/basic/SortedSet.py
- /library/data_structure/basic/SortedSet.py.html
title: data_structure/basic/SortedSet.py
---
