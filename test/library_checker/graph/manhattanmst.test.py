# verification-helper: PROBLEM https://judge.yosupo.jp/problem/manhattanmst

from geometory.manhattan_mst import ManhattanMST
from atcoder.dsu import DSU

n = int(input())
ps = [tuple(map(int, input().split())) for _ in range(n)]

mt = ManhattanMST()
for x, y in ps:
    mt.add_point(x, y)
mt.solve()

uf = DSU(n)
tot = 0
ans = []
for w, x, y in mt.edges:
    if uf.same(x, y):
        continue
    uf.merge(x, y)
    tot += w
    ans.append(f"{x} {y}")
print(tot)
print(*ans, sep="\n")
