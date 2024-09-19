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
  code: "def overlap(S: str, T: str) -> int:\n    \"\"\"\n    Get overlapped string\
    \ length by O(min(|S|,|T|)), when 'S','T' -> 'ST'.\n    Algorithm is based on\
    \ z-algorithm.\n    'snuke' + 'kensho' -> 2\n    \"\"\"\n    sn, tn = len(S),\
    \ len(T)\n    if sn == 0 or tn == 0:\n        return 0\n    # S,T\u306F\u77ED\u3044\
    \u65B9\u306E\u9577\u3055\u306B\u5408\u308F\u305B\u308B. S\u306F\u672B\u5C3E, T\u306F\
    \u5148\u982D\u3092\u4FDD\u6301\u3059\u308B.\n    if sn > tn:\n        sn = tn\n\
    \        S = S[-tn:]\n    elif sn < tn:\n        tn = sn\n        T = T[:sn]\n\
    \    n = sn + tn\n    s = [ord(c) for c in (T + S)]\n    # z-algorithm\n    z\
    \ = [0] * n\n    j = 0\n    for i in range(1, n):\n        z[i] = 0 if j + z[j]\
    \ <= i else min(j + z[j] - i, z[i - j])\n        while i + z[i] < n and s[z[i]]\
    \ == s[i + z[i]]:\n            z[i] += 1\n        if j + z[j] < i + z[i]:\n  \
    \          j = i\n    z[0] = n\n    for i in range(sn, 0, -1):\n        # S\u306E\
    \u672B\u5C3Ei\u6587\u5B57\u3068T\u306E\u5148\u982Di\u6587\u5B57\u304C\u5408\u81F4\
    \u3059\u308B\u304B\n        if i == z[-i]:\n            return i\n    return 0\n"
  dependsOn: []
  isVerificationFile: false
  path: str/overlap.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: str/overlap.py
layout: document
title: "\u6587\u5B57\u5217\u9023\u7D50\u6642\u306E\u91CD\u8907"
---

文字列$S$の後ろに文字列$T$を文字の重なり有りで連結するときの最大重複文字数を計算する.
z-algorithmを使用して O(min(|S|,|T|))の計算量である.
'snuke' + 'kensho' -> 2