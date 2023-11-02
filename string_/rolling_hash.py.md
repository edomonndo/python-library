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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class RollingHash:\n    def __init__(self, S, base=317, mod=1 << 61 - 1):\n\
    \        self.S = S\n        self.mod = mod\n        self.pow_base = [1]\n   \
    \     self.hash = [0]\n        for s in S:\n            self.hash.append((self.hash[-1]\
    \ * base + ord(s)) % self.mod)\n            self.pow_base.append((self.pow_base[-1]\
    \ * base) % self.mod)\n\n    def get(self, l, r):\n        return (self.hash[r]\
    \ - self.hash[l] * self.pow_base[r - l]) % self.mod\n"
  dependsOn: []
  isVerificationFile: false
  path: string_/rolling_hash.py
  requiredBy: []
  timestamp: '2023-07-22 14:27:24+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: string_/rolling_hash.py
layout: document
title: "\u30ED\u30FC\u30EA\u30F3\u30B0\u30CF\u30C3\u30B7\u30E5"
---

文字列を高速に検索する.