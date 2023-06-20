# verification-helper: PROBLEM https://judge.yosupo.jp/problem/factorize

from math.factorize import factorize

Q = int(input())
query = [input() for _ in range(Q)]
ans = [None] * Q
for i in range(Q):
    x = factorize(query[i])
    ans[i] = " ".join([str(len(x))] + x)

print(*ans, sep="\n")
