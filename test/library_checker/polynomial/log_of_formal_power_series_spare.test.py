# verification-helper: PROBLEM https://judge.yosupo.jp/problem/log_of_formal_power_series_sparse

from convolution.formal_power_series import FPS

n, k = map(int, input().split())
A = [0] * n
for _ in range(k):
    i, a = map(int, input().split())
    A[i] = a
print(*FPS.log(A))
