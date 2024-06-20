# verification-helper: PROBLEM https://judge.yosupo.jp/problem/multipoint_evaluation_on_geometric_sequence
from convolution.chirp_z import *

n, m, a, r = map(int, input().split())
C = [int(x) for x in input().split()]
print(*chirp_z(C, r, m, a))
