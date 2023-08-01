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
  code: "def convex_hull(xy, multi=False):\n    xy.sort(key=lambda x: (x[1], x[0]))\n\
    \    res = []\n\n    def cross3(a, b, c):\n        return (b[0] - a[0]) * (c[1]\
    \ - a[1]) - (b[1] - a[1]) * (c[0] - a[0])\n\n    if multi:\n\n        def f(a,\
    \ b, c):\n            return cross3(a, b, c) > 0\n\n    else:\n\n        def f(a,\
    \ b, c):\n            return cross3(a, b, c) >= 0\n\n    for p in xy:\n      \
    \  while len(res) > 1 and f(res[-1], res[-2], p):\n            res.pop()\n   \
    \     res.append(p)\n\n    le = len(res)\n    for p in xy[::-1][1:]:\n       \
    \ while len(res) > le and f(res[-1], res[-2], p):\n            res.pop()\n   \
    \     res.append(p)\n    res.pop()\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: geometory/convex_full.py
  requiredBy: []
  timestamp: '2023-08-01 14:51:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: geometory/convex_full.py
layout: document
redirect_from:
- /library/geometory/convex_full.py
- /library/geometory/convex_full.py.html
title: geometory/convex_full.py
---
