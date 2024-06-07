# verification-helper: PROBLEM https://judge.yosupo.jp/problem/deque_operate_all_composite

from data_structure.basic.FoldableDeque import FoldableDeque

MOD = 998244353
mask = (1 << 32) - 1


def op(x, y):
    ax, bx = x >> 32, x & mask
    ay, by = y >> 32, y & mask
    return (ax * ay % MOD) << 32 | (ay * bx + by) % MOD


que = FoldableDeque(op, 1 << 32)
Q = int(input())
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        a, b = q
        que.pushleft(a << 32 | b)
    elif t == 1:
        a, b = q
        que.push(a << 32 | b)
    elif t == 2:
        que.popleft()
    elif t == 3:
        que.pop()
    else:
        x = q[0]
        c = que.fold()
        a, b = c >> 32, c & mask
        print((a * x + b) % MOD)
