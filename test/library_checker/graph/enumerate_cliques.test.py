# verification-helper: PROBLEM https://judge.yosupo.jp/problem/enumerate_cliques

from graph.enumerate_cliques import enumerate_cliques


MOD = 998244353


def calc(vs: list[int]) -> int:
    res = 1
    for v in vs:
        res = (res * X[v]) % MOD
    return res


def merge(x: int, y: int) -> int:
    return (x + y) % MOD


n, m = map(int, input().split())
X = [int(x) for x in input().split()]
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(enumerate_cliques(n, edges, calc, merge, 0))
