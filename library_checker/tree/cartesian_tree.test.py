# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cartesian_tree

from tree.cartesian_tree import cartesian_tree

N = int(input())
A = list(map(int, input().split()))

parent = cartesian_tree(A)
# 根は$parent_r$ = rとする
print(*[v if v != -1 else i for i, v in enumerate(parent)])
