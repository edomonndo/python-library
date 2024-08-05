---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':question:'
    path: graph/matrix_tree_theorem.py
    title: "\u884C\u5217\u6728\u5B9A\u7406"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/linear_algebra/linear_equations.test.py
    title: System of Linear Equations
  - icon: ':heavy_check_mark:'
    path: test/library_checker/linear_algebra/matrix_determinant.test.py
    title: Determinant of Matrix
  - icon: ':heavy_check_mark:'
    path: test/library_checker/linear_algebra/matrix_inverse.test.py
    title: Inverse Matrix
  - icon: ':heavy_check_mark:'
    path: test/library_checker/linear_algebra/matrix_power.test.py
    title: Pow of Matrix
  - icon: ':heavy_check_mark:'
    path: test/library_checker/linear_algebra/matrix_product.test.py
    title: Matrix Product
  - icon: ':heavy_check_mark:'
    path: test/library_checker/linear_algebra/matrix_rank.test.py
    title: Rank of Matrix
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "MOD = 998244353\n\n\nclass Matrix:\n\n    def __init__(self, n: int, m: int,\
    \ mat: list[list[int]] = None):\n        self.n = n\n        self.m = m\n    \
    \    self.mat = [[0] * self.m for _ in range(self.n)]\n        if mat:\n     \
    \       assert len(mat) == n and len(mat[0]) == m\n            for i in range(self.n):\n\
    \                self.mat[i] = mat[i].copy()\n\n    def __getitem__(self, key:\
    \ int) -> list[int]:\n        if isinstance(key, slice):\n            return self.mat[key]\n\
    \        else:\n            assert key >= 0\n            return self.mat[key]\n\
    \n    def __setitem__(self, key: int, value) -> None:\n        if isinstance(key,\
    \ slice):\n            self.mat[key] = value\n        else:\n            assert\
    \ key >= 0\n            self.mat[key] = value\n\n    def __len__(self) -> int:\n\
    \        return len(self.mat)\n\n    def __str__(self) -> str:\n        return\
    \ \"\\n\".join(\" \".join(map(str, self[i])) for i in range(self.n))\n\n    def\
    \ __pos__(self) -> int:\n        return self\n\n    def __neg__(self) -> int:\n\
    \        return self.times(-1)\n\n    def __add__(self, other) -> \"Matrix\":\n\
    \        assert self.n == other.n and self.m == other.m\n        res = [[0] *\
    \ self.m for _ in range(self.n)]\n        for i in range(self.n):\n          \
    \  res_i, self_i, other_i = res[i], self[i], other[i]\n            for j in range(self.m):\n\
    \                res_i[j] = (self_i[j] + other_i[j]) % MOD\n        return __class__(self.n,\
    \ self.m, res)\n\n    def __sub__(self, other) -> \"Matrix\":\n        assert\
    \ self.n == other.n and self.m == other.m\n        res = [[0] * self.m for _ in\
    \ range(self.n)]\n        for i in range(self.n):\n            res_i, self_i,\
    \ other_i = res[i], self[i], other[i]\n            for j in range(self.m):\n \
    \               res_i[j] = (self_i[j] - other_i[j]) % MOD\n        return __class__(self.n,\
    \ self.m, res)\n\n    def __mul__(self, other) -> \"Matrix\":\n        if other.__class__\
    \ == Matrix:\n            assert self.m == other.n\n            res = [[0] * other.m\
    \ for _ in range(self.n)]\n            for i in range(self.n):\n             \
    \   res_i, self_i = res[i], self[i]\n                for k in range(self.m):\n\
    \                    self_ik, other_k = self_i[k], other[k]\n                \
    \    for j in range(other.m):\n                        res_i[j] += self_ik * other_k[j]\n\
    \                        res_i[j] %= MOD\n            return __class__(self.n,\
    \ other.m, res)\n        else:\n            return self.times(other)\n\n    def\
    \ __rmul__(self, other) -> \"Matrix\":\n        return self.times(other)\n\n \
    \   def __pow__(self, k: int) -> \"Matrix\":\n        assert self.is_square()\n\
    \        tmp = __class__(self.n, self.n, self.mat)\n        res = self.id(self.n)\n\
    \        while k:\n            if k & 1:\n                res *= tmp\n       \
    \     tmp *= tmp\n            k >>= 1\n        return res\n\n    def is_square(self)\
    \ -> bool:\n        return self.n == self.m\n\n    def id(self, n: int) -> \"\
    Matrix\":\n        res = __class__(n, n)\n        for i in range(n):\n       \
    \     res[i][i] = 1\n        return res\n\n    def times(self, k: int) -> \"Matrix\"\
    :\n        res = [[0] * self.m for _ in range(self.n)]\n        for i in range(self.n):\n\
    \            res_i, self_i = res[i], self[i]\n            for j in range(self.m):\n\
    \                res_i[j] = k * self_i[j] % MOD\n        return __class__(self.n,\
    \ self.m, res)\n\n    def determinant(self) -> int:\n        assert self.is_square()\n\
    \        res = 1\n        tmp = __class__(self.n, self.n, self.mat)\n        for\
    \ j in range(self.n):\n            if tmp[j][j] == 0:\n                for i in\
    \ range(j + 1, self.n):\n                    if tmp[i][j] != 0:\n            \
    \            break\n                else:\n                    return 0\n    \
    \            tmp.mat[j], tmp.mat[i] = tmp.mat[i], tmp.mat[j]\n               \
    \ res *= -1\n            tmp_j = tmp[j]\n            inv = pow(tmp_j[j], MOD -\
    \ 2, MOD)\n            for i in range(j + 1, self.n):\n                tmp_i =\
    \ tmp[i]\n                c = -inv * tmp_i[j] % MOD\n                for k in\
    \ range(self.n):\n                    tmp_i[k] += c * tmp_j[k]\n             \
    \       tmp_i[k] %= MOD\n        for i in range(self.n):\n            res *= tmp[i][i]\n\
    \            res %= MOD\n        return res\n\n    def inverse(self) -> \"Matrix\"\
    :\n        assert self.is_square()\n        res = self.id(self.n)\n        tmp\
    \ = __class__(self.n, self.n, self.mat)\n        for j in range(self.n):\n   \
    \         if tmp[j][j] == 0:\n                for i in range(j + 1, self.n):\n\
    \                    if tmp[i][j]:\n                        break\n          \
    \      else:\n                    return -1\n                tmp.mat[j], tmp.mat[i]\
    \ = tmp.mat[i], tmp.mat[j]\n                res.mat[j], res.mat[i] = res.mat[i],\
    \ res.mat[j]\n            tmp_j, res_j = tmp[j], res[j]\n            inv = pow(tmp_j[j],\
    \ MOD - 2, MOD)\n            for k in range(self.n):\n                tmp_j[k]\
    \ *= inv\n                tmp_j[k] %= MOD\n                res_j[k] *= inv\n \
    \               res_j[k] %= MOD\n            for i in range(self.n):\n       \
    \         if i == j:\n                    continue\n                c = tmp[i][j]\n\
    \                tmp_i, res_i = tmp[i], res[i]\n                for k in range(self.n):\n\
    \                    tmp_i[k] -= tmp_j[k] * c\n                    tmp_i[k] %=\
    \ MOD\n                    res_i[k] -= res_j[k] * c\n                    res_i[k]\
    \ %= MOD\n        return res\n\n    def rank(self) -> int:\n        tmp = __class__(self.n,\
    \ self.m, self.mat)\n        rank = 0\n        for j in range(self.m):\n     \
    \       for i in range(rank, self.n):\n                if tmp[i][j] != 0:\n  \
    \                  break\n            else:\n                continue\n      \
    \      tmp[i], tmp[rank] = tmp[rank], tmp[i]\n            inv = pow(tmp[rank][j],\
    \ -1, MOD)\n            tmp_rank = tmp[rank]\n            for k in range(self.m):\n\
    \                tmp_rank[k] = tmp_rank[k] * inv % MOD\n            for i in range(self.n):\n\
    \                if i == rank:\n                    continue\n               \
    \ tmp_i = tmp[i]\n                c = -tmp_i[j]\n                for k in range(self.m):\n\
    \                    tmp_i[k] = (tmp_i[k] + c * tmp_rank[k]) % MOD\n         \
    \   rank += 1\n        return rank\n\n    def linear_equations(\n        self,\
    \ vec: list[int]\n    ) -> tuple[int, list[int], list[list[int]]]:\n        assert\
    \ self.n == len(vec)\n        aug = [self[i] + [vec[i]] for i in range(self.n)]\n\
    \        rank = 0\n        p = []\n        q = []\n        for j in range(self.m\
    \ + 1):\n            for i in range(rank, self.n):\n                if aug[i][j]:\n\
    \                    break\n            else:\n                q.append(j)\n \
    \               continue\n            if j == self.m:\n                return\
    \ -1, [], []\n            p.append(j)\n            aug[rank], aug[i] = aug[i],\
    \ aug[rank]\n            inv = pow(aug[rank][j], MOD - 2, MOD)\n            aug_rank\
    \ = aug[rank]\n            for k in range(self.m + 1):\n                aug_rank[k]\
    \ *= inv\n                aug_rank[k] %= MOD\n            for i in range(self.n):\n\
    \                if i == rank:\n                    continue\n               \
    \ aug_i = aug[i]\n                c = -aug_i[j]\n                for k in range(self.m\
    \ + 1):\n                    aug_i[k] += c * aug_rank[k]\n                   \
    \ aug_i[k] %= MOD\n            rank += 1\n        dim = self.m - rank\n      \
    \  sol = [0] * self.m\n        for i in range(rank):\n            sol[p[i]] =\
    \ aug[i][-1]\n        vecs = [[0] * self.m for _ in range(dim)]\n        for i\
    \ in range(dim):\n            vecs[i][q[i]] = 1\n        for i in range(dim):\n\
    \            vecs_i = vecs[i]\n            for j in range(rank):\n           \
    \     vecs_i[p[j]] = -aug[j][q[i]] % MOD\n        return dim, sol, vecs\n"
  dependsOn: []
  isVerificationFile: false
  path: linear_algebra/matrix.py
  requiredBy:
  - graph/matrix_tree_theorem.py
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/linear_algebra/matrix_power.test.py
  - test/library_checker/linear_algebra/matrix_product.test.py
  - test/library_checker/linear_algebra/matrix_rank.test.py
  - test/library_checker/linear_algebra/matrix_determinant.test.py
  - test/library_checker/linear_algebra/matrix_inverse.test.py
  - test/library_checker/linear_algebra/linear_equations.test.py
documentation_of: linear_algebra/matrix.py
layout: document
title: "\u884C\u5217"
---

Matrixクラスは$\bmod{998,244,353}$で計算される.

### `Mat = Matrix(N, M, [Mat])`

$N$行$M$列の行列を作成する.引数に$Mat$を指定した場合は,その行列をコピーする.

### `四則演算`

$+$,$-$,$\times$　がサポートされている.

### `Mat.is_square()`

正方行列(`self.n == self.m`)であれば`True`.

### `Mat.times(k)`

行列の各要素を`k`倍する.

### `Mat.determinant()`

行列式を計算する.

### `Mat.inverse()`

逆行列を計算する.

### `Mat.linear_equations(b)`

行列$A$とベクトル$b$から,$Ax=b$となるベクトル$x$を求める.
