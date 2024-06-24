# verification-helper: PROBLEM https://atcoder.jp/contests/abc339/tasks/abc339_g

from data_structure.segtree.merge_sort_tree import MergeSortTree

n = int(input())
A = [int(x) for x in input().split()]
q = int(input())
t = MergeSortTree(A)
res = 0
for _ in range(q):
    a, b, c = map(int, input().split())
    l, r, x = a ^ res, b ^ res, c ^ res
    res = t.sum_le(l - 1, r, x)
    print(res)
