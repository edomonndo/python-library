---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/associative_array
    links:
    - https://judge.yosupo.jp/problem/associative_array
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.12/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.12/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/associative_array\n\
    \nimport sys\n\ninput = sys.stdin.readline\n\nQ = int(input())\ndic = dict()\n\
    for _ in range(Q):\n    # \u30A4\u30F3\u30D7\u30C3\u30C8\u3092\u6574\u6570\u306B\
    \u5909\u63DB\u3059\u308B\u3068TLE\u306B\u306A\u308B.str\u306E\u307E\u307E\u306E\
    \u65B9\u304C\u901F\u3044.\n    query = input().split()\n    if query[0] == \"\
    0\":\n        k, v = query[1], query[2]\n        dic[k] = v\n    elif query[0]\
    \ == \"1\":\n        k = query[1]\n        if k in dic:\n            print(dic[k])\n\
    \        else:\n            print(\"0\")\n"
  dependsOn: []
  isVerificationFile: true
  path: test/library_checker/data_structure/associative_array.test.py
  requiredBy: []
  timestamp: '2023-08-06 23:53:12+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/associative_array.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/associative_array.test.py
- /verify/test/library_checker/data_structure/associative_array.test.py.html
title: test/library_checker/data_structure/associative_array.test.py
---
