---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/string/manacher.test.py
    title: test/library_checker/string/manacher.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def manacher(s):\n    \"\"\"\n    \u3042\u308B\u6587\u5B57\u5217S\u304C\u4E0E\
    \u3048\u3089\u308C\u3066\u3044\u308B\u3068\u3059\u308B\u3002\n    Manacher\u3067\
    \u306F,\u305D\u308C\u305E\u308C\u306Ei\u306B\u3064\u3044\u3066\u6587\u5B57i\u3092\
    \u4E2D\u5FC3\u3068\u3059\u308B\u6700\u9577\u56DE\u6587\u306E\u534A\u5F84\u3092\
    \u8A18\u9332\u3057\u305F\u914D\u5217\u3092\u7DDA\u5F62\u6642\u9593\u3067\u69CB\
    \u7BC9\u3059\u308B\n    \"\"\"\n    if s == \"\":\n        return (0, 1)\n   \
    \ n = len(s)\n    t = \"^#\" + \"#\".join(s) + \"#$\"\n    m = len(t)\n    p =\
    \ [0] * m\n    c, d = 1, 1\n    for i in range(2, m - 1):\n        mirror = 2\
    \ * c - i\n        p[i] = max(0, min(d - i, p[mirror]))\n        while t[i + 1\
    \ + p[i]] == t[i - 1 - p[i]]:\n            p[i] += 1\n        if i + p[i] > d:\n\
    \            c = i\n            d = i + p[i]\n    # p[i]: ^#0#1#2...#n-1#$\u306B\
    \u304A\u3051\u308B\u4F4D\u7F6Ei\u3092\u4E2D\u5FC3\u3068\u3059\u308B\u6700\u9577\
    \u56DE\u5206\u306E\u534A\u5F84\n    # p[2*(i+1)]//2: \u3082\u3068\u306E\u6587\u5B57\
    \u5217\u306Ei\u3092\u4E2D\u5FC3\u3068\u3059\u308B\u6700\u9577\u56DE\u5206\u306E\
    \u534A\u5F84\n    # p[2*(i+1)+1]//2: \u3082\u3068\u306E\u6587\u5B57\u5217\u306E\
    i,i+1\u3092\u4E2D\u5FC3\u3068\u3059\u308B\u6700\u9577\u56DE\u5206\u306E\u534A\u5F84\
    \n    return [p[2 * (i + 1)] // 2 for i in range(n)], [\n        p[2 * (i + 1)\
    \ + 1] // 2 for i in range(n)\n    ]\n    # \u6700\u9577\u56DE\u5206\u306E[s,t)\u304C\
    \u6B32\u3057\u3044\u5834\u5408\n    # k, i = max((p[i], i) for i in range(1, m\
    \ - 1))\n    # return (i - k) // 2, (i + k) // 2\n"
  dependsOn: []
  isVerificationFile: false
  path: string_/manacher.py
  requiredBy: []
  timestamp: '2023-07-23 01:42:59+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/string/manacher.test.py
documentation_of: string_/manacher.py
layout: document
redirect_from:
- /library/string_/manacher.py
- /library/string_/manacher.py.html
title: string_/manacher.py
---
