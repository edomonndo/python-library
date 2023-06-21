---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: library_checker/matrix/matrix_det.test.py
    title: library_checker/matrix/matrix_det.test.py
  - icon: ':heavy_check_mark:'
    path: library_checker/matrix/matrix_det_arbitrary_mod.test.py
    title: library_checker/matrix/matrix_det_arbitrary_mod.test.py
  - icon: ':x:'
    path: library_checker/matrix/matrix_inverse.test.py
    title: library_checker/matrix/matrix_inverse.test.py
  - icon: ':x:'
    path: library_checker/matrix/matrix_product.test.py
    title: library_checker/matrix/matrix_product.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Matrix:\n    MOD = 998244353\n\n    def __init__(self, n, m, mat=None):\n\
    \        self.n = n\n        self.m = m\n        self.mat = [[0] * self.m for\
    \ _ in range(self.n)]\n        if mat:\n            assert len(mat) == n and len(mat[0])\
    \ == m\n            for i in range(self.n):\n                self.mat[i] = mat[i].copy()\n\
    \n    def __getitem__(self, key):\n        if isinstance(key, slice):\n      \
    \      return self.mat[key]\n        else:\n            assert key >= 0\n    \
    \        return self.mat[key]\n\n    def __len__(self):\n        return len(self.mat)\n\
    \n    def __str__(self):\n        return \"\\n\".join(\" \".join(map(str, self[i]))\
    \ for i in range(self.n))\n\n    def __pos__(self):\n        return self\n\n \
    \   def __neg__(self):\n        return self.times(-1)\n\n    def __add__(self,\
    \ other):\n        assert self.n == other.n and self.m == other.m\n        res\
    \ = [[0] * self.m for _ in range(self.n)]\n        for i in range(self.n):\n \
    \           res_i, self_i, other_i = res[i], self[i], other[i]\n            for\
    \ j in range(self.m):\n                res_i[j] = (self_i[j] + other_i[j]) % self.MOD\n\
    \        return Matrix(self.n, self.m, res)\n\n    def __sub__(self, other):\n\
    \        assert self.n == other.n and self.m == other.m\n        res = [[0] *\
    \ self.m for _ in range(self.n)]\n        for i in range(self.n):\n          \
    \  res_i, self_i, other_i = res[i], self[i], other[i]\n            for j in range(self.m):\n\
    \                res_i[j] = (self_i[j] - other_i[j]) % self.MOD\n        return\
    \ Matrix(self.n, self.m, res)\n\n    def __mul__(self, other):\n        if other.__class__\
    \ == Matrix:\n            assert self.m == other.n\n            res = [[0] * other.m\
    \ for _ in range(self.n)]\n            for i in range(self.n):\n             \
    \   res_i, self_i = res[i], self[i]\n                for k in range(self.m):\n\
    \                    self_ik, other_k = self_i[k], other[k]\n                \
    \    for j in range(other.m):\n                        res_i[j] += self_ik * other_k[j]\n\
    \                        res_i[j] %= self.MOD\n            return Matrix(self.n,\
    \ other.m, res)\n        else:\n            return self.times(other)\n\n    def\
    \ __rmul__(self, other):\n        return self.times(other)\n\n    def __pow__(self,\
    \ k):\n        assert self.is_square()\n        tmp = Matrix(self.n, self.n, self.mat)\n\
    \        res = Matrix.id(self.n)\n        while k:\n            if k & 1:\n  \
    \              res *= tmp\n            tmp *= tmp\n            k >>= 1\n     \
    \   return res\n\n    def is_square(self):\n        return self.n == self.m\n\n\
    \    def id(n):\n        res = Matrix(n, n)\n        for i in range(n):\n    \
    \        res[i][i] = 1\n        return res\n\n    def times(self, k):\n      \
    \  res = [[0] * self.m for _ in range(self.n)]\n        for i in range(self.n):\n\
    \            res_i, res_j = res[i], self[i]\n            for j in range(self.m):\n\
    \                res_i[j] = k * self_i[j] % self.MOD\n        return Matrix(self.n,\
    \ self.m, res)\n\n    def linear_equations(self, vec):\n        assert self.n\
    \ == len(vec)\n        aug = [self[i] + [vec[i]] for i in range(self.n)]\n   \
    \     rank = 0\n        p = []\n        q = []\n        for j in range(self.m\
    \ + 1):\n            for i in range(rank, self.n):\n                if aug[i][j]\
    \ != 0:\n                    break\n            else:\n                q.append(j)\n\
    \                continue\n            if j == self.m:\n                return\
    \ -1, [], []\n            p.append(j)\n            aug[rank], aug[i] = aug[i],\
    \ aug[rank]\n            inv = pow(aug[rank][j], self.MOD - 2, self.MOD)\n   \
    \         aug_rank = aug[rank]\n            for k in range(self.m + 1):\n    \
    \            aug_rank[k] *= inv\n                aug_rank[k] %= self.MOD\n   \
    \         for i in range(self.n):\n                if i == rank:\n           \
    \         continue\n                aug_i = aug[i]\n                c = -aug_i[j]\n\
    \                for k in range(self.m + 1):\n                    aug_i[k] +=\
    \ c * aug_rank[k]\n                    aug_i[k] %= self.MOD\n            rank\
    \ += 1\n        dim = self.m - rank\n        sol = [0] * self.m\n        for i\
    \ in range(rank):\n            sol[p[i]] = aug[i][-1]\n        vecs = [[0] * self.m\
    \ for _ in range(dim)]\n        for i in range(dim):\n            vecs[i][q[i]]\
    \ = 1\n        for i in range(dim):\n            vecs_i = vecs[i]\n          \
    \  for j in range(rank):\n                vecs_i[p[j]] = -aug[j][q[i]] % self.MOD\n\
    \        return dim, sol, vecs\n\n    def determinant(self):\n        assert self.is_square()\n\
    \        res = 1\n        tmp = Matrix(self.n, self.n, self.mat)\n        for\
    \ j in range(self.n):\n            if tmp[j][j] == 0:\n                for i in\
    \ range(j + 1, self.n):\n                    if tmp[i][j] != 0:\n            \
    \            break\n                else:\n                    return 0\n    \
    \            tmp.mat[j], tmp.mat[i] = tmp.mat[i], tmp.mat[j]\n               \
    \ res *= -1\n            tmp_j = tmp[j]\n            inv = pow(tmp_j[j], self.MOD\
    \ - 2, self.MOD)\n            for i in range(j + 1, self.n):\n               \
    \ tmp_i = tmp[i]\n                c = -inv * tmp_i[j] % self.MOD\n           \
    \     for k in range(self.n):\n                    tmp_i[k] += c * tmp_j[k]\n\
    \                    tmp_i[k] %= self.MOD\n        for i in range(self.n):\n \
    \           res *= tmp[i][i]\n            res %= self.MOD\n        return res\n\
    \n    def inverse(self):\n        assert self.is_square()\n        res = Matrix.id(self.n)\n\
    \        tmp = Matrix(self.n, self.n, self.mat)\n        for j in range(self.n):\n\
    \            if tmp[j][j] == 0:\n                for i in range(j + 1, self.n):\n\
    \                    if tmp[i][j]:\n                        break\n          \
    \      else:\n                    return -1\n                tmp.mat[j], tmp.mat[i]\
    \ = tmp.mat[i], tmp.mat[j]\n                res.mat[j], res.mat[i] = res.mat[i],\
    \ res.mat[j]\n            tmp_j, res_j = tmp[j], res[j]\n            inv = pow(tmp_j[j],\
    \ self.MOD - 2, self.MOD)\n            for k in range(self.n):\n             \
    \   tmp_j[k] *= inv\n                tmp_j[k] %= self.MOD\n                res_j[k]\
    \ *= inv\n                res_j[k] %= self.MOD\n            for i in range(self.n):\n\
    \                if i == j:\n                    continue\n                c =\
    \ tmp[i][j]\n                tmp_i, res_i = tmp[i], res[i]\n                for\
    \ k in range(self.n):\n                    tmp_i[k] -= tmp_j[k] * c\n        \
    \            tmp_i[k] %= self.MOD\n                    res_i[k] -= res_j[k] *\
    \ c\n                    res_i[k] %= self.MOD\n        return res\n\n    def linear_equations(self,\
    \ vec):\n        assert self.n == len(vec)\n        aug = [self[i] + [vec[i]]\
    \ for i in range(self.n)]\n        rank = 0\n        p = []\n        q = []\n\
    \        for j in range(self.m + 1):\n            for i in range(rank, self.n):\n\
    \                if aug[i][j]:\n                    break\n            else:\n\
    \                q.append(j)\n                continue\n            if j == self.m:\n\
    \                return -1, [], []\n            p.append(j)\n            aug[rank],\
    \ aug[i] = aug[i], aug[rank]\n            inv = pow(aug[rank][j], self.MOD - 2,\
    \ self.MOD)\n            aug_rank = aug[rank]\n            for k in range(self.m\
    \ + 1):\n                aug_rank[k] *= inv\n                aug_rank[k] %= self.MOD\n\
    \            for i in range(self.n):\n                if i == rank:\n        \
    \            continue\n                aug_i = aug[i]\n                c = -aug_i[j]\n\
    \                for k in range(self.m + 1):\n                    aug_i[k] +=\
    \ c * aug_rank[k]\n                    aug_i[k] %= self.MOD\n            rank\
    \ += 1\n        dim = self.m - rank\n        sol = [0] * self.m\n        for i\
    \ in range(rank):\n            sol[p[i]] = aug[i][-1]\n        vecs = [[0] * self.m\
    \ for _ in range(dim)]\n        for i in range(dim):\n            vecs[i][q[i]]\
    \ = 1\n        for i in range(dim):\n            vecs_i = vecs[i]\n          \
    \  for j in range(rank):\n                vecs_i[p[j]] = -aug[j][q[i]] % self.MOD\n\
    \        return dim, sol, vecs\n\n\ndef determinant_arbitrary_mod(N, A, mod=998244353):\n\
    \    \"\"\"\n    A\u306F\u6B63\u65B9\u884C\u5217\u3092\u8868\u30592\u6B21\u5143\
    \u914D\u5217\n    A\u3092\u7834\u58CA\u7684\u5909\u66F4\u3059\u308B\u3053\u3068\
    \u306B\u6CE8\u610F\n    \"\"\"\n    res = 1\n    for i in range(N):\n        for\
    \ j in range(i + 1, N):\n            while A[j][i]:\n                tmp = A[i][i]\
    \ // A[j][i]\n                if tmp:\n                    for k in range(i, N):\n\
    \                        A[i][k] -= tmp * A[j][k]\n                        A[i][k]\
    \ %= mod\n                A[i], A[j] = A[j], A[i]\n                res *= -1\n\
    \                res %= mod\n        res *= A[i][i]\n        res %= mod\n    \
    \    if not res:\n            break\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: matrix/matrix.py
  requiredBy: []
  timestamp: '2023-06-21 22:43:59+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - library_checker/matrix/matrix_product.test.py
  - library_checker/matrix/matrix_inverse.test.py
  - library_checker/matrix/matrix_det_arbitrary_mod.test.py
  - library_checker/matrix/matrix_det.test.py
documentation_of: matrix/matrix.py
layout: document
redirect_from:
- /library/matrix/matrix.py
- /library/matrix/matrix.py.html
title: matrix/matrix.py
---
