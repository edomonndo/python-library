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
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def compress_to_dict(arr):\n    return {e: i for i, e in enumerate(sorted(set(arr)))}\n\
    \n\ndef compress_to_list(arr):\n    # 0-index\n    return list(map({e: i for i,\
    \ e in enumerate(sorted(set(arr)), 0)}.__getitem__, arr))\n\n\ndef compress(arr):\n\
    \    dic = {e: i for i, e in enumerate(sorted(set(arr)))}\n    lst = list(map(dic.__getitem__,\
    \ arr))\n    return dic, lst\n"
  dependsOn: []
  isVerificationFile: false
  path: utility/compress.py
  requiredBy: []
  timestamp: '2023-12-04 22:53:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: utility/compress.py
layout: document
title: "\u5EA7\u6A19\u5727\u7E2E"
---

