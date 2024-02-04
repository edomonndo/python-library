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
  code: "import typing\n\nimport atcoder._scc\n\n\nclass SCCGraph:\n    def __init__(self,\
    \ n: int = 0) -> None:\n        self._internal = atcoder._scc.SCCGraph(n)\n\n\
    \    def add_edge(self, from_vertex: int, to_vertex: int) -> None:\n        n\
    \ = self._internal.num_vertices()\n        assert 0 <= from_vertex < n\n     \
    \   assert 0 <= to_vertex < n\n        self._internal.add_edge(from_vertex, to_vertex)\n\
    \n    def scc(self) -> typing.List[typing.List[int]]:\n        return self._internal.scc()\n"
  dependsOn: []
  isVerificationFile: false
  path: atcoder/scc.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: atcoder/scc.py
layout: document
redirect_from:
- /library/atcoder/scc.py
- /library/atcoder/scc.py.html
title: atcoder/scc.py
---
