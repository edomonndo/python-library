---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: str/suffix_array.py
    title: Suffix array
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library_checker/string/longeset_common_substring.test.py
    title: test/library_checker/string/longeset_common_substring.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from str.suffix_array import suffix_array, lcp_array\n\n\ndef find_lcs_idx(S:\
    \ str, T: str) -> tuple[int, int, int, int]:\n    n = len(S)\n    S = S + \"_\"\
    \ + T\n    N = len(S)\n    sa = suffix_array(S)\n    lcp = lcp_array(S, sa)\n\n\
    \    m = 0\n    vs = [[] for _ in range(N)]\n    for i in range(N - 1):\n    \
    \    vs[lcp[i]].append(i)\n        if lcp[i] > m and (sa[i] < n) != (sa[i + 1]\
    \ < n):\n            m = lcp[i]\n    if m > 0:\n        for i in vs[m]:\n    \
    \        if (sa[i] < n) != (sa[i + 1] < n):\n                if sa[i] < n:\n \
    \                   return (sa[i], sa[i] + m, sa[i + 1] - n - 1, sa[i + 1] + m\
    \ - n - 1)\n                else:\n                    return (sa[i + 1], sa[i\
    \ + 1] + m, sa[i] - n - 1, sa[i] + m - n - 1)\n    else:\n        return (0, 0,\
    \ 0, 0)\n"
  dependsOn:
  - str/suffix_array.py
  isVerificationFile: false
  path: str/longest_common_substring.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/library_checker/string/longeset_common_substring.test.py
documentation_of: str/longest_common_substring.py
layout: document
title: Longest Common Substring
---

文字列$S, T$の最長共通文字列を求める．
返り値は，$si, sj, ti, tj$. ここで$S[si: sj], T[ti: tj]$が最長共通文字列となる.