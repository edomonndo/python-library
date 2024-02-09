---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: persistent_data_structure/persistent_queue.py
    title: persistent_data_structure/persistent_queue.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/persistent_queue
    links:
    - https://judge.yosupo.jp/problem/persistent_queue
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/persistent_queue\n\
    from persistent_data_structure.persistent_queue import PersistentQueue\n\nQ =\
    \ int(input())\nq = PersistentQueue(Q)\nfor _ in range(Q):\n    t, *query = map(int,\
    \ input().split())\n    if t == 0:\n        k, x = query\n        q.append(t,\
    \ x)\n    else:\n        k = query[0]\n        print(q.popleft(t))\n"
  dependsOn:
  - persistent_data_structure/persistent_queue.py
  isVerificationFile: true
  path: test/library_checker/data_structure/persistent_queue.test.py
  requiredBy: []
  timestamp: '2024-02-09 16:12:14+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/data_structure/persistent_queue.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/persistent_queue.test.py
- /verify/test/library_checker/data_structure/persistent_queue.test.py.html
title: test/library_checker/data_structure/persistent_queue.test.py
---
