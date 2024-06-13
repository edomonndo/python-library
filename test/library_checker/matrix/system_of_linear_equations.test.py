# verification-helper: PROBLEM https://judge.yosupo.jp/problem/system_of_linear_equations

from matrix.matrix import Matrix

n, m = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(n)]
B = [int(x) for x in input().split()]
M = Matrix(n, m, A)
dim, sol, vecs = M.linear_equations(B)
print(dim)
print(*sol)
for vec in vecs:
    print(*vec)
