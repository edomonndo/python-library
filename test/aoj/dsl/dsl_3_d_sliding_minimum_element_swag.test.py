# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_D

from data_structure.basic.FoldableQue import FoldableQue

N, L = map(int, input().split())
A = list(map(int, input().split()))
INF = float("inf")
que = FoldableQue(min, INF)
ans = []
for i in range(L):
    que.push(A[i])
ans.append(que.fold())
for i in range(L, N):
    que.pop()
    que.push(A[i])
    ans.append(que.fold())
print(*ans)
