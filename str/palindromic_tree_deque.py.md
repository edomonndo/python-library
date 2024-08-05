---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: data_structure/basic/deque.py
    title: "Deque\uFF08\uFF0B\u30E9\u30F3\u30C0\u30E0\u30A2\u30AF\u30BB\u30B9\u30FB\
      \u5408\u8A08\uFF09"
  _extendedRequiredBy: []
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
  code: "from data_structure.basic.deque import Deque\n\n\nclass DequePalindromicTree:\n\
    \    class Node:\n        def __init__(self, par: int, link: int, length: int,\
    \ size: int):\n            self.par = par\n            self.link = link\n    \
    \        self.length = length\n            self.cnt = 0\n            self.link_cnt\
    \ = 0\n            self.to = [-1 for _ in range(size)]\n            self.direct_link\
    \ = [-1 for _ in range(size)]\n\n    def __init__(self, S: str, base: str = \"\
    a\", word_size: int = 26):\n        self.n = 0\n        self.offset = ord(base)\n\
    \        self.word_size = word_size\n        self.free = []\n        self.nodes\
    \ = []\n        self.nodes.append(self._new_node(-1, -1, -1))  # ODD\n       \
    \ self.nodes.append(self._new_node(-1, 0, 0))  # EVEN\n        inf = float(\"\
    inf\")\n        self.nodes[0].cnt = self.nodes[1].cnt = inf\n        mod = 4\n\
    \        while mod < word_size:\n            mod *= 2\n        self.mod = mod\n\
    \        self.msk = mod - 1\n        self.dat = [None] * (mod * 3)  # (c, left_surface,\
    \ right_surface)\n        self.L = self.R = 0\n\n    def _new_node(self, par:\
    \ int, link: int, length: int, c: int) -> int:\n        self.n += 1\n        node\
    \ = self.Node(par, link, length, self.word_size)\n        if link != -1:\n   \
    \         self.nodes[link].link_cnt + 1\n        p = 0\n        if len(self.free)\
    \ == 0:\n            p = len(self.nodes)\n            self.nodes.append(node)\n\
    \        else:\n            p = self.free.pop()\n            self.nodes[p] = node\n\
    \        if par != -1:\n            self.nodes[par].to[c] = p\n        return\
    \ p\n\n    def _remove_node(self, idx: int, c: int) -> None:\n        self.n -=\
    \ 1\n        pidx = self.nodes[idx].par\n        # assert self.nodes[pidx].to[c]\
    \ == idx\n        self.nodes[pidx].to[c] = -1\n        k = self.nodes[idx].link\n\
    \        self.nodes[k].link_cnt -= 1\n        if self.nodes[k].link_cnt == 0:\n\
    \            self.free.append(idx)\n        return\n\n    def _suffix_node(self):\n\
    \        if self.L == self.R:\n            return self.nodes[1]\n        return\
    \ self.dat[((self.R - 1) & self.msk) * 3 + 1]\n\n    def _prefix_node(self):\n\
    \        if self.L == self.R:\n            return self.nodes[1]\n        return\
    \ self.dat[(self.L & self.msk) * 3 + 2]\n\n    def append(self, c: str):\n   \
    \     # assert len(c) == 1\n        c = ord(c) - self.offset\n        # assert\
    \ 0 <= c < self.word_size\n        v = self._suffix_node()\n        self.dat[(self.R\
    \ & self.msk) * 3] = c\n\n        def dfs(v: int) -> int:\n            w = self.nodes[v].direct_link[c]\n\
    \            if w != -1:\n                return w\n            p = self.nodes[v].link\n\
    \            j = self.R - 1 - self.nodes[p].length\n            if self.L <= j\
    \ and j <= self.R and self.dat[(j & self.msk) * 3] == c:\n                self.nodes[v].direct_link[c]\
    \ = p\n                return p\n            w = dfs(p)\n            self.nodes[v].direct_link[c]\
    \ = w\n            return w\n\n        j = self.R - 1 - self.nodes[v].length\n\
    \        if not (self.L <= j and j <= self.R and self.dat[(j & self.msk) * 3]\
    \ == c):\n            v = dfs(v)\n        if self.nodes[v].to[c] != -1:\n    \
    \        v = self.nodes[v].to[c]\n        else:\n            link = self.nodes[1]\
    \ if v == self.nodes[0] else self.nodes[dfs(v)].to[c]\n            v = self._new_node(v,\
    \ link, self.nodes[v].length + 2, c)\n\n\nq = int(input())\nPT = DequePalindromicTree(\"\
    a\", 26)\nfor _ in range(q):\n    t, *qu = input().split()\n    if t == \"0\"\
    :\n        PT.appendleft(qu[0])\n    elif t == \"1\":\n        PT.append(qu[0])\n\
    \    elif t == \"2\":\n        PT.popleft()\n    elif t == \"3\":\n        PT.pop()\n\
    \    print(\n        PT.count_distinct_palindrome(),\n        PT.max_prefix_palindrome(),\n\
    \        PT.max_suffix_palindrome(),\n    )\n"
  dependsOn:
  - data_structure/basic/deque.py
  isVerificationFile: false
  path: str/palindromic_tree_deque.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: str/palindromic_tree_deque.py
layout: document
redirect_from:
- /library/str/palindromic_tree_deque.py
- /library/str/palindromic_tree_deque.py.html
title: str/palindromic_tree_deque.py
---
