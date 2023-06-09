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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List\n\n\ndef sa_is(s: List[int], upper: int) -> List[int]:\n\
    \    n = len(s)\n    if n == 0:\n        return []\n    if n == 1:\n        return\
    \ [0]\n    if n == 2:\n        if s[0] < s[1]:\n            return [0, 1]\n  \
    \      else:\n            return [1, 0]\n    sa = [0] * n\n    ls = [0] * n\n\
    \    for i in range(n - 2, -1, -1):\n        ls[i] = ls[i + 1] if (s[i] == s[i\
    \ + 1]) else (s[i] < s[i + 1])\n    sum_l = [0] * (upper + 1)\n    sum_s = [0]\
    \ * (upper + 1)\n    for i in range(n):\n        if not (ls[i]):\n           \
    \ sum_s[s[i]] += 1\n        else:\n            sum_l[s[i] + 1] += 1\n    for i\
    \ in range(upper + 1):\n        sum_s[i] += sum_l[i]\n        if i < upper:\n\
    \            sum_l[i + 1] += sum_s[i]\n\n    def induce(lms):\n        for i in\
    \ range(n):\n            sa[i] = -1\n        buf = sum_s[:]\n        for d in\
    \ lms:\n            if d == n:\n                continue\n            sa[buf[s[d]]]\
    \ = d\n            buf[s[d]] += 1\n        buf = sum_l[:]\n        sa[buf[s[n\
    \ - 1]]] = n - 1\n        buf[s[n - 1]] += 1\n        for i in range(n):\n   \
    \         v = sa[i]\n            if v >= 1 and not (ls[v - 1]):\n            \
    \    sa[buf[s[v - 1]]] = v - 1\n                buf[s[v - 1]] += 1\n        buf\
    \ = sum_l[:]\n        for i in range(n - 1, -1, -1):\n            v = sa[i]\n\
    \            if v >= 1 and ls[v - 1]:\n                buf[s[v - 1] + 1] -= 1\n\
    \                sa[buf[s[v - 1] + 1]] = v - 1\n\n    lms_map = [-1] * (n + 1)\n\
    \    m = 0\n    for i in range(1, n):\n        if not (ls[i - 1]) and ls[i]:\n\
    \            lms_map[i] = m\n            m += 1\n    lms = []\n    for i in range(1,\
    \ n):\n        if not (ls[i - 1]) and ls[i]:\n            lms.append(i)\n    induce(lms)\n\
    \    if m:\n        sorted_lms = []\n        for v in sa:\n            if lms_map[v]\
    \ != -1:\n                sorted_lms.append(v)\n        rec_s = [0] * m\n    \
    \    rec_upper = 0\n        rec_s[lms_map[sorted_lms[0]]] = 0\n        for i in\
    \ range(1, m):\n            l = sorted_lms[i - 1]\n            r = sorted_lms[i]\n\
    \            end_l = lms[lms_map[l] + 1] if (lms_map[l] + 1 < m) else n\n    \
    \        end_r = lms[lms_map[r] + 1] if (lms_map[r] + 1 < m) else n\n        \
    \    same = True\n            if end_l - l != end_r - r:\n                same\
    \ = False\n            else:\n                while l < end_l:\n             \
    \       if s[l] != s[r]:\n                        break\n                    l\
    \ += 1\n                    r += 1\n                if (l == n) or (s[l] != s[r]):\n\
    \                    same = False\n            if not (same):\n              \
    \  rec_upper += 1\n            rec_s[lms_map[sorted_lms[i]]] = rec_upper\n   \
    \     rec_sa = sa_is(rec_s, rec_upper)\n        for i in range(m):\n         \
    \   sorted_lms[i] = lms[rec_sa[i]]\n        induce(sorted_lms)\n    return sa\n\
    \n\ndef suffix_array_upper(s: List[int], upper: int) -> List[int]:\n    assert\
    \ 0 <= upper\n    for d in s:\n        assert 0 <= d and d <= upper\n    return\
    \ sa_is(s, upper)\n\n\ndef suffix_array(s: str) -> List[int]:\n    n = len(s)\n\
    \    if type(s) == str:\n        s2 = [ord(i) for i in s]\n        return sa_is(s2,\
    \ 255)\n    else:\n        idx = list(range(n))\n        idx.sort(key=lambda x:\
    \ s[x])\n        s2 = [0] * n\n        now = 0\n        for i in range(n):\n \
    \           if i & s[idx[i - 1]] != s[idx[i]]:\n                now += 1\n   \
    \         s2[idx[i]] = now\n        return sa_is(s2, now)\n"
  dependsOn: []
  isVerificationFile: false
  path: string/suffix_array.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: string/suffix_array.py
layout: document
redirect_from:
- /library/string/suffix_array.py
- /library/string/suffix_array.py.html
title: string/suffix_array.py
---