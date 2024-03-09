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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Node:\n    def __init__(self, val):\n        self.val = val\n     \
    \   self.next = None\n        self.prev = None\n\n\nclass DoublyLinkedList:\n\
    \    def __init__(self):\n        self.head = None\n        self.tail = None\n\
    \        self.length = 0\n\n    def append(self, val) -> None:\n        cur =\
    \ Node(val)\n        if not self.head:\n            self.head = cur\n        \
    \    self.tail = self.head\n        else:\n            self.tail.next = cur\n\
    \            cur.prev = self.tail\n            self.tail = cur\n        self.length\
    \ += 1\n\n    def pop(self) -> Node:\n        if not self.head:\n            raise\
    \ IndexError(\"pop from empty list\")\n        tail = self.tail\n        if self.length\
    \ == 1:\n            self.tail = None\n            self.head = None\n        else:\n\
    \            self.tail = tail.prev\n            self.tail.next = None\n      \
    \      tail.prev = None\n        self.length -= 1\n        return tail\n\n   \
    \ def popleft(self) -> Node:\n        if self.length == 0:\n            raise\
    \ IndexError(\"popleft from empty list\")\n        head = self.head\n        if\
    \ self.length == 1:\n            self.head = None\n            self.tail = None\n\
    \        else:\n            self.head = head.next\n        head.next = None\n\
    \        self.length -= 1\n        return head\n\n    def appendleft(self, val)\
    \ -> None:\n        cur = Node(val)\n        if self.length == 0:\n          \
    \  self.head = cur\n            self.tail = cur\n        else:\n            self.head.prev\
    \ = cur\n            cur.next = self.head\n            self.head = cur\n     \
    \   self.length += 1\n\n    def __getitem__(self, index) -> Node:\n        if\
    \ (index < 0) or (index > self.length):\n            raise IndexError\n      \
    \  halfOfLength = self.length // 2\n        if index <= halfOfLength:\n      \
    \      cnt = 0\n            cur = self.head\n            while cnt != index:\n\
    \                cur = cur.next\n                cnt = cnt + 1\n            return\
    \ cur\n        elif index > halfOfLength:\n            cnt = self.length - 1\n\
    \            cur = self.tail\n            while cnt != index:\n              \
    \  cur = cur.prev\n                cnt = cnt - 1\n            return cur\n\n \
    \   def __setitem__(self, index, val) -> None:\n        targetNode = self.get(index)\n\
    \        targetNode.val = val\n\n    def insert(self, index, val) -> None:\n \
    \       if (index < 0) or (index > self.length):\n            raise IndexError\n\
    \        if index == 0:\n            self.appendleft(val)\n        if index ==\
    \ self.length:\n            self.append(val)\n        pre = self.get(index - 1)\n\
    \        cur = Node(val)\n        nex = pre.next\n        pre.next = cur\n   \
    \     cur.prev = pre\n        nex.prev = cur\n        cur.next = nex\n       \
    \ self.length += 1\n\n    def remove(self, index) -> Node:\n        if (index\
    \ < 0) or (index >= self.length):\n            raise IndexError\n        if index\
    \ == 0:\n            self.popleft()\n        if index == self.length - 1:\n  \
    \          self.pop()\n        cur = self.get(index)\n        cur.prev.next =\
    \ cur.next\n        cur.next.prev = cur.prev\n        cur.next = None\n      \
    \  cur.prev = None\n        self.length -= 1\n        return cur\n\n    def reverse(self)\
    \ -> None:\n        node = self.head\n        self.head = self.tail\n        self.tail\
    \ = node\n        tmpPrev = None\n        tmpNext = None\n        while node:\n\
    \            tmpPrev = node.prev\n            tmpNext = node.next\n          \
    \  node.next = tmpPrev\n            node.prev = tmpNext\n            node = node.prev\n\
    \n    def tolist(self) -> None:\n        arr = []\n        cur = self.head\n \
    \       while cur is not None:\n            arr.append(cur.val)\n            cur\
    \ = cur.next\n        return arr\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/doubly_linked_list.py
  requiredBy: []
  timestamp: '2024-03-10 00:23:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/doubly_linked_list.py
layout: document
title: "\u53CC\u65B9\u5411\u9023\u7D50\u30EA\u30B9\u30C8"
---

