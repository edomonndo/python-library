# verification-helper: PROBLEM https://judge.yosupo.jp/problem/assignment

from graph.hungarian import hungarian

N = int(input())
A = [[int(x) for x in input().split()] for _ in range(N)]
total, row = hungarian(A)
print(total)
print(*row)
