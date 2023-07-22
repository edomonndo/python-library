from string_.manacher import manacher

S = input()
N = len(S)
l1, l2 = manacher(S)

ans = [-1] * (2 * N - 1)
for i in range(N):
    ans[2 * i] = 2 * l1[i] + 1
    if i < N - 1:
        ans[2 * i + 1] = 2 * l2[i]
print(*ans)
