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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import subprocess\n\n\ndef factorize(s: str) -> list[str]:\n    \"\"\"\n\
    \    Factorize x by Linux command. Note that args s is string.\n    ```\n    $\
    \ factor 12 -> \"b'12: 2 2 3\\r\\n'\"\n    ```\n    \"\"\"\n    x = str(subprocess.check_output(\"\
    factor \" + s, shell=True))\n    return x[x.rfind(\":\") + 2 : -3].split()\n"
  dependsOn: []
  isVerificationFile: false
  path: math_/factorize.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: math_/factorize.py
layout: document
title: "\u7D20\u56E0\u6570\u5206\u89E3"
---

なぜかLinuxのコマンドの方が速い。もちろんLinuxでしか使えない。

### `factorize(s: str)`

$s$を素因数分解する。$s$は**文字列**であることに注意。