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
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from heapq import heapify, heappush, heappop\n\n\nclass Node:\n    def __init__(self,\
    \ val: int):\n        self.val = val\n        self.lt = None\n        self.rt\
    \ = None\n\n\nclass HuTucker:\n    inf = float(\"inf\")\n\n    @staticmethod\n\
    \    def meld(a: Node | None, b: Node | None) -> Node | None:\n        if a is\
    \ None:\n            return b\n        if b is None:\n            return a\n \
    \       if a.val > b.val:\n            a, b = b, a\n        a.rt = HuTucker.meld(a.rt,\
    \ b)\n        a.lt, a.rt = a.rt, a.lt\n        return a\n\n    @staticmethod\n\
    \    def top(a: Node) -> int:\n        return a.val\n\n    @staticmethod\n   \
    \ def pop(a: Node) -> Node:\n        return HuTucker.meld(a.lt, a.rt)\n\n    @staticmethod\n\
    \    def push(a: Node, x: int) -> Node:\n        b = Node(x)\n        return HuTucker.meld(a,\
    \ b)\n\n    @staticmethod\n    def solve(w: list[int]) -> int:\n        inf =\
    \ HuTucker.inf\n        meld, top, pop, push = HuTucker.meld, HuTucker.top, HuTucker.pop,\
    \ HuTucker.push\n        n = len(w)\n        lt = [0] * n\n        rt = [0] *\
    \ n\n        cost = [0] * (n - 1)\n        heap = [None for _ in range(n - 1)]\n\
    \        pq = []\n        for i in range(n - 1):\n            lt[i] = i - 1\n\
    \            rt[i] = i + 1\n            cost[i] = w[i] + w[i + 1]\n          \
    \  pq.append(cost[i] * n + i)\n        heapify(pq)\n        res = 0\n        for\
    \ _ in range(n - 1):\n            while True:\n                p = heappop(pq)\n\
    \                c, i = divmod(p, n)\n                if cost[i] == c and rt[i]\
    \ >= 0:\n                    break\n            ml = mr = False\n            if\
    \ heap[i] is not None and w[i] + heap[i].val == c:\n                heap[i] =\
    \ pop(heap[i])\n                ml = True\n            elif w[i] + w[rt[i]] ==\
    \ c:\n                ml = mr = True\n            else:\n                t = top(heap[i])\n\
    \                heap[i] = pop(heap[i])\n                if heap[i] is not None\
    \ and top(heap[i]) + t == c:\n                    heap[i] = pop(heap[i])\n   \
    \             else:\n                    mr = True\n            res += c\n   \
    \         heap[i] = push(heap[i], c)\n            if ml:\n                w[i]\
    \ = inf\n            if mr:\n                w[rt[i]] = inf\n            if ml\
    \ and i > 0:\n                j = lt[i]\n                heap[j] = meld(heap[i],\
    \ heap[j])\n                rt[j] = rt[i]\n                rt[i] = -1\n      \
    \          lt[rt[j]] = j\n                i = j\n            if mr and rt[i] +\
    \ 1 < n:\n                j = rt[i]\n                heap[i] = meld(heap[i], heap[j])\n\
    \                rt[i] = rt[j]\n                rt[j] = -1\n                lt[rt[i]]\
    \ = i\n            cost[i] = w[i] + w[rt[i]]\n            if heap[i] is not None:\n\
    \                t = top(heap[i])\n                heap[i] = pop(heap[i])\n  \
    \              cost[i] = min(cost[i], w[i] + t, w[rt[i]] + t)\n              \
    \  if heap[i] is not None:\n                    cost[i] = min(cost[i], top(heap[i])\
    \ + t)\n                heap[i] = push(heap[i], t)\n            heappush(pq, cost[i]\
    \ * n + i)\n        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/hu_tucker.py
  requiredBy: []
  timestamp: '2024-03-28 07:49:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/hu_tucker.py
layout: document
title: "\u6700\u9069\u4E8C\u5206\u63A2\u7D22\u6728(Hu-Tucker)"
---

$n$個の葉をもつ順序付き二分木の最小コストを求める.
コストは以下で定義する.

$$\displaystyle\sum^{n-1}_{i=0} {W_i} \times {depth_i}$$

$W_i$は葉の重み,$depth_i$は二分木における左から$i$個目の葉の深さを表す.

参考：https://atcoder.jp/contests/atc002/tasks/atc002_c