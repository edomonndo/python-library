MOD = 998244353


def determinant_arbitrary_mod(N, A, MOD):
    res = 1
    for i in range(N):
        for j in range(i + 1, N):
            while A[j][i]:
                tmp = A[i][i] // A[j][i]
                if tmp:
                    for k in range(i, N):
                        A[i][k] -= tmp * A[j][k]
                        A[i][k] %= MOD
                A[i], A[j] = A[j], A[i]
                res *= -1
                res %= MOD
        res *= A[i][i]
        res %= MOD
        if not res:
            break
    return res
