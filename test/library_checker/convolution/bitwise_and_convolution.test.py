# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution

from convolution.zeta_moebius_transform import bitwize_and_conv


n = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
bitwize_and_conv(A, B)
print(*A)
