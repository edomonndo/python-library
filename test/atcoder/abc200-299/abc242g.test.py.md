---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/mo.py
    title: Mo's Algorithm
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/abc242/tasks/abc242_g
    links:
    - https://atcoder.jp/contests/abc242/tasks/abc242_g
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc242/tasks/abc242_g\n\
    \n\nfrom data_structure.mo import Mo\n\n\nclass MoState:\n    def __init__(self,\
    \ max_value):\n        self.cnt = [0] * (max_value + 1)\n        self.res = 0\n\
    \n    def add(self, x):\n        \"\u533A\u9593\u306E\u7AEF\u306B x \u3092\u8FFD\
    \u52A0\u3059\u308B\u3068\u304D\u306E\u51E6\u7406\"\n        self.cnt[x] += 1\n\
    \        # ToDo\n        if self.cnt[x] & 1 == 0:\n            self.res += 1\n\
    \n    def delete(self, x):\n        \"\u533A\u9593\u306E\u7AEF\u304B\u3089 x \u3092\
    \u524A\u9664\u3059\u308B\u3068\u304D\u306E\u51E6\u7406\"\n        self.cnt[x]\
    \ -= 1\n        # ToDo\n        if self.cnt[x] & 1:\n            self.res -= 1\n\
    \n\nN = int(input())\nA = [int(x) for x in input().split()]\nQ = int(input())\n\
    state = MoState(max(A))\nmo = Mo(A, state)\nfor _ in range(Q):\n    l, r = map(int,\
    \ input().split())\n    mo.add_query(l - 1, r)\n\nans = mo.calc()\nprint(*ans,\
    \ sep=\"\\n\")\n"
  dependsOn:
  - data_structure/mo.py
  isVerificationFile: true
  path: test/atcoder/abc200-299/abc242g.test.py
  requiredBy: []
  timestamp: '2024-06-24 17:00:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/abc200-299/abc242g.test.py
layout: document
title: G - Range Pairing Query
---
