# verification-helper: IGNORE https://atcoder.jp/contests/past202104-open/tasks/past202104_m

from data_structure.interval_manager import IntervalManager

from collections import defaultdict

n = int(input())
A = [int(x) for x in input().split()]


d = defaultdict(int)


def add(l, r, x):
    global score
    score -= d[x] * (d[x] - 1) // 2
    d[x] += r - l
    score += d[x] * (d[x] - 1) // 2


def remove(l, r, x):
    add(r, l, x)


score = 0
im = IntervalManager(A, add, remove)

Q = int(input())
for _ in range(Q):
    l, r, x = map(int, input().split())
    im.update(l - 1, r, x)
    print(score)
