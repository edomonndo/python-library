---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: data_structure/basic/wordsize_tree_set.py
    title: data_structure/basic/wordsize_tree_set.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
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
  isVerificationFile: false
  path: test/library_checker/data_structure/predecessor_problem.py
  requiredBy: []
  timestamp: '2024-05-29 13:44:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: test/library_checker/data_structure/predecessor_problem.py
layout: document
redirect_from:
- /library/test/library_checker/data_structure/predecessor_problem.py
- /library/test/library_checker/data_structure/predecessor_problem.py.html
title: test/library_checker/data_structure/predecessor_problem.py
---
