---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: number_theory/count_squarefree.py
    title: number_theory/count_squarefree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/counting_squarefrees
    links:
    - https://judge.yosupo.jp/problem/counting_squarefrees
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/counting_squarefrees


    from number_theory.count_squarefree import count_squarefree


    n = int(input())

    print(count_squarefree(n))

    '
  dependsOn:
  - number_theory/count_squarefree.py
  isVerificationFile: true
  path: test/library_checker/number_theory/counting_squarefrees.test.py
  requiredBy: []
  timestamp: '2024-08-22 11:09:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/number_theory/counting_squarefrees.test.py
layout: document
title: Counting Square-free Integers
---
