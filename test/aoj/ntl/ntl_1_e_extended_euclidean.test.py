# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_E

from math_.ext_gcd import ext_gcd

a, b = map(int, input().split())
x, y = ext_gcd(a, b)
print(x, y)
