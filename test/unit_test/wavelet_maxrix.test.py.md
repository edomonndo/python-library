---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    IGNORE: ''
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: IGNORE\n\nfrom data_structure.wavelet_matrix import\
    \ WaveletMatrix\n\nif __name__ == \"__main__\":\n    T = [5, 4, 5, 5, 2, 1, 5,\
    \ 6, 1, 3, 5, 0]\n    WM = WaveletMatrix(T)\n\n    assert WM.n == len(T)\n   \
    \ assert WM.A == T\n\n    # access\n    for i, t in enumerate(T):\n        assert\
    \ t == WM.access(i), (t, WM.access(i))\n        assert t == WM.accessFromB(i),\
    \ (t, WM.accessFromB(i))\n\n    # rank\n    for l in range(len(T)):\n        for\
    \ r in range(l + 1, len(T)):\n            for t in T:\n                greedy_rank\
    \ = T[l:r].count(t)\n                assert greedy_rank == WM.rank(l, r, t), (\n\
    \                    (l, r, t),\n                    greedy_rank,\n          \
    \          WM.rank(l, r, t),\n                )\n\n    # select\n    def greedy_select(t,\
    \ k):\n        cnt = 0\n        for i, a in enumerate(T):\n            if a ==\
    \ t:\n                if cnt == k:\n                    return i\n           \
    \     cnt += 1\n        return -1\n\n    for t in set(T):\n        for k in range(T.count(t)):\n\
    \            assert greedy_select(t, k) == WM.select(t, k), (\n              \
    \  (t, k),\n                greedy_select(t, k),\n                WM.select(t,\
    \ k),\n            )\n\n    # quantile\n    def greedy_quantile(l, r, k):\n  \
    \      return sorted(T[l:r])[k]\n\n    for l in range(len(T)):\n        for r\
    \ in range(l + 1, len(T) + 1):\n            for k in range(r - l):\n         \
    \       assert greedy_quantile(l, r, k) == WM.quantile(l, r, k), (\n         \
    \           (l, r, k),\n                    greedy_quantile(l, r, k),\n      \
    \              WM.quantile(l, r, k),\n                )\n\n    # quantilerange\n\
    \    def greedy_quantilerange(l, r, k):\n        arr = sorted(T[l:r])\n      \
    \  val = arr[k]\n        num = arr[: k + 1].count(val)\n        cnt = 0\n    \
    \    for i, t in enumerate(T[l:r]):\n            if t == val:\n              \
    \  cnt += 1\n                if cnt == num:\n                    idx = i\n   \
    \                 break\n        return idx + l\n\n    for l in range(len(T)):\n\
    \        for r in range(l + 1, len(T) + 1):\n            for k in range(r - l):\n\
    \                assert greedy_quantilerange(l, r, k) == WM.quantilerange(l, r,\
    \ k), (\n                    (l, r, k),\n                    greedy_quantilerange(l,\
    \ r, k),\n                    WM.quantilerange(l, r, k),\n                )\n\n\
    \    # maxrange, minrange\n    def greedy_maxrange(l, r):\n        max_value =\
    \ max(T[l:r])\n        idx = -1\n        for i, t in enumerate(T[l:r]):\n    \
    \        if t == max_value:\n                idx = i\n        return idx + l\n\
    \n    def greedy_minrange(l, r):\n        min_value = min(T[l:r])\n        idx\
    \ = -1\n        for i, t in enumerate(T[l:r]):\n            if t == min_value:\n\
    \                idx = i\n                break\n        return idx + l\n\n  \
    \  for l in range(len(T)):\n        for r in range(l + 1, len(T) + 1):\n     \
    \       assert greedy_maxrange(l, r) == WM.maxrange(l, r), (\n               \
    \ (l, r),\n                greedy_maxrange(l, r),\n                WM.maxrange(l,\
    \ r),\n            )\n            assert greedy_minrange(l, r) == WM.minrange(l,\
    \ r), (\n                (l, r),\n                greedy_minrange(l, r),\n   \
    \             WM.minrange(l, r),\n            )\n\n    # topk\n    def greedy_topk(l,\
    \ r, k):\n        dic = dict()\n        for t in T[l:r]:\n            if t in\
    \ dic:\n                dic[t] += 1\n            else:\n                dic[t]\
    \ = 1\n        res = []\n        for key, value in sorted(dic.items(), key=lambda\
    \ x: (-x[1], x[0])):\n            res.append((key, value))\n        return res[:k]\n\
    \n    for l in range(len(T)):\n        for r in range(l + 1, len(T) + 1):\n  \
    \          for k in range(1, r - l + 1):\n                assert greedy_topk(l,\
    \ r, k) == WM.topk(l, r, k), (\n                    (l, r, k),\n             \
    \       greedy_topk(l, r, k),\n                    WM.topk(l, r, k),\n       \
    \         )\n\n    # rangesum\n    def greedy_rangesum(l, r):\n        return\
    \ sum(T[l:r])\n\n    for l in range(len(T)):\n        for r in range(l + 1, len(T)\
    \ + 1):\n            assert greedy_rangesum(l, r) == WM.rangesum(l, r)\n\n   \
    \ # intersect\n    def greedy_intersect(l1, r1, l2, r2):\n        S1 = set(T[l1:r1])\n\
    \        S2 = set(T[l2:r2])\n        S = S1 & S2\n        res = []\n        for\
    \ s in S:\n            t1 = T[l1:r1].count(s)\n            t2 = T[l2:r2].count(s)\n\
    \            res.append((s, t1, t2))\n        return res\n\n    for l1 in range(len(T)):\n\
    \        for r1 in range(l + 1, len(T) + 1):\n            for l2 in range(len(T)):\n\
    \                for r2 in range(l + 1, len(T) + 1):\n                    assert\
    \ greedy_intersect(l1, r1, l2, r2) == WM.intersect(\n                        l1,\
    \ r1, l2, r2\n                    ), (\n                        (l1, r1, l2, r2),\n\
    \                        greedy_intersect(l1, r1, l2, r2),\n                 \
    \       WM.intersect(l1, r1, l2, r2),\n                    )\n\n    # rangefreq_to,\
    \ rangefreq\n    def greedy_rangefreq_to(l, r, value):\n        return len([t\
    \ for t in T[l:r] if 0 <= t < value])\n\n    def greedy_rangefreq(l, r, x, y):\n\
    \        return len([t for t in T[l:r] if x <= t < y])\n\n    for l in range(len(T)):\n\
    \        for r in range(l + 1, len(T) + 1):\n            for y in range(max(T)\
    \ + 2):\n                assert greedy_rangefreq_to(l, r, y) == WM.rangefreq_to(l,\
    \ r, y)\n                for x in range(0, y):\n                    assert greedy_rangefreq(l,\
    \ r, x, y) == WM.rangefreq(l, r, x, y)\n\n    # prevvalue, nextvalue (Not verified)\n\
    \    def greedy_prevvalue(l, r, x, y):\n        try:\n            res = max(t\
    \ for t in T[l:r] if x <= t < y)\n        except ValueError:\n            res\
    \ = -1\n        return res\n\n    def greedy_nextvalue(l, r, x, y):\n        try:\n\
    \            res = min(t for t in T[l:r] if x <= t < y)\n        except ValueError:\n\
    \            res = -1\n        return res\n\n    for l in range(len(T)):\n   \
    \     for r in range(l + 1, len(T) + 1):\n            for x in range(max(T)):\n\
    \                for y in range(x + 1, max(T) + 2):\n                    assert\
    \ greedy_prevvalue(l, r, x, y) == WM.prevvalue(l, r, x, y), (\n              \
    \          (l, r, x, y),\n                        greedy_prevvalue(l, r, x, y),\n\
    \                        WM.prevvalue(l, r, x, y),\n                    )\n  \
    \                  assert greedy_nextvalue(l, r, x, y) == WM.nextvalue(l, r, x,\
    \ y), (\n                        (l, r, x, y),\n                        greedy_nextvalue(l,\
    \ r, x, y),\n                        WM.nextvalue(l, r, x, y),\n             \
    \       )\n"
  dependsOn: []
  isVerificationFile: true
  path: test/unit_test/wavelet_maxrix.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/unit_test/wavelet_maxrix.test.py
layout: document
redirect_from:
- /verify/test/unit_test/wavelet_maxrix.test.py
- /verify/test/unit_test/wavelet_maxrix.test.py.html
title: test/unit_test/wavelet_maxrix.test.py
---
