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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def combination_mod(n: int, r: int, mod=10**9 + 7) -> int:\n    num = 1\n\
    \    denom = 1\n    for i in range(r):\n        num = (num * (n - i)) % mod\n\
    \        denom = (denom * (r - i)) % mod\n\n    return num * pow(denom, mod -\
    \ 2, mod)\n"
  dependsOn: []
  isVerificationFile: false
  path: math_/combination_mod.py
  requiredBy: []
  timestamp: '2023-07-05 08:12:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: math_/combination_mod.py
layout: document
redirect_from:
- /library/math_/combination_mod.py
- /library/math_/combination_mod.py.html
title: math_/combination_mod.py
---
