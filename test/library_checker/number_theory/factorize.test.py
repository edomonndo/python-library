# verification-helper: PROBLEM https://judge.yosupo.jp/problem/factorize

from number_theory.factorize import factorize

Q = int(input())
query = [int(input()) for _ in range(Q)]
ans = [None] * Q
for i in range(Q):
    x = factorize(query[i])
    factors = [i for i, j in sorted(x.items()) for _ in range(j)]
    ans[i] = " ".join(map(str, [len(factors)] + factors))

print(*ans, sep="\n")
