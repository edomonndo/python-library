# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_A

from data_structure.basic.segment_tree import RangeMinQuery

N, Q = map(int, input().split())
INF = (1 << 31) - 1
G = RangeMinQuery([INF] * N)

ans = []
for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 0:
        G.update(x, y)
    else:
        ans.append(G.query(x, y + 1))
print(*ans, sep="\n")
