# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_C

from geometory.kd_tree import KDTree

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]
kd = KDTree(N, XY)

Q = int(input())
for _ in range(Q):
    sx, tx, sy, ty = map(int, input().split())
    ans = kd.query(sx, sy, tx, ty)
    for id in sorted(ans):
        print(id)
    print()
