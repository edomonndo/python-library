---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/assignment.test.py
    title: Assignment Problem
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def hungarian(A: list[list[int]]) -> tuple[int, list[int]]:\n    inf = float(\"\
    inf\")\n    n = len(A)\n    row = [-1] * n\n    col = [-1] * n\n    pi = [0] *\
    \ n\n    residual = lambda i, j: A[i][j] - pi[j]\n    transferrable = 0\n    for\
    \ j in range(n):\n        i = 0\n        for k in range(1, n):\n            if\
    \ A[i][j] > A[k][j]:\n                i = k\n        pi[j] = A[i][j]\n       \
    \ if row[i] == -1:\n            row[i] = j\n            col[j] = i\n         \
    \   transferrable |= 1 << i\n        else:\n            transferrable &= ~(1 <<\
    \ i)\n\n    for i, c in enumerate(row):\n        if (transferrable >> i) & 1 ==\
    \ 0:\n            continue\n        j = -1\n        for k in range(n):\n     \
    \       if k != c and (j == -1 or residual(i, j) > residual(i, k)):\n        \
    \        j = k\n        pi[c] -= residual(i, j)\n\n    for _ in range(2):\n  \
    \      for i in range(n):\n            if row[i] != -1:\n                continue\n\
    \            u1 = residual(i, 0)\n            u2 = inf\n            c1 = 0\n \
    \           for j in range(n):\n                u = residual(i, j)\n         \
    \       if u < u1 or (u == u1 and col[c1] != -1):\n                    u2 = u1\n\
    \                    u1 = u\n                    c1 = j\n                elif\
    \ u < u2:\n                    u2 = u\n            if u1 < u2:\n             \
    \   pi[c1] -= u2 - u1\n            if col[c1] != -1:\n                row[col[c1]]\
    \ = col[c1] = -1\n            row[i] = c1\n            col[c1] = i\n\n    cols\
    \ = [i for i in range(n)]\n    for i in range(n):\n        if row[i] != -1:\n\
    \            continue\n        dist = [residual(i, j) for j in range(n)]\n   \
    \     pred = [i] * n\n\n        def f():\n            scanned = labeled = last\
    \ = 0\n            while True:\n                if scanned == labeled:\n     \
    \               last = scanned\n                    mn = dist[cols[scanned]]\n\
    \                    for j in range(scanned, n):\n                        c =\
    \ cols[j]\n                        if dist[c] <= mn:\n                       \
    \     if dist[c] < mn:\n                                mn = dist[c]\n       \
    \                         labeled = scanned\n                            cols[j],\
    \ cols[labeled] = cols[labeled], cols[j]\n                            labeled\
    \ += 1\n                    for j in range(scanned, labeled):\n              \
    \          if col[cols[j]] == -1:\n                            return cols[j],\
    \ last\n                c1 = cols[scanned]\n                scanned += 1\n   \
    \             r1 = col[c1]\n                for j in range(labeled, n):\n    \
    \                c2 = cols[j]\n                    ln = residual(r1, c2) - residual(r1,\
    \ c1)\n                    if dist[c2] > dist[c1] + ln:\n                    \
    \    dist[c2] = dist[c1] + ln\n                        pred[c2] = r1\n       \
    \                 if ln == 0:\n                            if col[c2] == -1:\n\
    \                                return c2, last\n                           \
    \ cols[j], cols[labeled] = cols[labeled], cols[j]\n                          \
    \  labeled += 1\n\n        c0, last = f()\n        for j, c in enumerate(cols):\n\
    \            if j == last:\n                break\n            pi[c] += dist[c]\
    \ - dist[c0]\n\n        t = c0\n        while t != -1:\n            j = t\n  \
    \          r = pred[j]\n            col[j] = r\n            row[r], t = t, row[r]\n\
    \n    tot = sum(A[i][row[i]] for i in range(n))\n\n    return tot, row\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/hungarian.py
  requiredBy: []
  timestamp: '2024-02-09 16:12:14+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/assignment.test.py
documentation_of: graph/hungarian.py
layout: document
redirect_from:
- /library/graph/hungarian.py
- /library/graph/hungarian.py.html
title: graph/hungarian.py
---
