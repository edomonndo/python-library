---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/fenwick_tree/fenwick_tree.py
    title: "\u62BD\u8C61\u5316Fenwick Tree"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':grey_question:'
    path: test/atcoder/past17o.test.py
    title: test/atcoder/past17o.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent))\n\
    \n\nfrom data_structure.fenwick_tree.fenwick_tree import FenwickTree\nfrom typing\
    \ import TypeVar\n\nT = TypeVar(\"T\")\n\n\nclass Node:\n    def __init__(self,\
    \ key: int, value: T):\n        self.key = key\n        self.value = value\n\n\
    \    def __str__(self):\n        return f\"({self.key}, {self.value})\"\n\n  \
    \  __repr__ = __str__\n\n    def __iadd__(self, other: \"Node\") -> \"Node\":\n\
    \        return __class__(self.key + other.key, self.value + other.value)\n\n\
    \    def __isub__(self, other: \"Node\") -> \"Node\":\n        return __class__(self.key\
    \ - other.key, self.value - other.value)\n\n\nclass ValueRangeSum:\n\n    def\
    \ __init__(self, arr: list[T], max_value=200000):\n        self.n = len(arr)\n\
    \        self.src = arr[:]\n        dat = [[] for _ in range(2)]\n        self.tot\
    \ = [0, 0]\n        self.num = [0, 0]\n        for x in arr:\n            self.tot[x\
    \ >= 0] += abs(x)\n            self.num[x >= 0] += 1\n            dat[x >= 0].append(abs(x))\n\
    \        self.bit = [FenwickTree(max_value + 1, Node(0, 0)) for _ in range(2)]\n\
    \        for i in range(2):\n            for x in dat[i]:\n                self.bit[i].add(x,\
    \ Node(1, x))\n\n    def set(self, p: int, v: T) -> None:\n        \"\"\"A[p]\
    \ \u2190 v\"\"\"\n        c = self.src[p]\n        self.src[p] = v\n        ac,\
    \ av = abs(c), abs(v)\n        self.tot[c >= 0] -= ac\n        self.num[c >= 0]\
    \ -= 1\n        self.bit[c >= 0].add(ac, Node(-1, -ac))\n        self.tot[v >=\
    \ 0] += av\n        self.num[v >= 0] += 1\n        self.bit[v >= 0].add(av, Node(1,\
    \ av))\n\n    def add(self, p: int, v: T) -> None:\n        \"\"\"A[p] += v\"\"\
    \"\n        c = self.src[p]\n        self.set(p, c + v)\n\n    def sum_lt(self,\
    \ v: T) -> T:\n        \"\"\"Sum of A[i] where A[i] < v, 0 <= i < n\"\"\"\n  \
    \      if v >= 0:\n            return -self.tot[0] + self.bit[1].sum0(v).value\n\
    \        else:\n            return -self.tot[0] + self.bit[0].sum0(-v + 1).value\n\
    \n    def sum_le(self, v: T) -> T:\n        \"\"\"Sum of A[i] where A[i] <= v,\
    \ 0 <= i < n\"\"\"\n        return self.sum_lt(v + 1)\n\n    def sum_gt(self,\
    \ v: T) -> T:\n        \"\"\"Sum of A[i] where A[i] > v, 0 <= i < n\"\"\"\n  \
    \      if v >= 0:\n            return self.tot[1] - self.bit[1].sum0(v + 1).value\n\
    \        else:\n            return self.tot[1] - self.bit[0].sum0(-v).value\n\n\
    \    def sum_ge(self, v: T) -> T:\n        \"\"\"Sum of A[i] where A[i] >= v,\
    \ 0 <= i < n\"\"\"\n        return self.sum_gt(v - 1)\n\n    def sum_abs_from(self,\
    \ v: T) -> T:\n        \"\"\"Sum of abs(A[i] - v) where 0 <= i < n\"\"\"\n   \
    \     res = 0\n        if v >= 0:\n            node = self.bit[1].sum0(v)\n  \
    \          res += self.tot[1] - self.num[1] * v - 2 * (node.value - node.key *\
    \ v)\n            res += v * self.num[0] + self.tot[0]\n        else:\n      \
    \      node = self.bit[0].sum0(-v)\n            res += self.tot[0] + self.num[0]\
    \ * v - 2 * (node.value + node.key * v)\n            res += self.tot[1] - v *\
    \ self.num[1]\n        return res\n\n\nclass CompressedValueRangeSum:\n\n    def\
    \ __init__(self, arr: list[T], possible_values: set[T], possible_vs: set[T]):\n\
    \        self.src = arr[:]\n        candidates = possible_values | possible_vs\n\
    \        for v in possible_vs:\n            candidates.add(v + 1)\n          \
    \  candidates.add(v - 1)\n        self.to = {v: i for i, v in enumerate(sorted(candidates))}\n\
    \        dat = [[] for _ in range(2)]\n        self.tot = [0, 0]\n        self.num\
    \ = [0, 0]\n        for x in arr:\n            self.tot[x >= 0] += abs(x)\n  \
    \          self.num[x >= 0] += 1\n            dat[x >= 0].append(abs(x))\n   \
    \     self.bit = [FenwickTree(len(self.to) + 1, Node(0, 0)) for _ in range(2)]\n\
    \        for x in arr:\n            self.bit[x >= 0].add(self.to[x], Node(1, abs(x)))\n\
    \n    def set(self, p: int, v: T) -> None:\n        \"\"\"A[p] \u2190 v\"\"\"\n\
    \        c = self.src[p]\n        self.src[p] = v\n        ac, av = abs(c), abs(v)\n\
    \        self.tot[c >= 0] -= ac\n        self.num[c >= 0] -= 1\n        self.bit[c\
    \ >= 0].add(self.to[c], Node(-1, -ac))\n        self.tot[v >= 0] += av\n     \
    \   self.num[v >= 0] += 1\n        self.bit[v >= 0].add(self.to[v], Node(1, av))\n\
    \n    def add(self, p: int, v: T) -> None:\n        \"\"\"A[p] += v\"\"\"\n  \
    \      c = self.src[p]\n        self.set(p, c + v)\n\n    def sum_lt(self, v:\
    \ T) -> T:\n        \"\"\"Sum of A[i] where A[i] < v, 0 <= i < n\"\"\"\n     \
    \   if v >= 0:\n            return -self.tot[0] + self.bit[1].sum0(self.to[v]).value\n\
    \        else:\n            return -self.bit[0].sum0(self.to[v]).value\n\n   \
    \ def sum_le(self, v: T) -> T:\n        \"\"\"Sum of A[i] where A[i] <= v, 0 <=\
    \ i < n\"\"\"\n        return self.sum_lt(v + 1)\n\n    def sum_gt(self, v: T)\
    \ -> T:\n        \"\"\"Sum of A[i] where A[i] > v, 0 <= i < n\"\"\"\n        if\
    \ v >= 0:\n            return self.tot[1] - self.bit[1].sum0(self.to[v] + 1).value\n\
    \        else:\n            return self.tot[1] - self.tot[0] + self.bit[0].sum0(self.to[v]).value\n\
    \n    def sum_ge(self, v: T) -> T:\n        \"\"\"Sum of A[i] where A[i] >= v,\
    \ 0 <= i < n\"\"\"\n        return self.sum_gt(v - 1)\n\n    def sum_abs_from(self,\
    \ v: T) -> T:\n        \"\"\"Sum of abs(A[i] - v) where 0 <= i < n\"\"\"\n   \
    \     res = 0\n        if v >= 0:\n            node = self.bit[1].sum0(self.to[v])\
    \  # A[i] < v\n            res += self.tot[1] - self.num[1] * v - 2 * (node.value\
    \ - node.key * v)\n            res += v * self.num[0] + self.tot[0]\n        else:\n\
    \            node = self.bit[0].sum0(self.to[v])  # A[i] < v\n            res\
    \ += 2 * (node.key * v + node.value) - self.num[0] * v - self.tot[0]\n       \
    \     res += self.tot[1] - v * self.num[1]\n        return res\n"
  dependsOn:
  - data_structure/fenwick_tree/fenwick_tree.py
  isVerificationFile: false
  path: data_structure/fenwick_tree/value_range_sum.py
  requiredBy: []
  timestamp: '2024-06-19 13:18:51+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith:
  - test/atcoder/past17o.test.py
documentation_of: data_structure/fenwick_tree/value_range_sum.py
layout: document
redirect_from:
- /library/data_structure/fenwick_tree/value_range_sum.py
- /library/data_structure/fenwick_tree/value_range_sum.py.html
title: data_structure/fenwick_tree/value_range_sum.py
---
