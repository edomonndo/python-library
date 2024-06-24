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
  _verificationStatusIcon: ':grey_question:'
  attributes:
    IGNORE: https://atcoder.jp/contests/abc293/tasks/abc293_g
    links:
    - https://atcoder.jp/contests/abc293/tasks/abc293_g
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: IGNORE https://atcoder.jp/contests/abc293/tasks/abc293_g\n\
    \n\nfrom data_structure.mo import Mo\n\n\nclass MoState:\n    def __init__(self,\
    \ max_value):\n        self.cnt = [0] * (max_value + 1)\n        self.res = 0\n\
    \n    def add(self, x):\n        \"\u533A\u9593\u306E\u7AEF\u306B x \u3092\u8FFD\
    \u52A0\u3059\u308B\u3068\u304D\u306E\u51E6\u7406\"\n        cnt = self.cnt[x]\n\
    \        self.res += cnt * (cnt - 1) >> 1\n        self.cnt[x] += 1\n\n    def\
    \ delete(self, x):\n        \"\u533A\u9593\u306E\u7AEF\u304B\u3089 x \u3092\u524A\
    \u9664\u3059\u308B\u3068\u304D\u306E\u51E6\u7406\"\n        self.cnt[x] -= 1\n\
    \        cnt = self.cnt[x]\n        self.res -= cnt * (cnt - 1) >> 1\n\n\nN, Q\
    \ = map(int, input().split())\nA = [int(x) for x in input().split()]\nstate =\
    \ MoState(max(A))\nmo = Mo(A, state)\nfor _ in range(Q):\n    l, r = map(int,\
    \ input().split())\n    mo.add_query(l - 1, r)\n\nans = mo.calc()\nprint(*ans,\
    \ sep=\"\\n\")\n"
  dependsOn:
  - data_structure/mo.py
  isVerificationFile: true
  path: test/atcoder/abc200-299/abc293g.test.py
  requiredBy: []
  timestamp: '2024-06-24 17:29:04+09:00'
  verificationStatus: TEST_IGNORED
  verifiedWith: []
documentation_of: test/atcoder/abc200-299/abc293g.test.py
layout: document
redirect_from:
- /verify/test/atcoder/abc200-299/abc293g.test.py
- /verify/test/atcoder/abc200-299/abc293g.test.py.html
title: test/atcoder/abc200-299/abc293g.test.py
---
