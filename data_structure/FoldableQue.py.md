---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl_3_d_sliding_minimum_element_swag.test.py
    title: test/aoj/dsl_3_d_sliding_minimum_element_swag.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class FoldableQue:\n    def __init__(self, op, e):\n        self.op = op\n\
    \        self.e = e\n        self.top = []\n        self.bottom = []\n       \
    \ self.topfold = [e]\n        self.bottomfold = [e]\n\n    def _pushbottom(self,\
    \ x):\n        self.bottom.append(x)\n        self.bottomfold.append(self.op(self.bottomfold[-1],\
    \ x))\n\n    def _popbottom(self):\n        self.bottomfold.pop()\n        return\
    \ self.bottom.pop()\n\n    def _pushtop(self, x):\n        self.top.append(x)\n\
    \        self.topfold.append(self.op(x, self.topfold[-1]))\n\n    def _poptop(self):\n\
    \        self.topfold.pop()\n        return self.top.pop()\n\n    def push(self,\
    \ x):\n        self._pushbottom(x)\n\n    def fold(self):\n        return self.op(self.topfold[-1],\
    \ self.bottomfold[-1])\n\n    def pop(self):\n        if not self.top:\n     \
    \       while self.bottom:\n                x = self._popbottom()\n          \
    \      self._pushtop(x)\n        if not self.top:\n            return self.e\n\
    \        else:\n            return self._poptop()\n\n    def front(self):\n  \
    \      if not self.top:\n            while self.bottom:\n                x = self._popbottom()\n\
    \                self._pushtop(x)\n        return self.top[-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/FoldableQue.py
  requiredBy: []
  timestamp: '2023-08-07 21:41:31+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/dsl_3_d_sliding_minimum_element_swag.test.py
documentation_of: data_structure/FoldableQue.py
layout: document
title: Foldable Queue(SWAG)
---

通常のQueueに加えて，列全体の総積を$O(1)$で求められる．

`.push(item)`, `.pop()`, `.front()`は通常のQueueと同様．
`.fold()`で総積を返す．総積に使用する関数と単位元は`op`,`e`で指定する．