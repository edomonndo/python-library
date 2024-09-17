---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def next_permutation(a: list, l: int = 0, r: int = None) -> bool:\n    if\
    \ r is None:\n        r = len(a) - 1\n    for i in range(r - 1, l - 1, -1):\n\
    \        if a[i] < a[i + 1]:\n            for j in range(r, i, -1):\n        \
    \        if a[i] < a[j]:\n                    a[i], a[j] = a[j], a[i]\n      \
    \              p, q = i + 1, r\n                    while p < q:\n           \
    \             a[p], a[q] = a[q], a[p]\n                        p += 1\n      \
    \                  q -= 1\n                    return True\n    return False\n\
    \n\ndef prev_permutation(a: list, l: int = 0, r: int = None) -> bool:\n    if\
    \ r is None:\n        r = len(a) - 1\n    for i in range(r - 1, l - 1, -1):\n\
    \        if a[i] > a[i + 1]:\n            for j in range(r, i, -1):\n        \
    \        if a[i] > a[j]:\n                    a[i], a[j] = a[j], a[i]\n      \
    \              p, q = i + 1, r\n                    while p < q:\n           \
    \             a[p], a[q] = a[q], a[p]\n                        p += 1\n      \
    \                  q -= 1\n                    return True\n    return False\n\
    \n\nimport bisect\n\nMOD = 998244353\n\n\ndef get_permutation_order(A: list):\n\
    \    \"\"\"\n    \u9806\u5217\u306E\u3046\u3061a\u3068\u306A\u308B\u306E\u306F\
    \u4F55\u756A\u76EE\u304B\uFF1F\n    \u8FD4\u308A\u5024\u306F0-indexed\n    \"\"\
    \"\n    n = len(A)\n    fact = [1]\n    for i in range(n - 1):\n        x = (fact[-1]\
    \ * (i + 1)) % MOD\n        fact.append(x)\n    B = []\n    ans = 0\n    for i\
    \ in range(n - 1):\n        a = A[i]\n        k = bisect.bisect(B, a)\n      \
    \  B.insert(k, a)\n        a1 = a - 1 - k\n        ans += a1 * fact[n - 1 - i]\n\
    \        ans %= MOD\n    return ans\n\n\ndef kth_permutation(n: int, k: int) ->\
    \ list:\n    \"\"\"\n    0<=i<n\u304B\u3089\u306A\u308B\u9806\u5217\u306Ek\u756A\
    \u76EE\u3092\u8FD4\u3059. k\u306F0-indexed\n    \"\"\"\n    tmp = [i for i in\
    \ range(n)]\n\n    surplus = [-1] * n\n    for i in range(1, n):\n        surplus[n\
    \ - i] = k % i\n        k = k // i\n    surplus[0] = k\n\n    res = [-1] * n\n\
    \    for i in range(n):\n        res[i] = tmp[surplus[i]]\n        for j in range(surplus[i],\
    \ n - 1):\n            tmp[j] = tmp[j + 1]\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: utility/permutations.py
  requiredBy: []
  timestamp: '2024-05-27 17:45:23+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: utility/permutations.py
layout: document
redirect_from:
- /library/utility/permutations.py
- /library/utility/permutations.py.html
title: utility/permutations.py
---
