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
  code: "class FixedSizeHeapQue:\n    def __init__(self, arr=None, max_size=10**8):\n\
    \        self.size = 0\n        self.heap = arr if arr is not None else []\n \
    \       self.max_size = max_size\n\n        if arr:\n            n = len(arr)\n\
    \            self.size = n\n            self.heapify()\n\n    def heapify(self):\n\
    \        \"\"\"Transform list into a heap, in-place, in O(len(x)) time.\"\"\"\n\
    \        for i in reversed(range(self.size // 2)):\n            self._siftup(i)\n\
    \n    def push(self, item):\n        \"\"\"Push item onto heap, maintaining the\
    \ heap invariant.\"\"\"\n        if self.size < self.max_size:\n            self.heap.append(item)\n\
    \            self.size += 1\n            self._siftdown(0, self.size - 1)\n  \
    \      else:\n            self._replace(item)\n\n    def pop(self):\n        \"\
    \"\"Pop the smallest item off the heap, maintaining the heap invariant.\"\"\"\n\
    \        lastelt = self.heap.pop()  # raises appropriate IndexError if heap is\
    \ empty\n        self.size -= 1\n        if self.heap:\n            returnitem\
    \ = self.heap[0]\n            self.heap[0] = lastelt\n            self._siftup(0)\n\
    \            return returnitem\n        return lastelt\n\n    def pushpop(self,\
    \ item):\n        \"\"\"Fast version of a heappush followed by a heappop.\"\"\"\
    \n        if self.heap and self.heap[0] < item:\n            item, self.heap[0]\
    \ = self.heap[0], item\n            self._siftup(0)\n        return item\n\n \
    \   def _replace(self, item):\n        \"\"\"Pop and return the current smallest\
    \ value, and add the new item.\n\n        This is more efficient than heappop()\
    \ followed by heappush(), and can be\n        more appropriate when using a fixed-size\
    \ heap.  Note that the value\n        returned may be larger than item!  That\
    \ constrains reasonable uses of\n        this routine unless written as part of\
    \ a conditional replacement:\n\n            if item > heap[0]:\n             \
    \   item = heapreplace(heap, item)\n        \"\"\"\n        returnitem = self.heap[0]\
    \  # raises appropriate IndexError if heap is empty\n        self.heap[0] = item\n\
    \        self._siftup(0)\n        return returnitem\n\n    def _siftup(self, pos):\n\
    \        endpos = self.size\n        startpos = pos\n        newitem = self.heap[pos]\n\
    \        childpos = 2 * pos + 1\n        while childpos < endpos:\n          \
    \  rightpos = childpos + 1\n            if rightpos < endpos and not self.heap[childpos]\
    \ < self.heap[rightpos]:\n                childpos = rightpos\n            self.heap[pos]\
    \ = self.heap[childpos]\n            pos = childpos\n            childpos = 2\
    \ * pos + 1\n        self.heap[pos] = newitem\n        self._siftdown(startpos,\
    \ pos)\n\n    def _siftdown(self, startpos, pos):\n        newitem = self.heap[pos]\n\
    \        while pos > startpos:\n            parentpos = (pos - 1) >> 1\n     \
    \       parent = self.heap[parentpos]\n            if newitem < parent:\n    \
    \            self.heap[pos] = parent\n                pos = parentpos\n      \
    \          continue\n            break\n        self.heap[pos] = newitem\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/FixedSizeHeapQue.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/FixedSizeHeapQue.py
layout: document
title: "\u5E45\u56FA\u5B9A\u30D2\u30FC\u30D7\u30AD\u30E5\u30FC"
---
