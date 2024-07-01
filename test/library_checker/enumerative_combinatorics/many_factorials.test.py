# verification-helper: PROBLEM https://judge.yosupo.jp/problem/many_factorials

from enumerative_combinatorics.factorial_iter_mod import factorial_iter_mod


t = int(input())
qs = [int(input()) for _ in range(t)]
ans = factorial_iter_mod(qs)
print(*ans, sep="\n")
