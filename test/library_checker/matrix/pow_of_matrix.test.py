# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix

from matrix.matrix import Matrix

n, k = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(n)]
M = Matrix(n, n, A)
M = M**k
for i in range(n):
    tmp = [M[i][j] for j in range(n)]
    print(" ".join(map(str, tmp)))
