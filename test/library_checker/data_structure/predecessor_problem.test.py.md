---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/basic/wordsize_tree_set.py
    title: "32\u5206\u6728"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/predecessor_problem
    links:
    - https://judge.yosupo.jp/problem/predecessor_problem
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/predecessor_problem\n\
    \nfrom data_structure.basic.wordsize_tree_set import WordsizeTreeSet\n\nn, q =\
    \ map(int, input().split())\ns = input()\nT = WordsizeTreeSet(n, [i for i, c in\
    \ enumerate(s) if c == \"1\"])\nans = []\nfor _ in range(q):\n    c, k = map(int,\
    \ input().split())\n    if c == 0:\n        T.add(k)\n    elif c == 1:\n     \
    \   T.discard(k)\n    elif c == 2:\n        ans.append(\"1\" if k in T else \"\
    0\")\n    elif c == 3:\n        ans.append(str(T.ge(k)))\n    else:\n        ans.append(str(T.le(k)))\n\
    \nfor k in ans:\n    print(k)\n"
  dependsOn:
  - data_structure/basic/wordsize_tree_set.py
  isVerificationFile: true
  path: test/library_checker/data_structure/predecessor_problem.test.py
  requiredBy: []
  timestamp: '2024-06-05 09:56:18+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/predecessor_problem.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/predecessor_problem.test.py
- /verify/test/library_checker/data_structure/predecessor_problem.test.py.html
title: test/library_checker/data_structure/predecessor_problem.test.py
---
