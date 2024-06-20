# verification-helper: PROBLEM https://judge.yosupo.jp/problem/multipoint_evaluation_on_geometric_sequence
from convolution.multipoint_evaluation import *

n, m = map(int, input().split())
C = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]
print(*multipoint_evaluation(C, P))
