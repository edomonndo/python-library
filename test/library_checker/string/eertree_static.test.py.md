---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: str/palindromic_tree.py
    title: "\u56DE\u6587\u6728"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/eertree
    links:
    - https://judge.yosupo.jp/problem/eertree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/eertree\n\n\
    from str.palindromic_tree import PalindromicTree\n\nS = input()\nPT = PalindromicTree(S,\
    \ \"a\")\npar, suffix_link, mx_palindromic_suffix = PT.solve()\nprint(PT.n)\n\
    for p, s in zip(par, suffix_link):\n    print(p, s)\nprint(*mx_palindromic_suffix)\n"
  dependsOn:
  - str/palindromic_tree.py
  isVerificationFile: true
  path: test/library_checker/string/eertree_static.test.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/string/eertree_static.test.py
layout: document
title: Eertree
---
