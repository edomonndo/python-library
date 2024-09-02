---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/past/past4m_hld.test.py
    title: "M - \u7B46\u5857\u308A"
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/jump_on_tree_hld.test.py
    title: Jump on Tree (HLD)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/vertex_add_path_sum_hld.test.py
    title: Vertex Add Path Sum (HLD)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/vertext_set_path_composite.test.py
    title: Vertex Set Path Composite
  - icon: ':heavy_check_mark:'
    path: "test/yukicoder/235_\u3081\u3050\u308B\u306F\u3081\u3050\u308B(5).test.py"
    title: "No.235 \u3081\u3050\u308B\u306F\u3081\u3050\u308B (5)"
  - icon: ':heavy_check_mark:'
    path: "test/yukicoder/399_\u52D5\u7684\u306A\u9818\u4E3B.test.py"
    title: "No.399 \u52D5\u7684\u306A\u9818\u4E3B"
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Tree:\n    @staticmethod\n    def from_input(n: int, is_1idx: bool\
    \ = False) -> list[list[int]]:\n        res = [[] for _ in range(n)]\n       \
    \ for _ in range(n - 1):\n            u, v = map(int, input().split())\n     \
    \       u -= is_1idx\n            v -= is_1idx\n            res[u].append(v)\n\
    \            res[v].append(u)\n        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/tree/template.py
  requiredBy: []
  timestamp: '2024-09-02 08:53:18+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/past/past4m_hld.test.py
  - "test/yukicoder/235_\u3081\u3050\u308B\u306F\u3081\u3050\u308B(5).test.py"
  - "test/yukicoder/399_\u52D5\u7684\u306A\u9818\u4E3B.test.py"
  - test/library_checker/tree/jump_on_tree_hld.test.py
  - test/library_checker/tree/vertext_set_path_composite.test.py
  - test/library_checker/tree/vertex_add_path_sum_hld.test.py
documentation_of: graph/tree/template.py
layout: document
redirect_from:
- /library/graph/tree/template.py
- /library/graph/tree/template.py.html
title: graph/tree/template.py
---