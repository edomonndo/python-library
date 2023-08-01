# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_kth_smallest


from data_structure.wavelet_matrix import WaveletMatrix

N, Q = map(int, input().split())
A = list(map(int, input().split()))

WM = WaveletMatrix(A)

for _ in range(Q):
    l, r, k = map(int, input().split())
    print(WM.quantile(l, r, k))
