---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: other/typical_problems_of_sum.py
    title: "\u5178\u578B\u554F\u984C\uFF08\u8DB3\u3057\u4E0A\u3052\uFF09"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A\n\
    \n\ndef greedy1(A):\n    n = len(A)\n    res = 0\n    for i in range(n):\n   \
    \     for j in range(i + 1, n):\n            res += A[i] * A[j]\n    return res\n\
    \n\ndef greedy2(A):\n    n = len(A)\n    res = 0\n    for i in range(n):\n   \
    \     for j in range(i + 1, n):\n            res += min(A[i], A[j])\n    return\
    \ res\n\n\ndef greedy3(A):\n    n = len(A)\n    res = 0\n    for i in range(n):\n\
    \        for j in range(i + 1, n):\n            for k in range(j + 1, n):\n  \
    \              res += A[i] * A[j] * A[k]\n    return res\n\n\ndef greedy4(A):\n\
    \    n = len(A)\n    res = 0\n    for i in range(n):\n        for j in range(i\
    \ + 1, n):\n            for k in range(j + 1, n):\n                res += min(A[i],\
    \ A[j], A[k])\n    return res\n\n\ndef greedy5(A):\n    n = len(A)\n    res =\
    \ 0\n    for i in range(n - 1):\n        for j in range(i + 1, n):\n         \
    \   res += A[i] ^ A[j]\n    return res\n\n\ndef greedy6(A):\n    n = len(A)\n\
    \    res = 0\n    for i in range(n - 1):\n        for j in range(i + 1, n):\n\
    \            res += (A[i] - A[j]) ** 2\n    return res\n\n\ndef greedy7(A):\n\
    \    n = len(A)\n    res = 0\n    for i in range(n - 1):\n        for j in range(i\
    \ + 1, n):\n            res += abs(A[i] - A[j])\n    return res\n\n\nif __name__\
    \ == \"__main__\":\n    from other.typical_problems_of_sum import *\n\n    import\
    \ random\n\n    testcase = 10\n    for _ in range(testcase):\n        n = 100\n\
    \        A = [random.randrange(1, 10**9) for _ in range(n)]\n        assert greedy1(A)\
    \ == solve1(A)\n        assert greedy2(A) == solve2(A)\n        assert greedy3(A)\
    \ == solve3(A)\n        assert greedy4(A) == solve4(A)\n        assert greedy5(A)\
    \ == solve5(A)\n        assert greedy6(A) == solve6(A)\n        assert greedy7(A)\
    \ == solve7(A)\n\n    print(\"Hello World\")\n"
  dependsOn:
  - other/typical_problems_of_sum.py
  isVerificationFile: true
  path: test/unit_test/typical_problems_of_sum.test.py
  requiredBy: []
  timestamp: '2024-07-23 17:42:41+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unit_test/typical_problems_of_sum.test.py
layout: document
title: "\u5178\u578B\u8DB3\u3057\u4E0A\u3052"
---
