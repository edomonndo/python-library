# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_get_range_contour_add_on_tree

from data_structure.fenwick_tree.range_add_point_get import RangeAddPointGet
from tree.contour_query import ContourQuery


n, q = map(int, input().split())
A = [int(x) for x in input().split()]
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

bit = []


def f(arr):
    for i in range(len(arr)):
        bit.append(RangeAddPointGet(len(arr[i])))


def query(p, k):
    global ans
    ans += bit[p].get(k)


cq = ContourQuery(g, f)

for _ in range(q):
    t, *qu = map(int, input().split())
    if t == 0:
        p, l, r, x = qu
        cq.range_contour(
            p, l, r, lambda p, r: bit[p].add(0, r, x), lambda p, r: bit[p].add(0, r, -x)
        )
    else:
        p = qu[0]
        ans = A[p]
        cq.vertex(p, query)
        print(ans)
