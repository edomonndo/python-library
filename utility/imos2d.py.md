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
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def imos2d(H: int, W: int, arr: list[tuple(int, int, int, int)]) -> list[list[int]]:\n\
    \    res = [[0] * (W + 1) for _ in range(H + 1)]\n    for x1, y1, x2, y2 in arr:\n\
    \        res[x1][y1] += 1\n        if x2 + 1 <= H:\n            res[x2 + 1][y1]\
    \ -= 1\n        if y2 + 1 <= W:\n            res[x1][y2 + 1] -= 1\n        if\
    \ x2 + 1 <= H and y2 + 1 <= W:\n            res[x2 + 1][y2 + 1] += 1\n\n    for\
    \ i in range(H):\n        for j in range(W):\n            res[i + 1][j + 1] +=\
    \ res[i][j + 1] + res[i + 1][j] - res[i][j]\n\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: utility/imos2d.py
  requiredBy: []
  timestamp: '2023-12-04 22:53:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: utility/imos2d.py
layout: document
title: "\u4E8C\u6B21\u5143\u7D2F\u7A4D\u548C"
---

### `imos2d(H: int, W: int, arr: list[tuple(int, int, int, int)])`

$H$ x $W$サイズの盤面で長方形の重なりを計算する

$arr$の要素は$a,b,c,d$を持ち， $a,b$は長方形の左上の座標, $c,d$は長方形の右下の座標である.