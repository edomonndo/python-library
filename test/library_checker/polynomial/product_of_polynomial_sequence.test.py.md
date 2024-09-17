---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: polynomial/formal_power_series.py
    title: polynomial/formal_power_series.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/product_of_polynomial_sequence
    links:
    - https://judge.yosupo.jp/problem/product_of_polynomial_sequence
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/product_of_polynomial_sequence\n\
    \nfrom polynomial.formal_power_series import multiply\n\nfrom collections import\
    \ deque\n\nn = int(input())\nif n == 0:\n    print(1)\n    exit()\ndeq = deque()\n\
    for _ in range(n):\n    _, *a = map(int, input().split())\n    deq.append(a)\n\
    while len(deq) >= 2:\n    deq.append(multiply(deq.popleft(), deq.popleft()))\n\
    print(*deq.pop())\n"
  dependsOn:
  - polynomial/formal_power_series.py
  isVerificationFile: true
  path: test/library_checker/polynomial/product_of_polynomial_sequence.test.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/polynomial/product_of_polynomial_sequence.test.py
layout: document
title: Product of Polynomial Sequence
---
