---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/line_add_get_min.test.py
    title: Line Add Get Min
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/segment_add_get_min.test.py
    title: Segment Add Get Min
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class LiChaoTree:\n    def __init__(self, points: list[int], inf: int = 1\
    \ << 60):\n        \"\"\"\u6700\u5C0F\u5024(\u6700\u5927\u5024)\u3092\u6C42\u3081\
    \u308B\u9802\u70B9\u96C6\u5408\"\"\"\n        xs = sorted(set(points)) if points\
    \ else [0]\n        self.n = n = len(xs)\n        self.inf = inf\n        self.sz\
    \ = sz = 2 << n.bit_length() if n & (n - 1) else n\n        sz2 = self.sz << 1\n\
    \        self.bl = [0] * sz2\n        self.br = [0] * sz2\n        self.dat =\
    \ [(0, inf)] * sz2\n        for i in range(n):\n            self.bl[sz + i] =\
    \ self.br[sz + i] = xs[i]\n        for i in range(n, self.sz):\n            self.bl[sz\
    \ + i] = self.br[sz + i] = xs[n - 1]\n        for i in range(sz - 1, 0, -1):\n\
    \            self.bl[i] = self.bl[i << 1]\n            self.br[i] = self.br[i\
    \ << 1 | 1]\n\n    def add_line(self, a: int, b: int, idx: int = 1) -> None:\n\
    \        \"\"\"ax+b\u306E\u76F4\u7DDA\u3092\u8FFD\u52A0\u3059\u308B\"\"\"\n  \
    \      bl, br, dat = self.bl, self.br, self.dat\n        while True:\n       \
    \     a2, b2 = dat[idx]\n            l, r = bl[idx], br[idx]\n            lv =\
    \ a2 * l + b2\n            rv = a2 * r + b2\n            nlv = a * l + b\n   \
    \         nrv = a * r + b\n            if (lv <= nlv) == (rv <= nrv):\n      \
    \          if nlv < lv:\n                    dat[idx] = (a, b)\n             \
    \   return\n            m = br[idx << 1]\n            mv = a2 * m + b2\n     \
    \       nmv = a * m + b\n            if nmv < mv:\n                dat[idx], (a,\
    \ b) = (a, b), dat[idx]\n                lv, nlv = nlv, lv\n            idx =\
    \ (idx << 1) if nlv < lv else (idx << 1 | 1)\n\n    def add_segment(self, a: int,\
    \ b: int, l: int, r: int, idx: int = 1) -> None:\n        \"\"\"\u7DDA\u5206ax+b(l<=x<=r)\u3092\
    \u8FFD\u52A0\u3059\u308B\"\"\"\n        L, R, bl, br, add_line = l, r, self.bl,\
    \ self.br, self.add_line\n        st = [idx]\n        while st:\n            idx\
    \ = st.pop()\n            l, r = bl[idx], br[idx]\n            if R < l or r <\
    \ L:\n                continue\n            if L <= l and r <= R:\n          \
    \      add_line(a, b, idx)\n                continue\n            st += [idx <<\
    \ 1 | 1, idx << 1]\n\n    def query(self, x: int) -> int:\n        \"\"\"\u5EA7\
    \u6A19x\u306B\u304A\u3051\u308B\u76F4\u7DDA\u7FA4\u306E\u6700\u5C0F\u5024\u3092\
    \u8FD4\u3059\"\"\"\n        idx = 1\n        a, b = self.dat[idx]\n        res\
    \ = a * x + b\n        while idx < self.sz:\n            idx <<= 1\n         \
    \   if x > self.br[idx]:\n                idx += 1\n            a, b = self.dat[idx]\n\
    \            res = min(res, a * x + b)\n        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/li_chao_tree.py
  requiredBy: []
  timestamp: '2024-06-05 09:56:18+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/segment_add_get_min.test.py
  - test/library_checker/data_structure/line_add_get_min.test.py
documentation_of: data_structure/li_chao_tree.py
layout: document
title: Li Chao Tree
---

直線集合に直線追加($ax+b$), 直線集合に対して$x$での最小値を求める．

### LCT = LiChaoTree(arr)

初期化．$arr$はクエリの配列(オフライン不可)．

### LCT.add_edge(a, b)

直線$ax+b$を追加する．

### LCT.query(x)

点$x$での最小値を求める．