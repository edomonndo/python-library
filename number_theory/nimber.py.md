---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/number_theory/nim_product_64.test.py
    title: Nim Product
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Nimber:\n    exp = [0] * 262300\n    log = [0] * 65536\n\n    def __init__(self):\n\
    \        base = (\n            1,\n            10279,\n            14635,\n  \
    \          32768,\n            8445,\n            19741,\n            56906,\n\
    \            2583,\n            13412,\n            58281,\n            28045,\n\
    \            13500,\n            43297,\n            41331,\n            3772,\n\
    \            3689,\n        )\n\n        exp, log = self.exp, self.log\n     \
    \   exp[0] = 1\n        for i in range(1, 65535):\n            exp[i] = exp[i\
    \ - 1] << 1\n            if exp[i] > 65535:\n                exp[i] ^= 92191\n\
    \        pre = [0] * (65535 + 1)\n        for b in range(16):\n            s,\
    \ t = 1 << b, 1 << (b + 1)\n            for i in range(s, t):\n              \
    \  pre[i] = pre[i - s] ^ base[b]\n        for i in range(65535):\n           \
    \ exp[i] = pre[exp[i]]\n            log[exp[i]] = i\n        for i in range(65535,\
    \ 2 * 65535 + 30):\n            exp[i] = exp[i - 65535]\n        log[0] = 2 *\
    \ 65535 + 31\n\n    def product_32(self, a: int, b: int) -> int:\n        exp,\
    \ log = self.exp, self.log\n        au, al = a >> 16, a & 0xFFFF\n        bu,\
    \ bl = b >> 16, b & 0xFFFF\n        l = exp[log[al] + log[bl]]\n        ul = exp[log[au\
    \ ^ al] + log[bu ^ bl]]\n        uq = exp[log[au] + log[bu] + 3]\n        return\
    \ ((ul ^ l) << 16) ^ uq ^ l\n\n    def Hproduct_32(self, a: int, b: int) -> int:\n\
    \        exp, log = self.exp, self.log\n        au, al = a >> 16, a & 0xFFFF\n\
    \        bu, bl = b >> 16, b & 0xFFFF\n        l = exp[log[al] + log[bl]]\n  \
    \      ul = exp[log[au ^ al] + log[bu ^ bl]]\n        uq = exp[log[au] + log[bu]\
    \ + 3]\n        ku, kl = ul ^ l, uq ^ l\n        return (exp[log[ku ^ kl] + 3]\
    \ << 16) ^ exp[log[ku] + 6]\n\n    def product_64(self, a: int, b: int) -> int:\n\
    \        a = a & 0xFFFFFFFFFFFFFFFF\n        b = b & 0xFFFFFFFFFFFFFFFF\n    \
    \    au, al = a >> 32, a & 0xFFFFFFFF\n        bu, bl = b >> 32, b & 0xFFFFFFFF\n\
    \        l = self.product_32(al, bl)\n        ul = self.product_32(au ^ al, bu\
    \ ^ bl)\n        uq = self.Hproduct_32(au, bu)\n        return ((ul ^ l) << 32)\
    \ | (uq ^ l)\n"
  dependsOn: []
  isVerificationFile: false
  path: number_theory/nimber.py
  requiredBy: []
  timestamp: '2024-09-05 15:49:13+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/number_theory/nim_product_64.test.py
documentation_of: number_theory/nimber.py
layout: document
title: Nimber
---
