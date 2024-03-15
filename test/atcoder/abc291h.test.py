# verification-helper: IGNORE https://atcoder.jp/contests/abc291/tasks/abc291_h


from tree.centroid_decomposition import CentroidDecomposition

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    g[u].append(v)
    g[v].append(u)

tree = CentroidDecomposition(g)
print(*[v + 1 if v >= 0 else v for v in tree.belong])
