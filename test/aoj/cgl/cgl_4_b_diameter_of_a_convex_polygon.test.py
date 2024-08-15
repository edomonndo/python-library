# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/4/CGL_4_B

from geometory.diameter import diameter

n = int(input())
ps = [tuple(map(float, input().split())) for _ in range(n)]
d, _, _ = diameter(ps)
print(d)
