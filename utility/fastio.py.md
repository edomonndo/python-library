---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/scc_incremental.test.py
    title: Strongly Connected Components (Incremental)
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import atexit\nimport os\nimport sys\n\n\nclass Fastio:\n    def __init__(self):\n\
    \        self.ibuf = bytes()\n        self.obuf = []\n        self.pil = 0\n \
    \       self.pir = 0\n        atexit.register(self.flush)\n        sys.stdin,\
    \ sys.stdout = None, None\n\n    def load(self):\n        self.ibuf = self.ibuf[self.pil\
    \ :]\n        self.ibuf += os.read(0, 131072)\n        self.pil = 0\n        self.pir\
    \ = len(self.ibuf)\n\n    def flush(self):\n        os.write(1, \"\".join(self.obuf).encode())\n\
    \n    def read(self):\n        if self.pir - self.pil < 64:\n            self.load()\n\
    \        minus = 0\n        x = 0\n        while self.ibuf[self.pil] < 45:\n \
    \           self.pil += 1\n        if self.ibuf[self.pil] == 45:\n           \
    \ minus = 1\n            self.pil += 1\n        while self.pil < len(self.ibuf)\
    \ and self.ibuf[self.pil] >= 48:\n            x = x * 10 + (self.ibuf[self.pil]\
    \ & 15)\n            self.pil += 1\n        if minus:\n            x = -x\n  \
    \      return x\n\n    def read_list(self, n: int):\n        return [self.read()\
    \ for _ in range(n)]\n\n    def write(self, x):\n        self.obuf.append(str(x))\n\
    \n    def writeln(self, x):\n        self.obuf.append(str(x) + \"\\n\")\n\n  \
    \  def write_list(self, a):\n        for i in range(len(a)):\n            if i:\n\
    \                self.obuf.append(\" \")\n            self.obuf.append(str(a[i]))\n\
    \        self.obuf.append(\"\\n\")\n"
  dependsOn: []
  isVerificationFile: false
  path: utility/fastio.py
  requiredBy: []
  timestamp: '2024-09-10 07:48:24+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/scc_incremental.test.py
documentation_of: utility/fastio.py
layout: document
title: "\u9AD8\u901F\u5165\u51FA\u529B"
---
