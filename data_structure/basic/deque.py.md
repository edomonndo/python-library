---
data:
  _extendedDependsOn: []
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
  code: "class Deque:\n    def __init__(self, src_arr=None, max_size=300000):\n  \
    \      if src_arr is None:\n            src_arr = []\n        self.N = max(max_size,\
    \ len(src_arr)) + 1\n        self.buf = list(src_arr) + [None] * (self.N - len(src_arr))\n\
    \        self.head = 0\n        self.tail = len(src_arr)\n        # customize\n\
    \        self.sum = sum(src_arr)\n\n    def __index(self, i):\n        l = len(self)\n\
    \        if not -l <= i < l:\n            raise IndexError(\"index out of range:\
    \ \" + str(i))\n        if i < 0:\n            i += l\n        return (self.head\
    \ + i) % self.N\n\n    def __extend(self):\n        ex = self.N - 1\n        self.buf[self.tail\
    \ + 1 : self.tail + 1] = [None] * ex\n        self.N = len(self.buf)\n       \
    \ if self.head > 0:\n            self.head += ex\n\n    def is_full(self):\n \
    \       return len(self) >= self.N - 1\n\n    def is_empty(self):\n        return\
    \ len(self) == 0\n\n    def append(self, x):\n        if self.is_full():\n   \
    \         self.__extend()\n        self.buf[self.tail] = x\n        self.tail\
    \ += 1\n        self.tail %= self.N\n        # customize\n        self.sum +=\
    \ x\n\n    def appendleft(self, x):\n        if self.is_full():\n            self.__extend()\n\
    \        self.buf[(self.head - 1) % self.N] = x\n        self.head -= 1\n    \
    \    self.head %= self.N\n        # customize\n        self.sum += x\n\n    def\
    \ pop(self):\n        if self.is_empty():\n            raise IndexError(\"pop()\
    \ when buffer is empty\")\n        ret = self.buf[(self.tail - 1) % self.N]\n\
    \        self.tail -= 1\n        self.tail %= self.N\n        # customize\n  \
    \      self.sum -= ret\n        return ret\n\n    def popleft(self):\n       \
    \ if self.is_empty():\n            raise IndexError(\"popleft() when buffer is\
    \ empty\")\n        ret = self.buf[self.head]\n        self.head += 1\n      \
    \  self.head %= self.N\n        # customize\n        self.sum -= ret\n       \
    \ return ret\n\n    def __len__(self):\n        return (self.tail - self.head)\
    \ % self.N\n\n    def __getitem__(self, key):\n        return self.buf[self.__index(key)]\n\
    \n    def __setitem__(self, key, value):\n        self.buf[self.__index(key)]\
    \ = value\n\n    def __str__(self):\n        return \"Deque({0})\".format(str(list(self)))\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/basic/deque.py
  requiredBy: []
  timestamp: '2024-05-21 07:51:26+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/basic/deque.py
layout: document
title: "Deque\uFF08\uFF0B\u30E9\u30F3\u30C0\u30E0\u30A2\u30AF\u30BB\u30B9\u30FB\u5408\
  \u8A08\uFF09"
---

デフォルトのdequeのランダムアクセスが計算量$O(N)$であるのに対し,$O(1)$で可能.

また,キューに入った要素の合計も$O(1)$で取得できる.

使い方は通常のdequeと同様.

バッファを拡張する/確認する作業が相対的に重いため,`max_size`が抑えられるならば,`is_full()`を外し多少の高速化が可能.

### `Deque.appendleft(x)`,`Deque.append(x)`

キューの先頭/末尾に$x$を追加する.

### `Deque.popleft()`,`Deque.pop()`

キューの先頭/末尾から$x$を削除する.削除した値が返り値となる.

### `Deque.sum`

キューに入った要素の合計を$O(1)$で取得する.