# verification-helper: PROBLEM https://judge.yosupo.jp/problem/primitive_root

from math_.primitive_root import primitive_root


q = int(input())
for _ in range(q):
    p = int(input())
    print(primitive_root(p))
