# verification-helper: PROBLEM https://judge.yosupo.jp/problem/maximum_independent_set

from graph.maximum_independent_set import maximum_independnet_set

n, m = map(int, input().split())
es = [tuple(map(int, input().split())) for _ in range(m)]
size, res = maximum_independnet_set(n, es)
print(size)
print(*res)
