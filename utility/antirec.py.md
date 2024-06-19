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
  code: "from types import GeneratorType\n\n\ndef antirec(func, stack=[]):\n    def\
    \ wrappedfunc(*args, **kwargs):\n        if stack:\n            return func(*args,\
    \ **kwargs)\n        to = func(*args, **kwargs)\n        while True:\n       \
    \     if isinstance(to, GeneratorType):\n                stack.append(to)\n  \
    \              to = next(to)\n            else:\n                stack.pop()\n\
    \                if not stack:\n                    break\n                to\
    \ = stack[-1].send(to)\n        return to\n\n    return wrappedfunc\n"
  dependsOn: []
  isVerificationFile: false
  path: utility/antirec.py
  requiredBy: []
  timestamp: '2024-06-04 09:09:32+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: utility/antirec.py
layout: document
title: "\u518D\u5E30\u9AD8\u901F\u5316"
---
