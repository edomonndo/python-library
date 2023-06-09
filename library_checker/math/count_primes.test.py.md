---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/counting_primes
    links:
    - https://judge.yosupo.jp/problem/counting_primes
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/counting_primes\n\
    \n\ndef count_primes(n: int) -> int:\n    \"\"\"\n    Count the number of primes\
    \ no more than N.\n    O(N**0.75 / logN)\n    \"\"\"\n    if n < 2:\n        return\
    \ 0\n    if n < 3:\n        return 1\n    if n < 5:\n        return 2\n    if\
    \ n < 7:\n        return 3\n    if n < 11:\n        return 4\n    if n < 13:\n\
    \        return 5\n    if n < 17:\n        return 6\n    if n < 19:\n        return\
    \ 7\n    if n < 23:\n        return 8\n    if n < 29:\n        return 9\n\n  \
    \  v = int(n**0.5) - 1\n    while True:\n        if v * v > n:\n            break\n\
    \        v += 1\n\n    smalls = [i + 1 >> 1 for i in range(v + 1)]\n    s = v\
    \ + 1 >> 1\n    roughs = [i << 1 | 1 for i in range(s)]\n    larges = [int(n /\
    \ (i << 1 | 1) + 1) >> 1 for i in range(s)]\n    skip = bytearray([0] * (v + 1))\n\
    \    pc = 0\n    for p in range(3, v + 1, 2):\n        if skip[p]:\n         \
    \   continue\n        q = p * p\n        pc += 1\n        if q * q > n:\n    \
    \        break\n        skip[p] = 1\n        for i in range(q, v + 1, p << 1):\n\
    \            skip[i] = 1\n        ns = 0\n        for k in range(s):\n       \
    \     i = roughs[k]\n            if skip[i]:\n                continue\n     \
    \       d = i * p\n            if d <= v:\n                x = larges[smalls[d]\
    \ - pc]\n            else:\n                x = smalls[int(n / d)]\n         \
    \   larges[ns] = larges[k] + pc - x\n            roughs[ns] = i\n            ns\
    \ += 1\n        s = ns\n        i = v\n        for j in range(int(v / p), p -\
    \ 1, -1):\n            c = smalls[j] - pc\n            e = j * p\n           \
    \ while i >= e:\n                smalls[i] -= c\n                i -= 1\n    ret\
    \ = larges[0] + ((s + (pc - 1 << 1)) * (s - 1) >> 1) - sum(larges[1:s])\n\n  \
    \  for l in range(1, s):\n        q = roughs[l]\n        m = int(n / q)\n    \
    \    e = smalls[int(m / q)] - pc\n        if e <= l:\n            break\n    \
    \    t = 0\n        for r in roughs[l + 1 : e + 1]:\n            t += smalls[int(m\
    \ / r)]\n        ret += t - (e - l) * (pc + l - 1)\n    return ret\n\n\nN = int(input())\n\
    print(count_primes(N))\n"
  dependsOn: []
  isVerificationFile: true
  path: library_checker/math/count_primes.test.py
  requiredBy: []
  timestamp: '2023-06-09 12:11:59+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: library_checker/math/count_primes.test.py
layout: document
redirect_from:
- /verify/library_checker/math/count_primes.test.py
- /verify/library_checker/math/count_primes.test.py.html
title: library_checker/math/count_primes.test.py
---