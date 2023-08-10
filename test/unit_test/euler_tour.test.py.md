---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A\n\
    \n\nif __name__ == \"__main__\":\n    from pathlib import Path\n    import sys\n\
    \n    sys.path.append(str(Path(__file__).resolve().parent.parent.parent))\n  \
    \  from data_structure.segment_tree import Segtree\n    from tree.euler_tour import\
    \ EulerTour\n\n    N = 6\n    G = [[] for _ in range(N)]\n    edges = [(0, 1,\
    \ 1), (0, 5, 16), (1, 2, 2), (1, 4, 8), (2, 3, 4)]\n    Vs = [1, 2, 4, 8, 16,\
    \ 32]\n    for u, v, w in edges:\n        G[u].append((w, v))\n        G[v].append((w,\
    \ u))\n    root = 0\n    et = EulerTour(N, G, root, Vs)\n\n    assert et.ET ==\
    \ [0, 1, 2, 3, -3, -2, 4, -4, -1, 5, -5, 0], et.ET\n    assert et.into == [0,\
    \ 1, 2, 3, 6, 9], et.into\n    assert et.out == [11, 8, 5, 4, 7, 10], et.out\n\
    \    assert et.depth == [\n        (0, 0),\n        (1, 1),\n        (2, 2),\n\
    \        (3, 3),\n        (2, 2),\n        (1, 1),\n        (2, 4),\n        (1,\
    \ 1),\n        (0, 0),\n        (1, 5),\n        (0, 0),\n        (0, -1),\n \
    \   ], et.depth\n    assert et.vcost == [1, 2, 4, 8, -8, -4, 16, -16, -2, 32,\
    \ -32, -1], et.vcost\n    assert et.ecost == [0, 1, 2, 4, -4, -2, 8, -8, -1, 16,\
    \ -16, 0], et.ecost\n    assert et.vcost_st == [1, 2, 4, 8, 0, 0, 16, 0, 0, 32,\
    \ 0, 0], et.vcost_st\n    assert et.ecost_st == [0, 1, 2, 4, 0, 0, 8, 0, 0, 16,\
    \ 0, 0], et.ecost_st\n\n    # Range Sum Query1 \u9802\u70B9v\u3092\u6839\u3068\
    \u3059\u308B\u90E8\u5206\u6728\u306E\u9802\u70B9\u306E\u5024\u306E\u548C\n   \
    \ SegRSQ1 = Segtree(et.vcost_st, (lambda x, y: x + y), 0)\n    v = 1\n    l, r\
    \ = et.into[v], et.out[v]\n    assert SegRSQ1.prod(l, r) == 30, SegRSQ1.prod(l,\
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
    \ + 1)\n\n    # \u9802\u70B9u,v\u306ELCA\n    # (depth, v)\u3067\u8FD4\u308B.\u6700\
    \u5C0F\u306Edepth\u306B\u5BFE\u3059\u308Bv\u304CLCA\n    SegLca = Segtree(et.depth,\
    \ min, (10**9, N))\n    u, v = 2, 5\n    if u == v:\n        pass\n    else:\n\
    \        l, r = et.into[u], et.into[v]\n        if l > r:\n            l, r =\
    \ r, l\n        assert SegLca.prod(l, r + 1) == (0, 0), SegLca.prod(l, r + 1)\n\
    \n    print(\"Hello World\")\n"
  dependsOn: []
  isVerificationFile: true
  path: test/unit_test/euler_tour.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unit_test/euler_tour.test.py
layout: document
redirect_from:
- /verify/test/unit_test/euler_tour.test.py
- /verify/test/unit_test/euler_tour.test.py.html
title: test/unit_test/euler_tour.test.py
---
