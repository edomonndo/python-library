---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/basic/safe_int_dict.py
    title: Safe Int Dict
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/associative_array
    links:
    - https://judge.yosupo.jp/problem/associative_array
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/associative_array\n\
    \nfrom data_structure.basic.safe_int_dict import SafeIntDict\n\nq = int(input())\n\
    dic = SafeIntDict()\nfor _ in range(q):\n    # \u30A4\u30F3\u30D7\u30C3\u30C8\u3092\
    \u6574\u6570\u306B\u5909\u63DB\u3059\u308B\u3068TLE\u306B\u306A\u308B.str\u306E\
    \u307E\u307E\u306E\u65B9\u304C\u901F\u3044.\n    t, *qu = map(int, input().split())\n\
    \    if t == 0:\n        k, v = qu\n        dic[k] = v\n    else:\n        k =\
    \ qu[0]\n        if k in dic:\n            print(dic[k])\n        else:\n    \
    \        print(\"0\")\n"
  dependsOn:
  - data_structure/basic/safe_int_dict.py
  isVerificationFile: true
  path: test/library_checker/data_structure/associative_array.test.py
  requiredBy: []
  timestamp: '2024-06-07 11:47:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/associative_array.test.py
layout: document
title: Assosiative Array
---
