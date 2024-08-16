# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/5/CGL_5_A
# verification-helper: ERROR 1e-6

from geometory.closest_pair import closest_pair

n = int(input())
ps = []
for _ in range(n):
    x, y = map(float, input().split())
    ps.append((x * 10**6, y * 10**6))
d, _, _ = closest_pair(ps)
print(d / (10**6))
