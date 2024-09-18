---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/fenwick_tree/fenwick_tree.py
    title: "\u62BD\u8C61\u5316Fenwick Tree"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/point_add_rectangle_sum.test.py
    title: Point Add Rectangle Sum
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from bisect import bisect_left\n\nfrom data_structure.fenwick_tree.fenwick_tree\
    \ import FenwickTree\n\n\nclass OfflinePointAddRectangleSum:\n    def __init__(self):\n\
    \        self.qs = []\n        self.q_cnt = [0]\n\n    def add_point(self, x:\
    \ int, y: int, w: int) -> None:\n        self.qs.append((-1, x, y, w))\n     \
    \   self.q_cnt.append(self.q_cnt[-1])\n\n    def add_query(self, x1: int, y1:\
    \ int, x2: int, y2: int) -> None:\n        self.qs.append((self.q_cnt[-1], x1,\
    \ y1, x2, y2))\n        self.q_cnt.append(self.q_cnt[-1] + 1)\n\n    def solve(self)\
    \ -> list[int]:\n        res = [0] * self.q_cnt[-1]\n        stack = [(0, len(self.qs))]\n\
    \        while stack:\n            l, r = stack.pop()\n            if r - l <\
    \ 2:\n                continue\n            m = (l + r) >> 1\n            stack\
    \ += [(l, m), (m, r)]\n\n            l_point = (m - l) - (self.q_cnt[m] - self.q_cnt[l])\n\
    \            r_query = self.q_cnt[r] - self.q_cnt[m]\n\n            # \u72ED\u3044\
    \u5834\u5408\u306F\u611A\u76F4\n            if l_point * r_query < 200:\n    \
    \            tmp = [self.qs[i] for i in range(l, m) if self.qs[i][0] == -1]\n\
    \                for i in range(m, r):\n                    if self.qs[i][0] !=\
    \ -1:\n                        qi, x1, y1, x2, y2 = self.qs[i]\n             \
    \           for _, x, y, w in tmp:\n                            if x1 <= x < x2\
    \ and y1 <= y < y2:\n                                res[qi] += w\n          \
    \      continue\n\n            # add_point\u306B\u5BFE\u3057\u3066\uFF0Cy\u5EA7\
    \u6A19\u3067\u30BD\u30FC\u30C8&\u5EA7\u5727\n            toY, P = [], []\n   \
    \         for i in range(l, m):\n                if self.qs[i][0] == -1:\n   \
    \                 toY.append(self.qs[i][2])\n                    P.append(self.qs[i])\n\
    \            toY.sort()\n            for i in range(l_point):\n              \
    \  _, x, y, w = P[i]\n                y_ = bisect_left(toY, y)\n             \
    \   P[i] = (x, y_, w)\n\n            # \u30A4\u30D9\u30F3\u30C8\u30BD\u30FC\u30C8\
    \n            Q = []\n            for i in range(m, r):\n                if self.qs[i][0]\
    \ != -1:\n                    qi, x1, y1, x2, y2 = self.qs[i]\n              \
    \      y1_ = bisect_left(toY, y1)\n                    y2_ = bisect_left(toY,\
    \ y2)\n                    Q += [(~qi, x1, y1_, y2_), (qi, x2, y1_, y2_)]\n\n\
    \            # x\u5EA7\u6A19\u3067\u30BD\u30FC\u30C8\n            P.sort(key=lambda\
    \ p: p[0])\n            Q.sort(key=lambda q: q[1])\n\n            # \u5E73\u9762\
    \u8D70\u67FB\n            fw = FenwickTree(len(toY))\n            pi, qi = 0,\
    \ 0\n            while qi < len(Q):\n                if pi == len(P) or Q[qi][1]\
    \ <= P[pi][0]:\n                    i, x, y1, y2 = Q[qi]\n                   \
    \ s = fw.sum(y1, y2)\n                    if i < 0:\n                        res[~i]\
    \ -= s\n                    else:\n                        res[i] += s\n     \
    \               qi += 1\n                else:\n                    x, y, w =\
    \ P[pi]\n                    fw.add(y, w)\n                    pi += 1\n     \
    \   return res\n"
  dependsOn:
  - data_structure/fenwick_tree/fenwick_tree.py
  isVerificationFile: false
  path: geometory/offline_point_add_rectangle_sum.py
  requiredBy: []
  timestamp: '2024-08-14 05:50:48+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/point_add_rectangle_sum.test.py
documentation_of: geometory/offline_point_add_rectangle_sum.py
layout: document
redirect_from:
- /library/geometory/offline_point_add_rectangle_sum.py
- /library/geometory/offline_point_add_rectangle_sum.py.html
title: geometory/offline_point_add_rectangle_sum.py
---
