---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/string/eertree_static.test.py
    title: Eertree
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class PalindromicTree:\n    def __init__(self, S: str, base: str = \"a\"\
    , word_size: int = 26):\n        offset = ord(base)\n        S = [ord(s) - offset\
    \ for s in S]\n        self.n = n = len(S) + 2\n\n        self._init_node(n, word_size)\n\
    \        self._update_node(0, -1, -1, 0, -1)\n        self._update_node(1, 0,\
    \ 0, 0, 0)\n\n        link, length, to = self.link, self.length, self.to\n\n \
    \       self.path = path = []\n        p = 0\n        sz = 2\n        for i, s\
    \ in enumerate(S):\n            path.append(p)\n            while p:\n       \
    \         j = i - 1 - length[p]\n                ok = j >= 0 and S[j] == s\n \
    \               if ok:\n                    break\n                p = link[p]\n\
    \n            if to[p][s] != -1:\n                p = to[p][s]\n             \
    \   continue\n\n            l = i - 1 - length[p]\n            r = i + 1\n   \
    \         to[p][s] = sz\n\n            if p == 0:\n                t = 1\n   \
    \         else:\n                while True:\n                    p = link[p]\n\
    \                    j = i - 1 - length[p]\n                    ok = j >= 0 and\
    \ S[j] == s\n                    if ok:\n                        break\n     \
    \           t = to[p][s]\n                assert t != -1\n            self._update_node(sz,\
    \ t, r - l, l, r)\n            p = sz\n            sz += 1\n        path.append(p)\n\
    \        self._shrink_node()\n        return\n\n    def _init_node(self, n: int,\
    \ word_size: int):\n        self.link = [None] * n\n        self.length = [None]\
    \ * n\n        self.pos = [None] * n\n        self.to = [[-1 for _ in range(word_size)]\
    \ for _ in range(n)]\n\n    def _update_node(self, idx: int, link: int, length:\
    \ int, l: int, r: int) -> None:\n        self.link[idx] = link\n        self.length[idx]\
    \ = length\n        self.pos[idx] = (l, r)\n\n    def _shrink_node(self) -> None:\n\
    \        while self.link[-1] is None:\n            # assert self.length[-1] is\
    \ None\n            # assert self.pos[-1] is None\n            self.link.pop()\n\
    \            self.length.pop()\n            self.pos.pop()\n            self.to.pop()\n\
    \        self.n = len(self.link)\n        return\n\n    def count(self) -> list[int]:\n\
    \        cnt = [0] * len(self.n)\n        for p in self.path:\n            cnt[p]\
    \ += 1\n        for i, x in enumerate(self.link[1:], 1):\n            cnt[x] +=\
    \ cnt[i]\n        return cnt[2:]\n\n    def solve(self) -> tuple[list[int], list[int],\
    \ list[int]]:\n        par = [-1] * self.n\n        for i, js in enumerate(self.to):\n\
    \            for j in js:\n                if j != -1:\n                    par[j]\
    \ = i - 1\n\n        suffix_link = [0] * self.n\n        for i, j in enumerate(self.link[2:]):\n\
    \            if j is not None:\n                suffix_link[i] = j - 1\n\n   \
    \     max_palindromic_suffix = [p - 1 for p in self.path[1:]]\n        return\
    \ par[2:], suffix_link[:-2], max_palindromic_suffix\n"
  dependsOn: []
  isVerificationFile: false
  path: str/palindromic_tree.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/string/eertree_static.test.py
documentation_of: str/palindromic_tree.py
layout: document
title: "\u56DE\u6587\u6728"
---

$S$の空でない回文部分文字列からなる集合$P$に対して，以下を求める

- `n`: $|P|$.
- `par`: 頂点$v (0 <= v < n)$に対し， その親の頂点番号. ただし，|str($v$)|$=2$ならば親は$0$, |str($v$)|$=1$ならば，親は$-1$と定義する．
- `suffix_link`: 頂点$v (0 <= v < n)$に対し， $v$からのsuffix linkの行き先$s_v$ (str($v$)の空でない接尾辞回文のうち，str($v$)より短いもののうち最大のものに対応する頂点). ただし，そのような接尾辞回文が存在しない場合には$s_v = 0$と定義する．
- `max_palindromic_suffix`: $S$の長さ$i$の接尾辞$S_0 ⋯ S_{i-1}$の最大回文接尾辞に対する頂点番号$v_i$.

https://math314.hateblo.jp/entry/2016/12/19/005919