# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_D

from data_structure.wavelet_matrix import WaveletMatrix

N, L = map(int, input().split())
A = list(map(int, input().split()))
WM = WaveletMatrix(A)
ans = []
for l in range(N - L + 1):
    ans.append(WM.quantile(l, l + L, 0))
print(*ans)
