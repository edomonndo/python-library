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
  code: "def compress_to_dict(arr):\n    return {e: i for i, e in enumerate(sorted(set(arr)))}\n\
    \n\ndef compress_to_list(arr):\n    # 0-index\n    return list(map({e: i for i,\
    \ e in enumerate(sorted(set(arr)), 0)}.__getitem__, arr))\n\n\ndef compress(arr):\n\
    \    dic = {e: i for i, e in enumerate(sorted(set(arr)))}\n    lst = list(map(dic.__getitem__,\
    \ arr))\n    return dic, lst\n\n\nif __name__ == \"__main__\":\n    # \uFF11\u6B21\
    \u5143\n    A = [4, 90, 25, 30, 30, 8, 90, 90]\n    dic = compress_to_dict(A)\n\
    \    lst = compress_to_list(A)\n    assert dic == {4: 0, 8: 1, 25: 2, 30: 3, 90:\
    \ 4}\n    assert lst == [0, 4, 2, 3, 3, 1, 4, 4], lst\n    assert compress(A)\
    \ == (dic, lst)\n"
  dependsOn: []
  isVerificationFile: false
  path: utility/compress.py
  requiredBy: []
  timestamp: '2023-07-22 14:27:24+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: utility/compress.py
layout: document
redirect_from:
- /library/utility/compress.py
- /library/utility/compress.py.html
title: utility/compress.py
---
