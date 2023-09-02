# verification-helper: PROBLEM https://judge.yosupo.jp/problem/persistent_unionfind

from data_structure.rollback_unionfind import RollbackUnionFind

N, Q = map(int, input().split())
G = [[] for _ in range(Q + 1)]

for i in range(1, Q + 1):
    t, k, u, v = map(int, input().split())
    k += 1
    G[k].append((t, i, u, v, 1))

uf = RollbackUnionFind(N)
ans = [-1] * (Q + 1)
stack = [(-1, 0, -1, 0, 1)]
while stack:
    t, k, u, v, flag = stack.pop()
    if t == 1:
        ans[k] = uf.same(u, v)
        continue
    if flag:
        stack.append((t, k, u, v, 0))
        if t == 0:
            uf.merge(u, v)
        for item in G[k]:
            stack.append(item)
        continue
    if t == 0:
        uf.undo()

for x in ans:
    if x != -1:
        print(1 if x else 0)
