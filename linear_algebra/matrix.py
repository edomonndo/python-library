MOD = 998244353


class Matrix:

    def __init__(self, n: int, m: int, mat: list[list[int]] = None):
        self.n = n
        self.m = m
        self.mat = [[0] * self.m for _ in range(self.n)]
        if mat:
            assert len(mat) == n and len(mat[0]) == m
            for i in range(self.n):
                self.mat[i] = mat[i].copy()

    def __getitem__(self, key: int) -> list[int]:
        if isinstance(key, slice):
            return self.mat[key]
        else:
            assert key >= 0
            return self.mat[key]

    def __setitem__(self, key: int, value) -> None:
        if isinstance(key, slice):
            self.mat[key] = value
        else:
            assert key >= 0
            self.mat[key] = value

    def __len__(self) -> int:
        return len(self.mat)

    def __str__(self) -> str:
        return "\n".join(" ".join(map(str, self[i])) for i in range(self.n))

    def __pos__(self) -> int:
        return self

    def __neg__(self) -> int:
        return self.times(-1)

    def __add__(self, other) -> "Matrix":
        assert self.n == other.n and self.m == other.m
        res = [[0] * self.m for _ in range(self.n)]
        for i in range(self.n):
            res_i, self_i, other_i = res[i], self[i], other[i]
            for j in range(self.m):
                res_i[j] = (self_i[j] + other_i[j]) % MOD
        return __class__(self.n, self.m, res)

    def __sub__(self, other) -> "Matrix":
        assert self.n == other.n and self.m == other.m
        res = [[0] * self.m for _ in range(self.n)]
        for i in range(self.n):
            res_i, self_i, other_i = res[i], self[i], other[i]
            for j in range(self.m):
                res_i[j] = (self_i[j] - other_i[j]) % MOD
        return __class__(self.n, self.m, res)

    def __mul__(self, other) -> "Matrix":
        if other.__class__ == Matrix:
            assert self.m == other.n
            res = [[0] * other.m for _ in range(self.n)]
            for i in range(self.n):
                res_i, self_i = res[i], self[i]
                for k in range(self.m):
                    self_ik, other_k = self_i[k], other[k]
                    for j in range(other.m):
                        res_i[j] += self_ik * other_k[j]
                        res_i[j] %= MOD
            return __class__(self.n, other.m, res)
        else:
            return self.times(other)

    def __rmul__(self, other) -> "Matrix":
        return self.times(other)

    def __pow__(self, k: int) -> "Matrix":
        assert self.is_square()
        tmp = __class__(self.n, self.n, self.mat)
        res = self.id(self.n)
        while k:
            if k & 1:
                res *= tmp
            tmp *= tmp
            k >>= 1
        return res

    def is_square(self) -> bool:
        return self.n == self.m

    def id(self, n: int) -> "Matrix":
        res = __class__(n, n)
        for i in range(n):
            res[i][i] = 1
        return res

    def times(self, k: int) -> "Matrix":
        res = [[0] * self.m for _ in range(self.n)]
        for i in range(self.n):
            res_i, self_i = res[i], self[i]
            for j in range(self.m):
                res_i[j] = k * self_i[j] % MOD
        return __class__(self.n, self.m, res)

    def determinant(self) -> int:
        assert self.is_square()
        res = 1
        tmp = __class__(self.n, self.n, self.mat)
        for j in range(self.n):
            if tmp[j][j] == 0:
                for i in range(j + 1, self.n):
                    if tmp[i][j] != 0:
                        break
                else:
                    return 0
                tmp.mat[j], tmp.mat[i] = tmp.mat[i], tmp.mat[j]
                res *= -1
            tmp_j = tmp[j]
            inv = pow(tmp_j[j], MOD - 2, MOD)
            for i in range(j + 1, self.n):
                tmp_i = tmp[i]
                c = -inv * tmp_i[j] % MOD
                for k in range(self.n):
                    tmp_i[k] += c * tmp_j[k]
                    tmp_i[k] %= MOD
        for i in range(self.n):
            res *= tmp[i][i]
            res %= MOD
        return res

    def inverse(self) -> "Matrix":
        assert self.is_square()
        res = self.id(self.n)
        tmp = __class__(self.n, self.n, self.mat)
        for j in range(self.n):
            if tmp[j][j] == 0:
                for i in range(j + 1, self.n):
                    if tmp[i][j]:
                        break
                else:
                    return -1
                tmp.mat[j], tmp.mat[i] = tmp.mat[i], tmp.mat[j]
                res.mat[j], res.mat[i] = res.mat[i], res.mat[j]
            tmp_j, res_j = tmp[j], res[j]
            inv = pow(tmp_j[j], MOD - 2, MOD)
            for k in range(self.n):
                tmp_j[k] *= inv
                tmp_j[k] %= MOD
                res_j[k] *= inv
                res_j[k] %= MOD
            for i in range(self.n):
                if i == j:
                    continue
                c = tmp[i][j]
                tmp_i, res_i = tmp[i], res[i]
                for k in range(self.n):
                    tmp_i[k] -= tmp_j[k] * c
                    tmp_i[k] %= MOD
                    res_i[k] -= res_j[k] * c
                    res_i[k] %= MOD
        return res

    def rank(self) -> int:
        tmp = __class__(self.n, self.m, self.mat)
        rank = 0
        for j in range(self.m):
            for i in range(rank, self.n):
                if tmp[i][j] != 0:
                    break
            else:
                continue
            tmp[i], tmp[rank] = tmp[rank], tmp[i]
            inv = pow(tmp[rank][j], -1, MOD)
            tmp_rank = tmp[rank]
            for k in range(self.m):
                tmp_rank[k] = tmp_rank[k] * inv % MOD
            for i in range(self.n):
                if i == rank:
                    continue
                tmp_i = tmp[i]
                c = -tmp_i[j]
                for k in range(self.m):
                    tmp_i[k] = (tmp_i[k] + c * tmp_rank[k]) % MOD
            rank += 1
        return rank

    def linear_equations(
        self, vec: list[int]
    ) -> tuple[int, list[int], list[list[int]]]:
        assert self.n == len(vec)
        aug = [self[i] + [vec[i]] for i in range(self.n)]
        rank = 0
        p = []
        q = []
        for j in range(self.m + 1):
            for i in range(rank, self.n):
                if aug[i][j]:
                    break
            else:
                q.append(j)
                continue
            if j == self.m:
                return -1, [], []
            p.append(j)
            aug[rank], aug[i] = aug[i], aug[rank]
            inv = pow(aug[rank][j], MOD - 2, MOD)
            aug_rank = aug[rank]
            for k in range(self.m + 1):
                aug_rank[k] *= inv
                aug_rank[k] %= MOD
            for i in range(self.n):
                if i == rank:
                    continue
                aug_i = aug[i]
                c = -aug_i[j]
                for k in range(self.m + 1):
                    aug_i[k] += c * aug_rank[k]
                    aug_i[k] %= MOD
            rank += 1
        dim = self.m - rank
        sol = [0] * self.m
        for i in range(rank):
            sol[p[i]] = aug[i][-1]
        vecs = [[0] * self.m for _ in range(dim)]
        for i in range(dim):
            vecs[i][q[i]] = 1
        for i in range(dim):
            vecs_i = vecs[i]
            for j in range(rank):
                vecs_i[p[j]] = -aug[j][q[i]] % MOD
        return dim, sol, vecs
