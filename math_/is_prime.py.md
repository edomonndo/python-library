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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List\n\n\ndef miller_rabin(n: int) -> bool:\n    \"\"\"\
    Miller-Rabin: \u2252 O(1)\"\"\"\n    assert n <= 1 << 64\n    if n == 2:\n   \
    \     return True\n    if n < 2 or (n & 1) == 0:\n        return False\n    n1\
    \ = n - 1\n    d, s = n1, 0\n    while (d & 1) == 0:\n        d //= 2\n      \
    \  s += 1\n    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:\n\
    \        if a % n == 0:\n            continue\n        t = pow(a, d, n)\n    \
    \    if t == 1 or t == n1:\n            continue\n        for _ in range(s):\n\
    \            t = pow(t, 2, n)\n            if t == n1:\n                break\n\
    \        else:\n            return False\n    return True\n\n\ndef eratosthenes(N:\
    \ int) -> List[bool]:\n    # \u30C6\u30FC\u30D6\u30EB\n    isprime = [True] *\
    \ (N + 1)\n\n    # 0, 1 \u306F\u4E88\u3081\u3075\u308B\u3044\u843D\u3068\u3057\
    \u3066\u304A\u304F\n    isprime[0], isprime[1] = False, False\n\n    # \u3075\u308B\
    \u3044\n    for p in range(2, N + 1):\n        # \u3059\u3067\u306B\u5408\u6210\
    \u6570\u3067\u3042\u308B\u3082\u306E\u306F\u30B9\u30AD\u30C3\u30D7\u3059\u308B\
    \n        if not isprime[p]:\n            continue\n\n        # p \u4EE5\u5916\
    \u306E p \u306E\u500D\u6570\u304B\u3089\u7D20\u6570\u30E9\u30D9\u30EB\u3092\u5265\
    \u596A\n        q = p * 2\n        while q <= N:\n            isprime[q] = False\n\
    \            q += p\n\n    # 1 \u4EE5\u4E0A N \u4EE5\u4E0B\u306E\u6574\u6570\u304C\
    \u7D20\u6570\u304B\u3069\u3046\u304B\n    return isprime\n"
  dependsOn: []
  isVerificationFile: false
  path: math_/is_prime.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: math_/is_prime.py
layout: document
title: "\u7D20\u6570\u5224\u5B9A"
---

### `miller_rabin(n: int)`

$n$が素数かを高速に判定する。$n<=2^{64}$で決定的。

### `eratosthenes(n: int)`

$n$以下の非負整数が素数かどうかを配列で返す。