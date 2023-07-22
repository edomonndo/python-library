# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_frequency

from data_structure.wavelet_matrix import WaveletMatrix

N, Q = map(int, input().split())
A = list(map(int, input().split()))

WM = WaveletMatrix(A)

for _ in range(Q):
    l, r, x = map(int, input().split())
    print(WM.rangefreq(l, r, x, x + 1))
