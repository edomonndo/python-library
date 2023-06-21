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
  code: "from typing import List\n\n\ndef z_algorithm(s: str) -> List[int]:\n    n\
    \ = len(s)\n    if n == 0:\n        return []\n    z = [0] * n\n    i = 1\n  \
    \  j = 0\n    while i < n:\n        z[i] = 0 if (j + z[j] <= i) else min(j + z[j]\
    \ - i, z[i - j])\n        while (i + z[i] < n) and (s[z[i]] == s[i + z[i]]):\n\
    \            z[i] += 1\n        if j + z[j] < i + z[i]:\n            j = i\n \
    \       i += 1\n    z[0] = n\n    return z\n"
  dependsOn: []
  isVerificationFile: false
  path: string_/z_algorithm.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: string_/z_algorithm.py
layout: document
redirect_from:
- /library/string_/z_algorithm.py
- /library/string_/z_algorithm.py.html
title: string_/z_algorithm.py
---
