# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_count_distinct

from data_structure.wavelet_matrix import WaveletMatrix
from collections import Counter


def compress_to_list(arr):
    # 0-index
    return list(map({e: i for i, e in enumerate(sorted(set(arr)), 0)}.__getitem__, arr))


N, Q = map(int, input().split())
A = [int(x) for x in input().split()]
A = compress_to_list(A)
B = Counter()
for i, a in enumerate(A):
    A[i] = B[a]
    B[a] = i + 1

WM = WaveletMatrix(A)
for _ in range(Q):
    l, r = map(int, input().split())
    print(WM.rangefreq_to(l, r, l + 1))
