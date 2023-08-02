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
  code: "class BIT:\n    # \u521D\u671F\u5316\n    def __init__(self, n):\n      \
    \  self.size = n\n        self.tree = [0] * (n + 1)  # 1-index\u306E\u30EA\u30B9\
    \u30C8\u3067\u7BA1\u7406\n\n    # \u52A0\u7B97\n    def add(self, i, x):\n   \
    \     while i <= self.size:\n            self.tree[i] += x\n            i += i\
    \ & -i  # LSB\u306E\u8A08\u7B97\n\n    # \u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\
    0\u304B\u3089i\u307E\u3067\u306E\u7DCF\u548C\u3092\u8A08\u7B97\n    def sum(self,\
    \ i):\n        total = 0\n        while i > 0:\n            total += self.tree[i]\n\
    \            i -= i & -i  # LSB\u306E\u8A08\u7B97\n\n        return total\n\n\n\
    def inversionNumberByBIT(A, mod=10**9):\n    ans = 0\n    Bit = BIT(len(A))  #\
    \ Binary Indexed Tree\n    for i, a in enumerate(A):\n        ans += i - Bit.sum(a)\n\
    \        ans %= mod\n        Bit.add(a, 1)  # \u81EA\u5206\u306E\u4F4D\u7F6E\u3092\
    1\u306B\u3059\u308B\n    return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/inversion_number.py
  requiredBy: []
  timestamp: '2023-07-22 14:27:24+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/inversion_number.py
layout: document
title: "\u8EE2\u7F6E\u6570"
---
