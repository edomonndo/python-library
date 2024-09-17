---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl/dsl_3_a_smallest_window1.test.py
    title: DSL3A Tha Smallest Window I
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/deque_operate_all_composite.test.py
    title: Deque Operate All Composite
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class FoldableDeque:\n    def __init__(self, op, e):\n        self.op = op\n\
    \        self.e = e\n        self.top = []\n        self.bottom = []\n       \
    \ self.topfold = [e]\n        self.bottomfold = [e]\n\n    def _pushbottom(self,\
    \ x):\n        self.bottom.append(x)\n        self.bottomfold.append(self.op(self.bottomfold[-1],\
    \ x))\n\n    def _popbottom(self):\n        self.bottomfold.pop()\n        return\
    \ self.bottom.pop()\n\n    def _pushtop(self, x):\n        self.top.append(x)\n\
    \        self.topfold.append(self.op(x, self.topfold[-1]))\n\n    def _poptop(self):\n\
    \        self.topfold.pop()\n        return self.top.pop()\n\n    def push(self,\
    \ x):\n        self._pushbottom(x)\n\n    def pushleft(self, x):\n        self._pushtop(x)\n\
    \n    def fold(self):\n        return self.op(self.topfold[-1], self.bottomfold[-1])\n\
    \n    def popleft(self):\n        if not self.top:\n            stack = []\n \
    \           while self.bottom:\n                x = self._popbottom()\n      \
    \          stack.append(x)\n            n = len(stack)\n            stack = stack[::-1]\n\
    \            stack1 = stack[: (n + 1) >> 1]\n            stack2 = stack[(n + 1)\
    \ >> 1 :][::-1]\n            for _ in range((n + 1) >> 1):\n                self._pushtop(stack1.pop())\n\
    \            for _ in range(n >> 1):\n                self._pushbottom(stack2.pop())\n\
    \        if not self.top:\n            return self.e\n        else:\n        \
    \    return self._poptop()\n\n    def pop(self):\n        if not self.bottom:\n\
    \            stack = []\n            while self.top:\n                x = self._poptop()\n\
    \                stack.append(x)\n            n = len(stack)\n            stack1\
    \ = stack[: n >> 1]\n            stack2 = stack[n >> 1 :][::-1]\n            for\
    \ _ in range((n + 1) >> 1):\n                self._pushbottom(stack2.pop())\n\
    \            for _ in range(n >> 1):\n                self._pushtop(stack1.pop())\n\
    \        if not self.bottom:\n            return self.e\n        else:\n     \
    \       return self._popbottom()\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/basic/FoldableDeque.py
  requiredBy: []
  timestamp: '2024-06-13 11:50:32+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/deque_operate_all_composite.test.py
  - test/aoj/dsl/dsl_3_a_smallest_window1.test.py
documentation_of: data_structure/basic/FoldableDeque.py
layout: document
redirect_from:
- /library/data_structure/basic/FoldableDeque.py
- /library/data_structure/basic/FoldableDeque.py.html
title: data_structure/basic/FoldableDeque.py
---
