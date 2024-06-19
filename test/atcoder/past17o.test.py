# verification-helper: IGNORE https://atcoder.jp/contests/past17-open/tasks/past17_o

from data_structure.fenwick_tree.value_range_sum import CompressedValueRangeSum

n = int(input())
A = [int(x) for x in input().split()]
ps = set(A)
q = int(input())
qs = [tuple(map(int, input().split())) for _ in range(q)]
B = A[:]
for t, *qu in qs:
    if t == 1:
        k, d = qu
        k -= 1
        B[k] += d
        ps.add(B[k])
    else:
        ps.add(qu[0])
S = CompressedValueRangeSum(A, ps)
for t, *qu in qs:
    if t == 1:
        k, d = qu
        k -= 1
        S.add(k, d)
    else:
        x = qu[0]
        print(S.sum_abs_from(x))
