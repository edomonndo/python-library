def determinant_arbitrary_mod(N, A, mod=998244353):
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
