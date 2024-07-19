# verification-helper: PROBLEM https://judge.yosupo.jp/problem/enumerate_triangles

from graph.enumerate_triangles import enumerate_triangles


MOD = 998244353


def calc(u: int, v: int, w: int) -> int:
    return X[u] * X[v] % MOD * X[w] % MOD


def merge(x: int, y: int) -> int:
    return (x + y) % MOD


n, m = map(int, input().split())
X = [int(x) for x in input().split()]
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(enumerate_triangles(n, edges, calc, merge, 0))
