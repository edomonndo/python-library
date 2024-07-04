# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_range_contour_sum_on_tree


from atcoder.fenwicktree import FenwickTree
from graph.tree.contour_query import ContourQuery


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
        B = [0] * len(arr[i])
        for j in range(len(arr[i])):
            B[j] = A[arr[i][j]]
        bit.append(FenwickTree(len(arr[i])))
        for j in range(len(arr[i])):
            bit[-1].add(j, B[j])


def query1(p, r):
    global ans
    ans += bit[p]._sum(r)


def query2(p, r):
    global ans
    ans -= bit[p]._sum(r)


cq = ContourQuery(g, f)

for _ in range(q):
    t, *qu = map(int, input().split())
    if t == 0:
        p, x = qu
        cq.vertex(p, lambda a, b: bit[a].add(b, x))
    else:
        p, l, r = qu
        ans = 0
        cq.range_contour(p, l, r, query1, query2)
        print(ans)
