class Matrix:
    MOD = 998244353

    def __init__(self, n, m, mat=None):
        self.n = n
        self.m = m
        self.mat = [[0] * self.m for _ in range(self.n)]
        if mat:
            assert len(mat) == n and len(mat[0]) == m
            for i in range(self.n):
                self.mat[i] = mat[i].copy()

    def __getitem__(self, key):
        if isinstance(key, slice):
            return self.mat[key]
        else:
            assert key >= 0
            return self.mat[key]

    def __len__(self):
        return len(self.mat)

    def __str__(self):
        return "\n".join(" ".join(map(str, self[i])) for i in range(self.n))

    def __pos__(self):
        return self

    def __neg__(self):
        return self.times(-1)

    def __add__(self, other):
        assert self.n == other.n and self.m == other.m
        res = [[0] * self.m for _ in range(self.n)]
        for i in range(self.n):
            res_i, self_i, other_i = res[i], self[i], other[i]
            for j in range(self.m):
                res_i[j] = (self_i[j] + other_i[j]) % self.MOD
        return Matrix(self.n, self.m, res)

    def __sub__(self, other):
        assert self.n == other.n and self.m == other.m
        res = [[0] * self.m for _ in range(self.n)]
        for i in range(self.n):
            res_i, self_i, other_i = res[i], self[i], other[i]
            for j in range(self.m):
                res_i[j] = (self_i[j] - other_i[j]) % self.MOD
        return Matrix(self.n, self.m, res)

    def __mul__(self, other):
        if other.__class__ == Matrix:
            assert self.m == other.n
            res = [[0] * other.m for _ in range(self.n)]
            for i in range(self.n):
                res_i, self_i = res[i], self[i]
                for k in range(self.m):
                    self_ik, other_k = self_i[k], other[k]
                    for j in range(other.m):
                        res_i[j] += self_ik * other_k[j]
                        res_i[j] %= self.MOD
            return Matrix(self.n, other.m, res)
        else:
            return self.times(other)

    def __rmul__(self, other):
        return self.times(other)

    def __pow__(self, k):
        assert self.is_square()
        tmp = Matrix(self.n, self.n, self.mat)
        res = Matrix.id(self.n)
        while k:
            if k & 1:
                res *= tmp
            tmp *= tmp
            k >>= 1
        return res

    def is_square(self):
        return self.n == self.m

    def id(n):
        res = Matrix(n, n)
        for i in range(n):
            res[i][i] = 1
        return res

    def times(self, k):
        res = [[0] * self.m for _ in range(self.n)]
        for i in range(self.n):
            res_i, res_j = res[i], self[i]
            for j in range(self.m):
                res_i[j] = k * self_i[j] % self.MOD
        return Matrix(self.n, self.m, res)

    def linear_equations(self, vec):
        assert self.n == len(vec)
        aug = [self[i] + [vec[i]] for i in range(self.n)]
        rank = 0
        p = []
        q = []
        for j in range(self.m + 1):
            for i in range(rank, self.n):
                if aug[i][j] != 0:
                    break
            else:
                q.append(j)
                continue
            if j == self.m:
                return -1, [], []
            p.append(j)
            aug[rank], aug[i] = aug[i], aug[rank]
            inv = pow(aug[rank][j], self.MOD - 2, self.MOD)
            aug_rank = aug[rank]
            for k in range(self.m + 1):
                aug_rank[k] *= inv
                aug_rank[k] %= self.MOD
            for i in range(self.n):
                if i == rank:
                    continue
                aug_i = aug[i]
                c = -aug_i[j]
                for k in range(self.m + 1):
                    aug_i[k] += c * aug_rank[k]
                    aug_i[k] %= self.MOD
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
                vecs_i[p[j]] = -aug[j][q[i]] % self.MOD
        return dim, sol, vecs

    def determinant(self):
        assert self.is_square()
        res = 1
        tmp = Matrix(self.n, self.n, self.mat)
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
            inv = pow(tmp_j[j], self.MOD - 2, self.MOD)
            for i in range(j + 1, self.n):
                tmp_i = tmp[i]
                c = -inv * tmp_i[j] % self.MOD
                for k in range(self.n):
                    tmp_i[k] += c * tmp_j[k]
                    tmp_i[k] %= self.MOD
        for i in range(self.n):
            res *= tmp[i][i]
            res %= self.MOD
        return res

    def inverse(self):
        assert self.is_square()
        res = Matrix.id(self.n)
        tmp = Matrix(self.n, self.n, self.mat)
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
            inv = pow(tmp_j[j], self.MOD - 2, self.MOD)
            for k in range(self.n):
                tmp_j[k] *= inv
                tmp_j[k] %= self.MOD
                res_j[k] *= inv
                res_j[k] %= self.MOD
            for i in range(self.n):
                if i == j:
                    continue
                c = tmp[i][j]
                tmp_i, res_i = tmp[i], res[i]
                for k in range(self.n):
                    tmp_i[k] -= tmp_j[k] * c
                    tmp_i[k] %= self.MOD
                    res_i[k] -= res_j[k] * c
                    res_i[k] %= self.MOD
        return res

    def linear_equations(self, vec):
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
            inv = pow(aug[rank][j], self.MOD - 2, self.MOD)
            aug_rank = aug[rank]
            for k in range(self.m + 1):
                aug_rank[k] *= inv
                aug_rank[k] %= self.MOD
            for i in range(self.n):
                if i == rank:
                    continue
                aug_i = aug[i]
                c = -aug_i[j]
                for k in range(self.m + 1):
                    aug_i[k] += c * aug_rank[k]
                    aug_i[k] %= self.MOD
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
                vecs_i[p[j]] = -aug[j][q[i]] % self.MOD
        return dim, sol, vecs


def determinant_arbitrary_mod(N, A, mod=998244353):
    """
    Aは正方行列を表す2次元配列
    Aを破壊的変更することに注意
    """
    res = 1
    for i in range(N):
        for j in range(i + 1, N):
            while A[j][i]:
                tmp = A[i][i] // A[j][i]
                if tmp:
                    for k in range(i, N):
                        A[i][k] -= tmp * A[j][k]
                        A[i][k] %= mod
                A[i], A[j] = A[j], A[i]
                res *= -1
                res %= mod
        res *= A[i][i]
        res %= mod
        if not res:
            break
    return res
