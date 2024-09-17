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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import random\n\n\nclass RandomSet:\n    \"\"\"0\u4EE5\u4E0An\u672A\u6E80\
    \u306E\u6574\u6570\u3092\u96C6\u5408\u3067\u7BA1\u7406\u3059\u308B. \u96C6\u5408\
    \u306B\u542B\u307E\u308C\u308B\u6574\u6570\u3092\u30E9\u30F3\u30C0\u30E0\u3067\
    \u51FA\u529B\u3059\u308B.\"\"\"\n\n    def __init__(self, n: int):\n        \"\
    \"\"\u96C6\u5408\u306E\u4E0A\u9650\u5024\u3067\u521D\u671F\u5316.\"\"\"\n    \
    \    self.n = n\n        self.size = 0\n        self.dat = [-1] * n\n        self.idx\
    \ = [-1] * n\n        self.order = []\n\n    def __contains__(self, k: int) ->\
    \ bool:\n        assert 0 <= k < self.n\n        return self.idx[k] != -1\n\n\
    \    def __len__(self) -> int:\n        return self.size\n\n    def __iter__(self):\n\
    \        self.count = 0\n        if len(self.order) != self.size:\n          \
    \  self.order = [x for x in range(self.size)]\n        random.shuffle(self.order)\n\
    \        return self\n\n    def __next__(self):\n        self.count += 1\n   \
    \     if self.count > self.size:\n            raise StopIteration\n        return\
    \ self.dat[self.order[self.count - 1]]\n\n    def __str__(self) -> str:\n    \
    \    return f\"{self.__class__.__name__}({self.dat[:self.size]})\"\n\n    def\
    \ __repr__(self) -> str:\n        return f\"{self.__class__.__name__}(n={self.n},\
    \ size={self.size}, dat={self.dat}, idx={self.idx})\"\n\n    def add(self, k:\
    \ int) -> bool:\n        \"\"\"\u96C6\u5408\u306B\u8981\u7D20k\u3092\u8FFD\u52A0\
    .\"\"\"\n        assert 0 <= k < self.n\n        if self.idx[k] == -1:\n     \
    \       self.idx[k] = self.size\n            self.dat[self.size] = k\n       \
    \     self.size += 1\n            return True\n        return False\n\n    def\
    \ remove(self, k: int) -> bool:\n        \"\"\"\u96C6\u5408\u304B\u3089\u8981\u7D20\
    k\u3092\u524A\u9664.\"\"\"\n        assert 0 <= k < self.n\n        if self.idx[k]\
    \ != -1:\n            last = self.dat[self.size - 1]\n            self.dat[self.idx[k]]\
    \ = last\n            self.idx[last] = self.idx[k]\n            self.idx[k] =\
    \ -1\n            self.dat[self.size - 1] = -1\n            self.size -= 1\n \
    \           return True\n        return False\n\n    def get(self) -> int:\n \
    \       \"\"\"\u96C6\u5408\u304B\u3089\u30E9\u30F3\u30C0\u30E0\u306B\u8981\u7D20\
    \u3092\u53D6\u5F97.\"\"\"\n        assert self.size > 0\n        return self.dat[random.randrange(0,\
    \ self.size)]\n\n    def pop(self) -> int:\n        \"\"\"\u96C6\u5408\u304B\u3089\
    \u30E9\u30F3\u30C0\u30E0\u306B\u8981\u7D20\u3092\u53D6\u5F97\u3057,\u96C6\u5408\
    \u304B\u3089\u524A\u9664.\"\"\"\n        assert self.size > 0\n        k = self.get()\n\
    \        self.remove(k)\n        return k\n"
  dependsOn: []
  isVerificationFile: false
  path: other/random_set.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: other/random_set.py
layout: document
redirect_from:
- /library/other/random_set.py
- /library/other/random_set.py.html
title: other/random_set.py
---
