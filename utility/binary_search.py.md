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
  code: "def bin_search(ng, ok, is_ok):\n    while abs(ok - ng) > 1:\n        md =\
    \ (ok + ng) // 2\n        if is_ok(md):\n            ok = md\n        else:\n\
    \            ng = md\n    return ok\n"
  dependsOn: []
  isVerificationFile: false
  path: utility/binary_search.py
  requiredBy: []
  timestamp: '2024-01-05 12:48:48+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: utility/binary_search.py
layout: document
title: "\u4E8C\u5206\u6CD5"
---

初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す  
ng,okはとり得る最小の値-1 とり得る最大の値+1  
最大最小が逆の場合はよしなにひっくり返す
