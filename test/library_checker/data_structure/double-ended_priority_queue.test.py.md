---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: data_structure/SortedMultiset.py
    title: SortedMultiset
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/double_ended_priority_queue
    links:
    - https://judge.yosupo.jp/problem/double_ended_priority_queue
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/double_ended_priority_queue\n\
    \nfrom data_structure.SortedMultiset import SortedMultiset\n\nN, Q = map(int,\
    \ input().split())\nS = list(map(int, input().split()))\n\nMultiSet = SortedMultiset(S)\n\
    \nfor _ in range(Q):\n    query = list(map(int, input().split()))\n    if query[0]\
    \ == 0:\n        MultiSet.add(query[1])\n    elif query[0] == 1:\n        print(MultiSet.pop(0))\n\
    \    elif query[0] == 2:\n        print(MultiSet.pop(-1))\n"
  dependsOn:
  - data_structure/SortedMultiset.py
  isVerificationFile: true
  path: test/library_checker/data_structure/double-ended_priority_queue.test.py
  requiredBy: []
  timestamp: '2023-09-15 09:38:49+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/double-ended_priority_queue.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/double-ended_priority_queue.test.py
- /verify/test/library_checker/data_structure/double-ended_priority_queue.test.py.html
title: test/library_checker/data_structure/double-ended_priority_queue.test.py
---
