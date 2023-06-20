# verification-helper: PROBLEM https://judge.yosupo.jp/problem/convolution_mod

from convolution.convolution import multiply

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = multiply(A, B)
print(*C)
