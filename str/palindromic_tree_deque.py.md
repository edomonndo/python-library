---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: data_structure/basic/deque.py
    title: "Deque\uFF08\uFF0B\u30E9\u30F3\u30C0\u30E0\u30A2\u30AF\u30BB\u30B9\u30FB\
      \u5408\u8A08\uFF09"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/string/palindromes_in_deque.test.py
    title: test/library_checker/string/palindromes_in_deque.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from data_structure.basic.deque import Deque\n\n\nclass DequePalindromicTree:\n\
    \    def __init__(self, n: int, base: str = \"a\", word_size: int = 26):\n   \
    \     n += 2\n        self.n = n\n        self.offset = ord(base)\n        self.word_size\
    \ = word_size\n        self.to = [[0] * word_size for _ in range(n)]\n       \
    \ self.cnt = [0] * n\n        self.size = [0] * n\n        self.par = [0] * n\n\
    \        self.link = [0] * n\n        self.slink = [0] * n\n        self.link[0]\
    \ = self.slink[0] = 1\n        self.size[1] = -1\n        self.s = Deque(max_size=n)\n\
    \        self.states = Deque([0])\n        self.diffs = Deque()\n        self.sz\
    \ = 2\n        self.active = 0\n\n    def _get_link(self, v: int, c: int, back:\
    \ bool = True) -> int:\n        s, size, link, slink = self.s, self.size, self.link,\
    \ self.slink\n        while c != self._get(s, size[v] + 1, back):\n          \
    \  if c == self._get(s, size[link[v]] + 1, back):\n                v = link[v]\n\
    \            else:\n                v = slink[v]\n        return v\n\n    def\
    \ _make_to(self, last: int, c: int, back: bool = True) -> int:\n        to, link,\
    \ slink, par, size = self.to, self.link, self.slink, self.par, self.size\n   \
    \     last = self._get_link(last, c, back)\n        if not to[last][c]:\n    \
    \        u = to[self._get_link(link[last], c, back)][c]\n            sz = self.sz\n\
    \            link[sz] = u\n            par[sz] = last\n            size[sz] =\
    \ size[last] + 2\n            if size[sz] - size[u] == size[u] - size[link[u]]:\n\
    \                slink[sz] = slink[u]\n            else:\n                slink[sz]\
    \ = u\n            to[last][c] = sz\n            self.sz += 1\n        return\
    \ to[last][c]\n\n    def _get(self, d: Deque, idx: int, back: bool = True) ->\
    \ int:\n        if idx >= len(d):\n            return -1\n        if back:\n \
    \           idx = ~idx\n        return d[idx]\n\n    def _push(self, d: Deque,\
    \ c: int, back: bool = True):\n        if back:\n            d.append(c)\n   \
    \     else:\n            d.appendleft(c)\n\n    def _pop(self, d: Deque, back:\
    \ bool = True):\n        if back:\n            d.pop()\n        else:\n      \
    \      d.popleft()\n\n    def _add_letter(self, c: str, back: bool = True):\n\
    \        s, states, diffs, size = self.s, self.states, self.diffs, self.size\n\
    \        c = ord(c) - self.offset\n        self._push(s, c, back)\n        pre\
    \ = self._get(states, 0, back)\n        last = self._make_to(pre, c, back)\n \
    \       self.active += not (self.cnt[last])\n        self.cnt[last] += 1\n   \
    \     D = 2 + size[pre] - size[last]\n        while D + size[pre] <= size[last]:\n\
    \            self._pop(states, back)\n            if states:\n               \
    \ pre = self._get(states, 0, back)\n                D += self._get(diffs, 0, back)\n\
    \                self._pop(diffs, back)\n            else:\n                break\n\
    \        if states:\n            self._push(diffs, D, back)\n        self._push(states,\
    \ last, back)\n\n    def _pop_letter(self, back: bool = True):\n        cnt, link,\
    \ size, par = self.cnt, self.link, self.size, self.par\n        states, diffs\
    \ = self.states, self.diffs\n        last = self._get(states, 0, back)\n     \
    \   cnt[last] -= 1\n        self.active -= not (cnt[last])\n        self._pop(states,\
    \ back)\n        self._pop(self.s, back)\n        cands = [(link[last], size[last]\
    \ - size[link[last]]), (par[last], 0)]\n        for state, diff in cands:\n  \
    \          if not states:\n                states.append(state)\n            \
    \    diffs.append(diff)\n            else:\n                D = self._get(diffs,\
    \ 0, back) - diff\n                pre = self._get(states, 0, back)\n        \
    \        if D + size[state] > size[pre]:\n                    self._push(states,\
    \ state, back)\n                    self._pop(diffs, back)\n                 \
    \   self._push(diffs, D, back)\n                    self._push(diffs, diff, back)\n\
    \        self._pop(diffs, back)\n\n    def append(self, c: int):\n        # assert\
    \ 0 <= ord(c) - self.offset < self.word_size\n        self._add_letter(c, True)\n\
    \n    def appendleft(self, c: int):\n        # assert 0 <= ord(c) - self.offset\
    \ < self.word_size\n        self._add_letter(c, False)\n\n    def pop(self):\n\
    \        self._pop_letter(True)\n\n    def popleft(self):\n        self._pop_letter(False)\n\
    \n    def distinct(self):\n        return self.active\n\n    def max_prefix_size(self):\n\
    \        return self.size[self._get(self.states, 0, False)]\n\n    def max_suffix_size(self):\n\
    \        return self.size[self._get(self.states, 0, True)]\n"
  dependsOn:
  - data_structure/basic/deque.py
  isVerificationFile: false
  path: str/palindromic_tree_deque.py
  requiredBy: []
  timestamp: '2024-09-16 13:52:09+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/string/palindromes_in_deque.test.py
documentation_of: str/palindromic_tree_deque.py
layout: document
redirect_from:
- /library/str/palindromic_tree_deque.py
- /library/str/palindromic_tree_deque.py.html
title: str/palindromic_tree_deque.py
---
