---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: str/palindromic_tree.py
    title: str/palindromic_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
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
    \ \"a\")\npar, suffix_link, mx_palindromic_suffix = PT.solve()\nprint(PT.n - 2)\n\
    for p, s in zip(par, suffix_link):\n    print(p, s)\nprint(*mx_palindromic_suffix)\n"
  dependsOn:
  - str/palindromic_tree.py
  isVerificationFile: true
  path: test/library_checker/string/eertree_static.test.py
  requiredBy: []
  timestamp: '2024-08-05 22:04:36+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/string/eertree_static.test.py
layout: document
title: Eertree
---
