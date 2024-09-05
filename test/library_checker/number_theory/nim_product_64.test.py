# verification-helper: PROBLEM https://judge.yosupo.jp/problem/nim_product_64

from number_theory.nimber import Nimber

t = int(input())
nim = Nimber()
for _ in range(t):
    a, b = map(int, input().split())
    print(nim.product_64(a, b))
