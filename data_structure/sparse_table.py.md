---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl/dsl_3_d_sliding_minimum_element_st.test.py
    title: DSL3D Sliding Minimum Element (Sparse Table)
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SparseTable:\n    def __init__(self, arr, op):\n        bit_length\
    \ = 0\n        n = len(arr)\n        while (1 << bit_length) <= n:\n         \
    \   bit_length += 1\n        table = [[0] * n for _ in range(bit_length)]\n  \
    \      table[0] = arr[:]\n        for i in range(1, bit_length):\n           \
    \ j = 0\n            while j + (1 << i) <= n:\n                table[i][j] = op(table[i\
    \ - 1][j], table[i - 1][j + (1 << (i - 1))])\n                j += 1\n       \
    \ lookup = [0] * (n + 1)\n        for i in range(2, n + 1):\n            lookup[i]\
    \ = lookup[i >> 1] + 1\n\n        self.n = n\n        self.op = op\n        self.table\
    \ = table\n        self.lookup = lookup\n\n    def query(self, l, r):\n      \
    \  assert 0 <= l and r <= self.n\n        assert l < r\n        b = self.lookup[r\
    \ - l]\n        return self.op(self.table[b][l], self.table[b][r - (1 << b)])"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/sparse_table.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/dsl/dsl_3_d_sliding_minimum_element_st.test.py
documentation_of: data_structure/sparse_table.py
layout: document
title: Sparse table
---

静的な数列の区間に対するクエリを前処理$O(NlogN)$, クエリ$O(1)$で求めます．
Sparse tableに乗せられる演算は半群が条件です．（min, max, xor, gcd, lcmなど） 

### ST = SparseTable(arr, op)

数列$arr$からSparse tableを構築します．$op$は演算です．

### ST.query(l, r)

区間$[l, r)$の演算結果を返します．