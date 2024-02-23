---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl_3_a_smallest_window1.test.py
    title: test/aoj/dsl_3_a_smallest_window1.test.py
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/deque_operate_all_composite.test.py
    title: test/library_checker/data_structure/deque_operate_all_composite.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
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
    \            stack1 = stack[: (n + 1) // 2]\n            stack2 = stack[(n + 1)\
    \ // 2 :][::-1]\n            for _ in range((n + 1) // 2):\n                self._pushtop(stack1.pop())\n\
    \            for _ in range(n // 2):\n                self._pushbottom(stack2.pop())\n\
    \        if not self.top:\n            return self.e\n        else:\n        \
    \    return self._poptop()\n\n    def pop(self):\n        if not self.bottom:\n\
    \            stack = []\n            while self.top:\n                x = self._poptop()\n\
    \                stack.append(x)\n            n = len(stack)\n            stack1\
    \ = stack[: n // 2]\n            stack2 = stack[n // 2 :][::-1]\n            for\
    \ _ in range((n + 1) // 2):\n                self._pushbottom(stack2.pop())\n\
    \            for _ in range(n // 2):\n                self._pushtop(stack1.pop())\n\
    \        if not self.bottom:\n            return self.e\n        else:\n     \
    \       return self._popbottom()\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/FoldableDeque.py
  requiredBy: []
  timestamp: '2023-08-07 21:41:31+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/deque_operate_all_composite.test.py
  - test/aoj/dsl_3_a_smallest_window1.test.py
documentation_of: data_structure/FoldableDeque.py
layout: document
title: Foldable Deque(DSWAG)
---

通常のDeeueに加えて，列全体の総積を$O(1)$で求められる．

`.push(item)`, `.pushleft(item)`, `.pop()`, `.popleft()`は通常のDequeと同様．
`.fold()`で総積を返す．総積に使用する関数と単位元は`op`,`e`で指定する．