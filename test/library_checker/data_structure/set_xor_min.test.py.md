---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/binary_trie.py
    title: "\u30D0\u30A4\u30CA\u30EA\u30C8\u30E9\u30A4\u6728"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/set_xor_min
    links:
    - https://judge.yosupo.jp/problem/set_xor_min
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/set_xor_min\n\
    \nfrom data_structure.binary_trie import BinaryTrie\n\nq = int(input())\nbt =\
    \ BinaryTrie()\nfor _ in range(q):\n    t, x = map(int, input().split())\n   \
    \ if t == 0:\n        bt.add(x)\n    elif t == 1:\n        bt.remove(x)\n    else:\n\
    \        print(bt.xor_min(x) ^ x)\n"
  dependsOn:
  - data_structure/binary_trie.py
  isVerificationFile: true
  path: test/library_checker/data_structure/set_xor_min.test.py
  requiredBy: []
  timestamp: '2024-02-09 16:12:14+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/set_xor_min.test.py
layout: document
title: Set Xor-Min
---