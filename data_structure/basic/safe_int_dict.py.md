---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/associative_array.test.py
    title: Assosiative Array
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SafeIntDict(dict):\n    def __init__(self):\n        self.b = 5463325252\n\
    \        super().__init__()\n\n    def __getitem__(self, key):\n        return\
    \ super().__getitem__(key ^ self.b)\n\n    def __setitem__(self, key, value):\n\
    \        super().__setitem__(key ^ self.b, value)\n\n    def __delitem__(self,\
    \ key):\n        return super().__delitem__(key ^ self.b)\n\n    def get(self,\
    \ key, default=None):\n        return super().get(key ^ self.b, default)\n\n \
    \   def pop(self, key, default=None):\n        return super().pop(key ^ self.b,\
    \ default)\n\n    def __contains__(self, key):\n        return super().__contains__(key\
    \ ^ self.b)\n\n    def __repr__(self):\n        return str({k ^ self.b: v for\
    \ k, v in super().items()})\n\n    def __str__(self):\n        return str({k ^\
    \ self.b: v for k, v in super().items()})\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/basic/safe_int_dict.py
  requiredBy: []
  timestamp: '2024-06-07 11:47:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/associative_array.test.py
documentation_of: data_structure/basic/safe_int_dict.py
layout: document
redirect_from:
- /library/data_structure/basic/safe_int_dict.py
- /library/data_structure/basic/safe_int_dict.py.html
title: data_structure/basic/safe_int_dict.py
---
