---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: atcoder/_scc.py
    title: atcoder/_scc.py
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
  code: "import typing\n\nimport atcoder._scc\n\n\nclass TwoSAT:\n    '''\n    2-SAT\n\
    \n    Reference:\n    B. Aspvall, M. Plass, and R. Tarjan,\n    A Linear-Time\
    \ Algorithm for Testing the Truth of Certain Quantified Boolean\n    Formulas\n\
    \    '''\n\n    def __init__(self, n: int = 0) -> None:\n        self._n = n\n\
    \        self._answer = [False] * n\n        self._scc = atcoder._scc.SCCGraph(2\
    \ * n)\n\n    def add_clause(self, i: int, f: bool, j: int, g: bool) -> None:\n\
    \        assert 0 <= i < self._n\n        assert 0 <= j < self._n\n\n        self._scc.add_edge(2\
    \ * i + (0 if f else 1), 2 * j + (1 if g else 0))\n        self._scc.add_edge(2\
    \ * j + (0 if g else 1), 2 * i + (1 if f else 0))\n\n    def satisfiable(self)\
    \ -> bool:\n        scc_id = self._scc.scc_ids()[1]\n        for i in range(self._n):\n\
    \            if scc_id[2 * i] == scc_id[2 * i + 1]:\n                return False\n\
    \            self._answer[i] = scc_id[2 * i] < scc_id[2 * i + 1]\n        return\
    \ True\n\n    def answer(self) -> typing.List[bool]:\n        return self._answer\n"
  dependsOn:
  - atcoder/_scc.py
  isVerificationFile: false
  path: atcoder/twosat.py
  requiredBy: []
  timestamp: '2024-02-05 08:23:41+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: atcoder/twosat.py
layout: document
redirect_from:
- /library/atcoder/twosat.py
- /library/atcoder/twosat.py.html
title: atcoder/twosat.py
---
