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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
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
    \n\nimport bisect\n\n\ndef nth_permutations(A: list, MOD: int = 10**18):\n   \
    \ \"\"\"\n    \u9806\u5217\u306E\u3046\u3061a\u3068\u306A\u308B\u306E\u306F\u4F55\
    \u756A\u76EE\u304B\uFF1F\n    \u8FD4\u308A\u5024\u306F0-indexed\n    \"\"\"\n\
    \    n = len(A)\n    fact = [1]\n    for i in range(n - 1):\n        x = (fact[-1]\
    \ * (i + 1)) % MOD\n        fact.append(x)\n    B = []\n    ans = 0\n    for i\
    \ in range(n - 1):\n        a = A[i]\n        k = bisect.bisect(B, a)\n      \
    \  B.insert(k, a)\n        a1 = a - 1 - k\n        ans += a1 * fact[n - 1 - i]\n\
    \        ans %= MOD\n    return ans\n\n\nif __name__ == \"__main__\":\n    n =\
    \ 3\n    a = [0, 1, 2]\n    res = []\n    while True:\n        res.append(a[:])\n\
    \        if not next_permutation(a, 0, n - 1):\n            break\n    assert\
    \ res == [\n        [0, 1, 2],\n        [0, 2, 1],\n        [1, 0, 2],\n     \
    \   [1, 2, 0],\n        [2, 0, 1],\n        [2, 1, 0],\n    ], res\n\n    a =\
    \ [2, 1, 0]\n    res = []\n    while True:\n        res.append(a[:])\n       \
    \ if not prev_permutation(a, 0, n - 1):\n            break\n    assert res ==\
    \ [\n        [2, 1, 0],\n        [2, 0, 1],\n        [1, 2, 0],\n        [1, 0,\
    \ 2],\n        [0, 2, 1],\n        [0, 1, 2],\n    ], res\n\n    n = 3\n    a\
    \ = [3, 1, 5, 4, 2]\n    assert nth_permutations(a) == 53\n"
  dependsOn: []
  isVerificationFile: false
  path: utility/permutations.py
  requiredBy: []
  timestamp: '2023-07-23 00:15:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: utility/permutations.py
layout: document
title: "\u9806\u5217"
---

