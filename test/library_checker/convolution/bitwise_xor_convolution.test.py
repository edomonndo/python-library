# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_xor_convolution

from convolution.walsh_hadamard_tranform import bitwise_xor_conv

n = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
bitwise_xor_conv(A, B)
print(*A)
