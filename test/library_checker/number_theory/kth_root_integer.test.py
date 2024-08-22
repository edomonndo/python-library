# verification-helper: PROBLEM https://judge.yosupo.jp/problem/kth_root_integer

from number_theory.kth_root import KthRoot

t = int(input())
for _ in range(t):
    a, k = map(int, input().split())
    print(KthRoot.floor(a, k))
