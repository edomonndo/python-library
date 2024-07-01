# verification-helper: PROBLEM https://atcoder.jp/contests/abc340/tasks/abc340_g

from collections import defaultdict
from tree.auxiliary_tree import AuxiliaryTree

MOD = 998244353

n = int(input())
A = [int(x) for x in input().split()]
g0 = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    g0[u].append(v)
    g0[v].append(u)
AT = AuxiliaryTree(g0)
d = defaultdict(list)
for i, a in enumerate(A):
    d[a].append(i)
ans = 0
for a in d.keys():
    r, g = AT.build(d[a])
    dp1 = dict()
    dp2 = dict()
    stack = [~r, r]
    while stack:
        v = stack.pop()
        if v >= 0:
            for u in g[v]:
                stack.append(~u)
                stack.append(u)
        else:
            v = ~v
            if A[v] == a:
                res = 1
                for u in g[v]:
                    res *= dp2[u] + 1
                    res %= MOD
                dp1[v] = dp2[v] = res
            else:
                res = 1
                tmp = 0
                for u in g[v]:
                    res *= dp2[u] + 1
                    tmp += dp2[u]
                    res %= MOD
                    tmp %= MOD
                dp1[v] = res - tmp - 1
                dp2[v] = res - 1
    for x in dp1.values():
        ans = (ans + x) % MOD
print(ans)
