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
    \ LCA\n        self.depth = []\n        # For Path Query\n        self.vcost =\
    \ []\n        self.ecost = []\n        # For Range Sum Query\n        self.vcost_st\
    \ = []\n        self.ecost_st = []\n\n        # \u975E\u518D\u5E30DFS\n      \
    \  seen = [0] * N\n        idx = -1\n        depth = 0\n        stack = [(~root,\
    \ -depth, 0), (root, depth, 0)]\n        while stack:\n            v, depth, weight\
    \ = stack.pop()\n            idx += 1\n            if v >= 0:\n              \
    \  self.ET.append(v)\n                self.depth.append(depth)\n             \
    \   self.vcost.append(vcost[v])\n                self.ecost.append(weight)\n \
    \               self.vcost_st.append(vcost[v])\n                self.ecost_st.append(weight)\n\
    \                seen[v] = 1\n                if self.into[v] == 0:\n        \
    \            self.into[v] = idx\n                for w, u in G[v][::-1]:\n   \
    \                 if not seen[u]:\n                        stack.append((~u, depth,\
    \ w))\n                        stack.append((u, depth + 1, w))\n            else:\n\
    \                self.ET.append(v + 1)\n                self.depth.append(depth)\n\
    \                self.vcost.append(-vcost[~v])\n                self.ecost.append(-weight)\n\
    \                self.vcost_st.append(0)\n                self.ecost_st.append(0)\n\
    \                self.out[~v] = idx\n\n\nif __name__ == \"__main__\":\n    from\
    \ pathlib import Path\n    import sys\n\n    sys.path.append(str(Path(__file__).resolve().parent.parent))\n\
    \    from data_structure.segment_tree import Segtree\n\n    N = 6\n    G = [[]\
    \ for _ in range(N)]\n    edges = [(0, 1, 1), (0, 5, 16), (1, 2, 2), (1, 4, 8),\
    \ (2, 3, 4)]\n    Vs = [1, 2, 4, 8, 16, 32]\n    for u, v, w in edges:\n     \
    \   G[u].append((w, v))\n        G[v].append((w, u))\n    root = 0\n    et = EulerTour(N,\
    \ G, root, Vs)\n\n    assert et.ET == [0, 1, 2, 3, -3, -2, 4, -4, -1, 5, -5, 0],\
    \ et.ET\n    assert et.into == [0, 1, 2, 3, 6, 9], et.into\n    assert et.out\
    \ == [11, 8, 5, 4, 7, 10], et.out\n    assert et.depth == [0, 1, 2, 3, 2, 1, 2,\
    \ 1, 0, 1, 0, 0], et.depth\n    assert et.vcost == [1, 2, 4, 8, -8, -4, 16, -16,\
    \ -2, 32, -32, -1], et.vcost\n    assert et.ecost == [0, 1, 2, 4, -4, -2, 8, -8,\
    \ -1, 16, -16, 0], et.ecost\n    assert et.vcost_st == [1, 2, 4, 8, 0, 0, 16,\
    \ 0, 0, 32, 0, 0], et.vcost_st\n    assert et.ecost_st == [0, 1, 2, 4, 0, 0, 8,\
    \ 0, 0, 16, 0, 0], et.ecost_st\n\n    # Range Sum Query1 \u9802\u70B9v\u3092\u6839\
    \u3068\u3059\u308B\u90E8\u5206\u6728\u306E\u9802\u70B9\u306E\u5024\u306E\u548C\
    \n    SegRSQ1 = Segtree(et.vcost_st, (lambda x, y: x + y), 0)\n    v = 1\n   \
    \ l, r = et.into[v], et.out[v]\n    assert SegRSQ1.prod(l, r) == 30, SegRSQ1.prod(l,\
    \ r)\n\n    # Range Sum Query2 \u9802\u70B9v\u3092\u6839\u3068\u3059\u308B\u90E8\
    \u5206\u6728\u306E\u8FBA\u306E\u5024\u306E\u548C\n    SegRSQ2 = Segtree(et.ecost_st,\
    \ (lambda x, y: x + y), 0)\n    v = 1\n    l, r = et.into[v] + 1, et.out[v]\n\
    \    assert SegRSQ2.prod(l, r) == 14, SegRSQ2.prod(l, r)\n\n    # Path Query1\
    \ \u6839\u304B\u3089\u9802\u70B9v\u307E\u3067\u306E\u9802\u70B9\u306E\u5024\u306E\
    \u548C\n    SegPQ1 = Segtree(et.vcost, (lambda x, y: x + y), 0)\n    v = 4\n \
    \   assert SegPQ1.prod(0, et.into[v] + 1) == 19, SegPQ1.prod(0, et.into[v] + 1)\n\
    \n    # Path Query2 \u6839\u304B\u3089\u9802\u70B9v\u307E\u3067\u306E\u8FBA\u306E\
    \u5024\u306E\u548C\n    SegPQ2 = Segtree(et.ecost, (lambda x, y: x + y), 0)\n\
    \    v = 4\n    assert SegPQ2.prod(0, et.into[v] + 1) == 9, SegPQ2.prod(0, et.into[v]\
    \ + 1)\n\n    # \u9802\u70B9u,v\u306ELCA\n    SegLca = Segtree(et.depth, min,\
    \ 10**9)\n    u, v = 2, 5\n    assert SegLca.prod(et.into[u], et.into[v]) == 0\n"
  dependsOn: []
  isVerificationFile: false
  path: tree/euler_tour.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tree/euler_tour.py
layout: document
redirect_from:
- /library/tree/euler_tour.py
- /library/tree/euler_tour.py.html
title: tree/euler_tour.py
---
