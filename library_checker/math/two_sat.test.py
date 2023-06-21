# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_sat

from math_.two_sat import two_sat

p, cnf, N, M = input().split()
N, M = map(int, (N, M))
clause = []
for i in range(M):
    a, b, z = map(int, input().split())
    c, d = (a // abs(a) + 1) // 2, (b // abs(b) + 1) // 2
    c, d = bool(c), bool(d)
    clause.append((abs(a) - 1, c, abs(b) - 1, d))
result = two_sat(N, clause)
if result == None:
    print("s UNSATISFIABLE")
else:
    print("s SATISFIABLE")
    print("v", *[(i + 1) if result[i] else (-1 - i) for i in range(N)] + [0])
