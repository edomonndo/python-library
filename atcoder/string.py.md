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
  code: "import functools\nimport typing\n\n\ndef _sa_naive(s: typing.List[int]) ->\
    \ typing.List[int]:\n    sa = list(range(len(s)))\n    return sorted(sa, key=lambda\
    \ i: s[i:])\n\n\ndef _sa_doubling(s: typing.List[int]) -> typing.List[int]:\n\
    \    n = len(s)\n    sa = list(range(n))\n    rnk = s.copy()\n    tmp = [0] *\
    \ n\n    k = 1\n    while k < n:\n        def cmp(x: int, y: int) -> int:\n  \
    \          if rnk[x] != rnk[y]:\n                return rnk[x] - rnk[y]\n    \
    \        rx = rnk[x + k] if x + k < n else -1\n            ry = rnk[y + k] if\
    \ y + k < n else -1\n            return rx - ry\n        sa.sort(key=functools.cmp_to_key(cmp))\n\
    \        tmp[sa[0]] = 0\n        for i in range(1, n):\n            tmp[sa[i]]\
    \ = tmp[sa[i - 1]] + (1 if cmp(sa[i - 1], sa[i]) else 0)\n        tmp, rnk = rnk,\
    \ tmp\n        k *= 2\n    return sa\n\n\ndef _sa_is(s: typing.List[int], upper:\
    \ int) -> typing.List[int]:\n    threshold_naive = 10\n    threshold_doubling\
    \ = 40\n\n    n = len(s)\n\n    if n == 0:\n        return []\n    if n == 1:\n\
    \        return [0]\n    if n == 2:\n        if s[0] < s[1]:\n            return\
    \ [0, 1]\n        else:\n            return [1, 0]\n\n    if n < threshold_naive:\n\
    \        return _sa_naive(s)\n    if n < threshold_doubling:\n        return _sa_doubling(s)\n\
    \n    sa = [0] * n\n    ls = [False] * n\n    for i in range(n - 2, -1, -1):\n\
    \        if s[i] == s[i + 1]:\n            ls[i] = ls[i + 1]\n        else:\n\
    \            ls[i] = s[i] < s[i + 1]\n\n    sum_l = [0] * (upper + 1)\n    sum_s\
    \ = [0] * (upper + 1)\n    for i in range(n):\n        if not ls[i]:\n       \
    \     sum_s[s[i]] += 1\n        else:\n            sum_l[s[i] + 1] += 1\n    for\
    \ i in range(upper + 1):\n        sum_s[i] += sum_l[i]\n        if i < upper:\n\
    \            sum_l[i + 1] += sum_s[i]\n\n    def induce(lms: typing.List[int])\
    \ -> None:\n        nonlocal sa\n        sa = [-1] * n\n\n        buf = sum_s.copy()\n\
    \        for d in lms:\n            if d == n:\n                continue\n   \
    \         sa[buf[s[d]]] = d\n            buf[s[d]] += 1\n\n        buf = sum_l.copy()\n\
    \        sa[buf[s[n - 1]]] = n - 1\n        buf[s[n - 1]] += 1\n        for i\
    \ in range(n):\n            v = sa[i]\n            if v >= 1 and not ls[v - 1]:\n\
    \                sa[buf[s[v - 1]]] = v - 1\n                buf[s[v - 1]] += 1\n\
    \n        buf = sum_l.copy()\n        for i in range(n - 1, -1, -1):\n       \
    \     v = sa[i]\n            if v >= 1 and ls[v - 1]:\n                buf[s[v\
    \ - 1] + 1] -= 1\n                sa[buf[s[v - 1] + 1]] = v - 1\n\n    lms_map\
    \ = [-1] * (n + 1)\n    m = 0\n    for i in range(1, n):\n        if not ls[i\
    \ - 1] and ls[i]:\n            lms_map[i] = m\n            m += 1\n    lms = []\n\
    \    for i in range(1, n):\n        if not ls[i - 1] and ls[i]:\n            lms.append(i)\n\
    \n    induce(lms)\n\n    if m:\n        sorted_lms = []\n        for v in sa:\n\
    \            if lms_map[v] != -1:\n                sorted_lms.append(v)\n    \
    \    rec_s = [0] * m\n        rec_upper = 0\n        rec_s[lms_map[sorted_lms[0]]]\
    \ = 0\n        for i in range(1, m):\n            left = sorted_lms[i - 1]\n \
    \           right = sorted_lms[i]\n            if lms_map[left] + 1 < m:\n   \
    \             end_l = lms[lms_map[left] + 1]\n            else:\n            \
    \    end_l = n\n            if lms_map[right] + 1 < m:\n                end_r\
    \ = lms[lms_map[right] + 1]\n            else:\n                end_r = n\n\n\
    \            same = True\n            if end_l - left != end_r - right:\n    \
    \            same = False\n            else:\n                while left < end_l:\n\
    \                    if s[left] != s[right]:\n                        break\n\
    \                    left += 1\n                    right += 1\n             \
    \   if left == n or s[left] != s[right]:\n                    same = False\n\n\
    \            if not same:\n                rec_upper += 1\n            rec_s[lms_map[sorted_lms[i]]]\
    \ = rec_upper\n\n        rec_sa = _sa_is(rec_s, rec_upper)\n\n        for i in\
    \ range(m):\n            sorted_lms[i] = lms[rec_sa[i]]\n        induce(sorted_lms)\n\
    \n    return sa\n\n\ndef suffix_array(s: typing.Union[str, typing.List[int]],\n\
    \                 upper: typing.Optional[int] = None) -> typing.List[int]:\n \
    \   '''\n    SA-IS, linear-time suffix array construction\n    Reference:\n  \
    \  G. Nong, S. Zhang, and W. H. Chan,\n    Two Efficient Algorithms for Linear\
    \ Time Suffix Array Construction\n    '''\n\n    if isinstance(s, str):\n    \
    \    return _sa_is([ord(c) for c in s], 255)\n    elif upper is None:\n      \
    \  n = len(s)\n        idx = list(range(n))\n\n        def cmp(left: int, right:\
    \ int) -> int:\n            return typing.cast(int, s[left]) - typing.cast(int,\
    \ s[right])\n\n        idx.sort(key=functools.cmp_to_key(cmp))\n        s2 = [0]\
    \ * n\n        now = 0\n        for i in range(n):\n            if i and s[idx[i\
    \ - 1]] != s[idx[i]]:\n                now += 1\n            s2[idx[i]] = now\n\
    \        return _sa_is(s2, now)\n    else:\n        assert 0 <= upper\n      \
    \  for d in s:\n            assert 0 <= d <= upper\n\n        return _sa_is(s,\
    \ upper)\n\n\ndef lcp_array(s: typing.Union[str, typing.List[int]],\n        \
    \      sa: typing.List[int]) -> typing.List[int]:\n    '''\n    Longest-Common-Prefix\
    \ computation\n    Reference:\n    T. Kasai, G. Lee, H. Arimura, S. Arikawa, and\
    \ K. Park,\n    Linear-Time Longest-Common-Prefix Computation in Suffix Arrays\
    \ and Its\n    Applications\n    '''\n\n    if isinstance(s, str):\n        s\
    \ = [ord(c) for c in s]\n\n    n = len(s)\n    assert n >= 1\n\n    rnk = [0]\
    \ * n\n    for i in range(n):\n        rnk[sa[i]] = i\n\n    lcp = [0] * (n -\
    \ 1)\n    h = 0\n    for i in range(n):\n        if h > 0:\n            h -= 1\n\
    \        if rnk[i] == 0:\n            continue\n        j = sa[rnk[i] - 1]\n \
    \       while j + h < n and i + h < n:\n            if s[j + h] != s[i + h]:\n\
    \                break\n            h += 1\n        lcp[rnk[i] - 1] = h\n\n  \
    \  return lcp\n\n\ndef z_algorithm(s: typing.Union[str, typing.List[int]]) ->\
    \ typing.List[int]:\n    '''\n    Z algorithm\n    Reference:\n    D. Gusfield,\n\
    \    Algorithms on Strings, Trees, and Sequences: Computer Science and\n    Computational\
    \ Biology\n    '''\n\n    if isinstance(s, str):\n        s = [ord(c) for c in\
    \ s]\n\n    n = len(s)\n    if n == 0:\n        return []\n\n    z = [0] * n\n\
    \    j = 0\n    for i in range(1, n):\n        z[i] = 0 if j + z[j] <= i else\
    \ min(j + z[j] - i, z[i - j])\n        while i + z[i] < n and s[z[i]] == s[i +\
    \ z[i]]:\n            z[i] += 1\n        if j + z[j] < i + z[i]:\n           \
    \ j = i\n    z[0] = n\n\n    return z\n"
  dependsOn: []
  isVerificationFile: false
  path: atcoder/string.py
  requiredBy: []
  timestamp: '2024-02-05 08:23:41+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: atcoder/string.py
layout: document
redirect_from:
- /library/atcoder/string.py
- /library/atcoder/string.py.html
title: atcoder/string.py
---
