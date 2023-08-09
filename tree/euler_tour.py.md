---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - "https://maspypy.com/euler-tour-\u306E\u304A\u52C9\u5F37"
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://maspypy.com/euler-tour-\u306E\u304A\u52C9\u5F37\n\n\nclass EulerTour:\n\
    \    def __init__(self, N, G, root, vcost):\n        self.N = N\n        self.ET\
    \ = []\n        self.into = [0] * N\n        self.out = [0] * N\n        # For\
    \ LCA\n        self.parent = [-1] * N\n        self.depth = []\n        # For\
    \ Path Query\n        self.vcost = []\n        self.ecost = []\n        # For\
    \ Range Sum Query\n        self.vcost_st = []\n        self.ecost_st = []\n\n\
    \        # \u975E\u518D\u5E30DFS\n        seen = [0] * N\n        idx = -1\n \
    \       depth = 0\n        stack = [(~root, -depth, 0), (root, depth, 0)]\n  \
    \      while stack:\n            v, depth, weight = stack.pop()\n            idx\
    \ += 1\n            if v >= 0:\n                self.ET.append(v)\n          \
    \      self.depth.append((depth, v))\n                self.vcost.append(vcost[v])\n\
    \                self.ecost.append(weight)\n                self.vcost_st.append(vcost[v])\n\
    \                self.ecost_st.append(weight)\n                seen[v] = 1\n \
    \               if self.into[v] == 0:\n                    self.into[v] = idx\n\
    \                for w, u in G[v][::-1]:\n                    if not seen[u]:\n\
    \                        self.parent[u] = v\n                        stack.append((~u,\
    \ depth, w))\n                        stack.append((u, depth + 1, w))\n      \
    \      else:\n                self.ET.append(v + 1)\n                self.depth.append((depth,\
    \ self.parent[~v]))\n                self.vcost.append(-vcost[~v])\n         \
    \       self.ecost.append(-weight)\n                self.vcost_st.append(0)\n\
    \                self.ecost_st.append(0)\n                self.out[~v] = idx\n"
  dependsOn: []
  isVerificationFile: false
  path: tree/euler_tour.py
  requiredBy: []
  timestamp: '2023-08-02 17:54:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tree/euler_tour.py
layout: document
title: Euler tour
---

木をDFS順に訪問し，その結果をさまざまな形式で格納していく.
木の情報を列に変換し，区間計算できるようにする．