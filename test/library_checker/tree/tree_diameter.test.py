# verification-helper: PROBLEM https://judge.yosupo.jp/problem/tree_diameter

from tree.diameter import diameter

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

diam, path = diameter(N, G, True)
print(diam, len(path))
print(*path)
