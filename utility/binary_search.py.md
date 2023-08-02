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
  code: "def is_ok(arg):\n    pass\n\n\ndef binary_search(ng, ok):\n    \"\"\"\n \
    \   \u521D\u671F\u5024\u306Eng,ok\u3092\u53D7\u3051\u53D6\u308A,is_ok\u3092\u6E80\
    \u305F\u3059\u6700\u5C0F(\u6700\u5927)\u306Eok\u3092\u8FD4\u3059\n    ng ok \u306F\
    \  \u3068\u308A\u5F97\u308B\u6700\u5C0F\u306E\u5024-1 \u3068\u308A\u5F97\u308B\
    \u6700\u5927\u306E\u5024+1\n    \u6700\u5927\u6700\u5C0F\u304C\u9006\u306E\u5834\
    \u5408\u306F\u3088\u3057\u306A\u306B\u3072\u3063\u304F\u308A\u8FD4\u3059\n   \
    \ \"\"\"\n    while abs(ok - ng) > 1:\n        mid = (ok + ng) // 2\n        if\
    \ is_ok(mid):\n            ok = mid\n        else:\n            ng = mid\n   \
    \ return ok\n"
  dependsOn: []
  isVerificationFile: false
  path: utility/binary_search.py
  requiredBy: []
  timestamp: '2023-07-23 00:15:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: utility/binary_search.py
layout: document
title: "\u4E8C\u5206\u6CD5"
---

