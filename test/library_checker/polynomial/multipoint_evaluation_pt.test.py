# verification-helper: PROBLEM https://judge.yosupo.jp/problem/multipoint_evaluation
from convolution.product_tree import ProductTree

n, m = map(int, input().split())
C = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]
T = ProductTree(P)
print(*T.multipoint_evaluation(C))
