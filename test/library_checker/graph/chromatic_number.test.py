# verification-helper: PROBLEM https://judge.yosupo.jp/problem/chromatic_number

from graph.chromatic_number import chromatic_number

n, m = map(int, input().split())
es = [tuple(map(int, input().split())) for _ in range(m)]
print(chromatic_number(n, es))
