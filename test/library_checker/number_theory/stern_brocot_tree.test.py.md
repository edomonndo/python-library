---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: number_theory/stern_brocot_tree.py
    title: number_theory/stern_brocot_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/stern_brocot_tree
    links:
    - https://judge.yosupo.jp/problem/stern_brocot_tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/stern_brocot_tree\n\
    \nfrom number_theory.stern_brocot_tree import SternBrocotTree\n\nt = int(input())\n\
    SBT = SternBrocotTree\nfor _ in range(t):\n    s, *qu = input().split()\n    if\
    \ s == \"ENCODE_PATH\":\n        a, b = map(int, qu)\n        code = SBT.encode(a,\
    \ b)\n        ans = []\n        for is_right, k in code:\n            if is_right:\n\
    \                ans += [\"R\", str(k)]\n            else:\n                ans\
    \ += [\"L\", str(k)]\n        print(len(ans) // 2, *ans)\n    elif s == \"DECODE_PATH\"\
    :\n        code = []\n        size = int(qu[0])\n        for i in range(1, size\
    \ * 2, 2):\n            d = qu[i]\n            k = int(qu[i + 1])\n          \
    \  code.append((d == \"R\", k))\n        a, b = SBT.decode(code)\n        print(a,\
    \ b)\n    elif s == \"LCA\":\n        a, b, c, d = map(int, qu)\n        f, g\
    \ = SBT.lca(a, b, c, d)\n        print(f, g)\n    elif s == \"ANCESTOR\":\n  \
    \      k, a, b = map(int, qu)\n        f, g = SBT.ancestor(a, b, k, (-1, -1))\n\
    \        if f == -1:\n            print(-1)\n        else:\n            print(f,\
    \ g)\n    elif s == \"RANGE\":\n        a, b = map(int, qu)\n        f, g, h,\
    \ k = SBT.range(a, b)\n        print(f, g, h, k)\n"
  dependsOn:
  - number_theory/stern_brocot_tree.py
  isVerificationFile: true
  path: test/library_checker/number_theory/stern_brocot_tree.test.py
  requiredBy: []
  timestamp: '2024-08-22 11:38:30+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/number_theory/stern_brocot_tree.test.py
layout: document
title: "Stern\u2013Brocot Tree"
---
