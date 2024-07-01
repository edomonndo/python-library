# verification-helper: PROBLEM https://judge.yosupo.jp/problem/number_of_subsequences

from enumerative_combinatorics.number_of_subsequences import solve

n = int(input())
A = [int(x) for x in input().split()]
print(solve(A))
