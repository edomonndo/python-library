# verification-helper: PROBLEM https://judge.yosupo.jp/problem/factorial

from math_.factorial_mod import factorial_mod


t = int(input())

for _ in range(t):
    n = int(input())
    print(factorial_mod(n))
