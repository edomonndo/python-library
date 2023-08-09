# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_A

from data_structure.FoldableDeque import FoldableDeque

que = FoldableDeque(lambda x, y: x + y, 0)
N, S = map(int, input().split())
A = list(map(int, input().split()))
INF = float("inf")
ans = INF
n = 0
for i in range(N):
    que.push(A[i])
    n += 1
    if que.fold() < S:
        continue
    while que:
        que.popleft()
        n -= 1
        if que.fold() < S:
            ans = min(ans, n + 1)
            break
print(ans if ans != INF else 0)
