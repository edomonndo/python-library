# verification-helper: PROBLEM https://judge.yosupo.jp/problem/convolution_mod_1000000007

from convolution.cooley_turkey import CooleyTukey

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = CooleyTukey().karatsuba(A, B, 10**9 + 7)
print(*C)
