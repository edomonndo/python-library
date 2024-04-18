---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/set_xor_min.test.py
    title: test/library_checker/data_structure/set_xor_min.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class BinaryTrie:\n    def __init__(self, max_query=5 * 10**5, max_log=30):\n\
    \        n = max_query * max_log\n        self.nodes = [0] * (2 * n)\n       \
    \ self.size = [0] * n\n        self.id = 0\n        self.max_log = max_log\n\n\
    \    def add(self, x):\n        v = 0\n        stack = [v]\n        for i in reversed(range(self.max_log)):\n\
    \            c = (x >> i) & 1\n            if self.nodes[2 * v + c] == 0:\n  \
    \              self.id += 1\n                self.nodes[2 * v + c] = self.id\n\
    \            v = self.nodes[2 * v + c]\n            stack.append(v)\n        if\
    \ self.size[v]:\n            return\n        for v in stack:\n            self.size[v]\
    \ += 1\n\n    def remove(self, x):\n        v = 0\n        stack = [v]\n     \
    \   for i in reversed(range(self.max_log)):\n            c = (x >> i) & 1\n  \
    \          if self.nodes[2 * v + c] == 0:\n                return\n          \
    \  v = self.nodes[2 * v + c]\n            stack.append(v)\n        while len(stack)\
    \ > 1:\n            if self.size[stack[-1]] > 1:\n                break\n    \
    \        v = stack.pop()\n            nv = stack[-1]\n            if self.nodes[2\
    \ * nv] == v:\n                self.nodes[2 * nv] = 0\n            else:\n   \
    \             self.nodes[2 * nv + 1] = 0\n        for v in stack:\n          \
    \  self.size[v] -= 1\n\n    def __contains__(self, item):\n        v = 0\n   \
    \     for i in reversed(range(self.max_log)):\n            c = (item >> i) & 1\n\
    \            if self.nodes[2 * v + c] == 0:\n                return False\n  \
    \          v = self.nodes[2 * v + c]\n        return True\n\n    def max(self):\n\
    \        v = 0\n        if self.size[v] == 0:\n            return -1\n       \
    \ res = 0\n        for i in reversed(range(self.max_log)):\n            if self.nodes[2\
    \ * v + 1] == 0:\n                v = self.nodes[2 * v]\n            else:\n \
    \               v = self.nodes[2 * v + 1]\n                res |= 1 << i\n   \
    \     return res\n\n    def min(self):\n        v = 0\n        if self.size[v]\
    \ == 0:\n            return -1\n        res = 0\n        for i in reversed(range(self.max_log)):\n\
    \            if self.nodes[2 * v] == 0:\n                v = self.nodes[2 * v\
    \ + 1]\n                res |= 1 << i\n            else:\n                v =\
    \ self.nodes[2 * v]\n        return res\n\n    def xor_max(self, x):\n       \
    \ v = 0\n        if self.size[v] == 0:\n            return -1\n        for i in\
    \ reversed(range(self.max_log)):\n            if self.nodes[2 * v + 1] == 0:\n\
    \                v = self.nodes[2 * v]\n                continue\n           \
    \ if self.nodes[v][0] == 0:\n                v = self.nodes[2 * v + 1]\n     \
    \           res |= 1 << i\n                continue\n            if (x >> i) &\
    \ 1:\n                v = self.nodes[2 * v]\n            else:\n             \
    \   v = self.nodes[2 * v + 1]\n                res |= 1 << i\n        return res\n\
    \n    def xor_min(self, x):\n        v = 0\n        if self.size[v] == 0:\n  \
    \          return -1\n        res = 0\n        for i in reversed(range(self.max_log)):\n\
    \            if self.nodes[2 * v] == 0:\n                v = self.nodes[2 * v\
    \ + 1]\n                res |= 1 << i\n                continue\n            if\
    \ self.nodes[2 * v + 1] == 0:\n                v = self.nodes[2 * v]\n       \
    \         continue\n            if (x >> i) & 1:\n                v = self.nodes[2\
    \ * v + 1]\n                res |= 1 << i\n            else:\n               \
    \ v = self.nodes[2 * v]\n        return res\n\n    def bisect_left(self, x):\n\
    \        v = 0\n        res = 0\n        for i in reversed(range(self.max_log)):\n\
    \            if (x >> i) & 1:\n                if self.nodes[2 * v + 1] == 0:\n\
    \                    return res + self.size[v]\n                res += self.size[self.nodes[2\
    \ * v]]\n                v = self.nodes[2 * v + 1]\n            else:\n      \
    \          if self.nodes[2 * v] == 0:\n                    return res\n      \
    \          v = self.nodes[2 * v]\n        return res\n\n    def bisect_right(self,\
    \ x):\n        return self.bisect_left(x + 1)\n\n    # \u5C0F\u3055\u3044\u307B\
    \u3046\u304B\u3089k\u756A\u76EE\u306E\u5024\u3092\u53D6\u5F97\n    def get_kth(self,\
    \ k):\n        v = 0\n        if self.size[v] <= k:\n            return -1\n \
    \       res = 0\n        for i in reversed(range(self.max_log)):\n           \
    \ if self.nodes[2 * v] == 0:\n                v = self.nodes[2 * v + 1]\n    \
    \            res |= 1 << i\n                continue\n            if self.nodes[2\
    \ * v + 1] == 0:\n                v = self.nodes[2 * v]\n                continue\n\
    \            if self.size[self.nodes[2 * v]] <= k:\n                k -= self.size[self.nodes[2\
    \ * v]]\n                v = self.nodes[2 * v + 1]\n                res |= 1 <<\
    \ i\n            else:\n                v = self.nodes[2 * v]\n        return\
    \ res\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/binary_trie.py
  requiredBy: []
  timestamp: '2024-02-09 16:12:14+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/set_xor_min.test.py
documentation_of: data_structure/binary_trie.py
layout: document
title: "\u30D0\u30A4\u30CA\u30EA\u30C8\u30E9\u30A4\u6728"
---
