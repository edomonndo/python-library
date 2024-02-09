---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A\n\
    \n\nif __name__ == \"__main__\":\n    from pathlib import Path\n    import sys\n\
    \n    sys.path.append(str(Path(__file__).resolve().parent.parent.parent))\n  \
    \  from tree.euler_tour import EulerTour\n\n    N = 6\n    G = [[] for _ in range(N)]\n\
    \    edges = [(0, 1, 1), (0, 5, 16), (1, 2, 2), (1, 4, 8), (2, 3, 4)]\n    Vs\
    \ = [1, 2, 4, 8, 16, 32]\n    for u, v, w in edges:\n        G[u].append((v, w))\n\
    \        G[v].append((u, w))\n    root = 0\n    et = EulerTour(G, root, Vs)\n\n\
    \    assert et.ET == [0, 5, 0, 1, 4, 1, 2, 3, 2, 1, 0], et.ET\n    assert et.into\
    \ == [0, 3, 6, 7, 4, 1], et.into\n    assert et.out == [11, 10, 9, 8, 5, 2], et.out\n\
    \    assert et.depth == [0, 1, 2, 3, 2, 1, 6], et.depth\n    assert et.vcost ==\
    \ [1, 32, -32, 2, 16, -16, 4, 8, -8, -4, -2], et.vcost\n    assert et.ecost ==\
    \ [0, 16, -16, 1, 8, -8, 2, 4, -4, -2, -1], et.ecost\n    assert et.vcost_st ==\
    \ [1, 32, 0, 2, 16, 0, 4, 8, 0, 0, 0], et.vcost_st\n    assert et.ecost_st ==\
    \ [0, 16, 0, 1, 8, 0, 2, 4, 0, 0, 0], et.ecost_st\n\n    # Range Sum Query1 \u9802\
    \u70B9v\u3092\u6839\u3068\u3059\u308B\u90E8\u5206\u6728\u306E\u9802\u70B9\u306E\
    \u5024\u306E\u548C\n    assert et.subtree_verticle_sum(0) == 63, et.subtree_verticle_sum(0)\n\
    \    assert et.subtree_verticle_sum(1) == 30, et.subtree_verticle_sum(1)\n   \
    \ assert et.subtree_verticle_sum(2) == 12, et.subtree_verticle_sum(2)\n    assert\
    \ et.subtree_verticle_sum(3) == 8, et.subtree_verticle_sum(3)\n    assert et.subtree_verticle_sum(4)\
    \ == 16, et.subtree_verticle_sum(4)\n    assert et.subtree_verticle_sum(5) ==\
    \ 32, et.subtree_verticle_sum(5)\n\n    # Range Sum Query2 \u9802\u70B9v\u3092\
    \u6839\u3068\u3059\u308B\u90E8\u5206\u6728\u306E\u8FBA\u306E\u5024\u306E\u548C\
    \n    assert et.subtree_edge_sum(0) == 31, et.subtree_edge_sum(0)\n    assert\
    \ et.subtree_edge_sum(1) == 14, et.subtree_edge_sum(1)\n    assert et.subtree_edge_sum(2)\
    \ == 4, et.subtree_edge_sum(2)\n    assert et.subtree_edge_sum(3) == 0, et.subtree_edge_sum(3)\n\
    \    assert et.subtree_edge_sum(4) == 0, et.subtree_edge_sum(4)\n    assert et.subtree_edge_sum(5)\
    \ == 0, et.subtree_edge_sum(5)\n\n    # Path Query1 \u6839\u304B\u3089\u9802\u70B9\
    v\u307E\u3067\u306E\u9802\u70B9\u306E\u5024\u306E\u548C\n    assert et.path_verticle_sum(0)\
    \ == 1, et.path_verticle_sum(0)\n    assert et.path_verticle_sum(1) == 3, et.path_verticle_sum(1)\n\
    \    assert et.path_verticle_sum(2) == 7, et.path_verticle_sum(2)\n    assert\
    \ et.path_verticle_sum(3) == 15, et.path_verticle_sum(3)\n    assert et.path_verticle_sum(4)\
    \ == 19, et.path_verticle_sum(4)\n    assert et.path_verticle_sum(5) == 33, et.path_verticle_sum(5)\n\
    \n    # Path Query2 \u6839\u304B\u3089\u9802\u70B9v\u307E\u3067\u306E\u8FBA\u306E\
    \u5024\u306E\u548C\n    assert et.path_edge_sum(0) == 0, et.path_edge_sum(0)\n\
    \    assert et.path_edge_sum(1) == 1, et.path_edge_sum(1)\n    assert et.path_edge_sum(2)\
    \ == 3, et.path_edge_sum(2)\n    assert et.path_edge_sum(3) == 7, et.path_edge_sum(3)\n\
    \    assert et.path_edge_sum(4) == 9, et.path_edge_sum(4)\n    assert et.path_edge_sum(5)\
    \ == 16, et.path_edge_sum(5)\n\n    # \u9802\u70B9u,v\u306ELCA\n    for u in range(6):\n\
    \        for v in range(6):\n            if u == v:\n                assert et.lca(u,\
    \ v) == u, et.lca(u, v)\n            elif u == 0 or v == 0:\n                assert\
    \ et.lca(u, v) == 0, et.lca(u, v)\n            elif u == 5 or v == 5:\n      \
    \          assert et.lca(u, v) == 0, et.lca(u, v)\n            elif u == 1 or\
    \ v == 1:\n                assert et.lca(u, v) == 1, et.lca(u, v)\n          \
    \  elif (u == 2 and v == 3) or (v == 2 and u == 3):\n                assert et.lca(u,\
    \ v) == 2, et.lca(u, v)\n            elif (u == 2 and v == 4) or (v == 2 and u\
    \ == 4):\n                assert et.lca(u, v) == 1, et.lca(u, v)\n           \
    \ elif (u == 3 and v == 4) or (v == 3 and u == 4):\n                assert et.lca(u,\
    \ v) == 1, et.lca(u, v)\n            else:\n                assert False\n\n \
    \   # \u8FBA\u306E\u91CD\u307F\u3092\u66F4\u65B0\n    ediff = 1\n    et.update_parent_edge(2,\
    \ 2 + ediff)\n\n    assert et.subtree_edge_sum(0) == 31 + ediff, et.subtree_edge_sum(0)\n\
    \    assert et.subtree_edge_sum(1) == 14 + ediff, et.subtree_edge_sum(1)\n   \
    \ assert et.subtree_edge_sum(2) == 4, et.subtree_edge_sum(2)\n    assert et.subtree_edge_sum(3)\
    \ == 0, et.subtree_edge_sum(3)\n    assert et.subtree_edge_sum(4) == 0, et.subtree_edge_sum(4)\n\
    \    assert et.subtree_edge_sum(5) == 0, et.subtree_edge_sum(5)\n\n    assert\
    \ et.path_edge_sum(0) == 0, et.path_edge_sum(0)\n    assert et.path_edge_sum(1)\
    \ == 1, et.path_edge_sum(1)\n    assert et.path_edge_sum(2) == 3 + ediff, et.path_edge_sum(2)\n\
    \    assert et.path_edge_sum(3) == 7 + ediff, et.path_edge_sum(3)\n    assert\
    \ et.path_edge_sum(4) == 9, et.path_edge_sum(4)\n    assert et.path_edge_sum(5)\
    \ == 16, et.path_edge_sum(5)\n\n    # \u9802\u70B9\u306E\u91CD\u307F\u3092\u66F4\
    \u65B0\n    vdiff = 1\n    et.update_verticle(2, 4 + vdiff)\n\n    assert et.subtree_verticle_sum(0)\
    \ == 63 + vdiff, et.subtree_verticle_sum(0)\n    assert et.subtree_verticle_sum(1)\
    \ == 30 + vdiff, et.subtree_verticle_sum(1)\n    assert et.subtree_verticle_sum(2)\
    \ == 12 + vdiff, et.subtree_verticle_sum(2)\n    assert et.subtree_verticle_sum(3)\
    \ == 8, et.subtree_verticle_sum(3)\n    assert et.subtree_verticle_sum(4) == 16,\
    \ et.subtree_verticle_sum(4)\n    assert et.subtree_verticle_sum(5) == 32, et.subtree_verticle_sum(5)\n\
    \n    assert et.path_verticle_sum(0) == 1, et.path_verticle_sum(0)\n    assert\
    \ et.path_verticle_sum(1) == 3, et.path_verticle_sum(1)\n    assert et.path_verticle_sum(2)\
    \ == 7 + vdiff, et.path_verticle_sum(2)\n    assert et.path_verticle_sum(3) ==\
    \ 15 + vdiff, et.path_verticle_sum(3)\n    assert et.path_verticle_sum(4) == 19,\
    \ et.path_verticle_sum(4)\n    assert et.path_verticle_sum(5) == 33, et.path_verticle_sum(5)\n\
    \n    print(\"Hello World\")\n"
  dependsOn: []
  isVerificationFile: true
  path: test/unit_test/euler_tour.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/unit_test/euler_tour.test.py
layout: document
redirect_from:
- /verify/test/unit_test/euler_tour.test.py
- /verify/test/unit_test/euler_tour.test.py.html
title: test/unit_test/euler_tour.test.py
---
