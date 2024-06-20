# verification-helper: PROBLEM https://judge.yosupo.jp/problem/polynomial_interpolation
from convolution.product_tree import ProductTree


n = int(input())
xs = [int(x) for x in input().split()]
ys = [int(x) for x in input().split()]
T = ProductTree(xs)
print(*T.polynomial_interpolation(ys))
