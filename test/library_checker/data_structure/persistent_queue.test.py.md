---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: persistent_data_structure/persistent_queue.py
    title: "\u6C38\u7D9A\u30AD\u30E5\u30FC"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/persistent_queue
    links:
    - https://judge.yosupo.jp/problem/persistent_queue
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/persistent_queue\n\
    from persistent_data_structure.persistent_queue import PersistentQueue\n\nQ =\
    \ int(input())\nq = PersistentQueue(Q)\nfor _ in range(Q):\n    t, *query = map(int,\
    \ input().split())\n    if t == 0:\n        k, x = query\n        q.append(k,\
    \ x)\n    else:\n        (k,) = query\n        print(q.popleft(k))\n"
  dependsOn:
  - persistent_data_structure/persistent_queue.py
  isVerificationFile: true
  path: test/library_checker/data_structure/persistent_queue.test.py
  requiredBy: []
  timestamp: '2024-02-09 17:45:13+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/persistent_queue.test.py
layout: document
title: Persistent Queue
---
