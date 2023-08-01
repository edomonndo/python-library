---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/vertex_set_path_composite
    links:
    - https://judge.yosupo.jp/problem/vertex_set_path_composite
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_set_path_composite\n\
    \nfrom pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent))\n\
    \nfrom tree.euler_tour import EulerTour\nfrom data_structure.segment_tree import\
    \ Segtree\n\nN, Q = map(int, input().split())\nA = list(map(int, input().split()))\n\
    G = [[] for _ in range(N)]\nfor _ in range(N - 1):\n    u, v = map(int, input().split())\n\
    \    G[u].append((1, v))\n    G[v].append((1, u))\n\net = EulerTour(N, G, 0, A)\n\
    segPQ = Segtree(et.vcost, (lambda x, y: x + y), 0)\nsegLca = Segtree(et.depth,\
    \ min, 10**9)\nfor _ in range(Q):\n    t, *q = map(int, input().split())\n   \
    \ if t == 0:\n        p, x = q\n        segPQ.set(p, x)\n    elif t == 1:\n  \
    \      u, v = q\n        l, r = et.into[u], et.into[v]\n        if l > r:\n  \
    \          l, r = r, l\n        lca = segLca.prod(l, r + 1)\n        m = et.into[lca]\n\
    \        print(\n            segPQ.prod(0, l + 1)\n            + segPQ.prod(0,\
    \ r + 1)\n            - 2 * segPQ.prod(0, m + 1)\n            + segPQ.get(m)\n\
    \        )\n"
  dependsOn: []
  isVerificationFile: true
  path: test/library_checker/data_structure/vertext_set_path_composite.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/data_structure/vertext_set_path_composite.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/vertext_set_path_composite.test.py
- /verify/test/library_checker/data_structure/vertext_set_path_composite.test.py.html
title: test/library_checker/data_structure/vertext_set_path_composite.test.py
---
