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
redirect_from:
- /library/utility/binary_search.py
- /library/utility/binary_search.py.html
title: utility/binary_search.py
---
