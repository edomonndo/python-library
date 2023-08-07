---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: graph/bfs.py
    title: "\u5E45\u512A\u5148\u63A2\u7D22"
  - icon: ':warning:'
    path: graph/maxflow.py
    title: "\u6700\u5927\u30D5\u30ED\u30FC"
  - icon: ':warning:'
    path: graph/toporogical_sort.py
    title: "\u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\u30C8"
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# Dummy class for defaultdict\n\n\nclass defaultdict(dict):\n    def __init__(self,\
    \ func):\n        self.func = func\n\n    def __getitem__(self, item):\n     \
    \   if item not in self:\n            self[item] = self.func()\n        return\
    \ super().__getitem__(item)\n"
  dependsOn: []
  isVerificationFile: false
  path: collections.py
  requiredBy:
  - graph/maxflow.py
  - graph/toporogical_sort.py
  - graph/bfs.py
  timestamp: '2023-08-07 21:41:31+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: collections.py
layout: document
redirect_from:
- /library/collections.py
- /library/collections.py.html
title: collections.py
---
