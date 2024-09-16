---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: str/palindromic_tree_deque.py
    title: str/palindromic_tree_deque.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/palindromes_in_deque
    links:
    - https://judge.yosupo.jp/problem/palindromes_in_deque
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/palindromes_in_deque\n\
    \nfrom str.palindromic_tree_deque import DequePalindromicTree\n\nq = int(input())\n\
    PT = DequePalindromicTree(q, \"a\", 26)\nfor _ in range(q):\n    t, *qu = input().split()\n\
    \    if t == \"0\":\n        PT.appendleft(qu[0])\n    elif t == \"1\":\n    \
    \    PT.append(qu[0])\n    elif t == \"2\":\n        PT.popleft()\n    elif t\
    \ == \"3\":\n        PT.pop()\n    print(\n        PT.distinct(),\n        PT.max_prefix_size(),\n\
    \        PT.max_suffix_size(),\n    )\n"
  dependsOn:
  - str/palindromic_tree_deque.py
  isVerificationFile: true
  path: test/library_checker/string/palindromes_in_deque.test.py
  requiredBy: []
  timestamp: '2024-09-16 13:52:09+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/string/palindromes_in_deque.test.py
layout: document
title: Palindromes in Deque
---
