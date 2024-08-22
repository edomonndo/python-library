# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rational_approximation


from number_theory.stern_brocot_tree import SternBrocotTree

t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    a, b, c, d = SternBrocotTree.approx(n, x, y)
    print(a, b, c, d)
