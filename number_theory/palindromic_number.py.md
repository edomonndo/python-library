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
  code: "def nth_palindrome(n: int) -> str:\n    \"\"\"1-index\u3067n\u756A\u76EE\u306B\
    \u5C0F\u3055\u3044\u56DE\u6587\u6570\"\"\"\n    assert n > 0\n    if n == 1:\n\
    \        return 0\n    n -= 1\n    sz, cnt = 1, 9\n    while n > cnt:\n      \
    \  n -= cnt\n        sz += 1\n        cnt = 9 * (10 ** ((sz - 1) // 2))\n    half\
    \ = (sz + 1) // 2\n    s = 10 ** (half - 1)\n    num = s + (n - 1)\n    res =\
    \ str(num) + (str(num)[::-1] if sz & 1 == 0 else str(num)[-2::-1])\n    return\
    \ res\n\n\ndef count_palindrome(n: int, inf=10**20) -> int:\n    \"\"\"0\u4EE5\
    \u4E0An\u672A\u6E80\u306E\u6574\u6570\u306B\u304A\u3051\u308B\u56DE\u6587\u6570\
    \u306E\u6570\"\"\"\n\n    def bin_seach(ok: int, ng: int, include_mid: bool):\n\
    \        while abs(ok - ng) > 1:\n            mid = (ok + ng) >> 1\n         \
    \   s = str(mid)\n            t = \"\".join(reversed(s))\n            if include_mid:\n\
    \                tmp = int(s + t)\n            else:\n                tmp = int(s[:-1]\
    \ + t)\n            if tmp <= n:\n                ok = mid\n            else:\n\
    \                ng = mid\n        return ok\n\n    res = bin_seach(0, inf, 0)\
    \ + bin_seach(0, inf, 1)\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: number_theory/palindromic_number.py
  requiredBy: []
  timestamp: '2024-09-10 07:31:46+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: number_theory/palindromic_number.py
layout: document
title: "\u56DE\u6587\u6570"
---
