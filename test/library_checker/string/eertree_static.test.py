# verification-helper: PROBLEM https://judge.yosupo.jp/problem/eertree

from str.palindromic_tree import PalindromicTree

S = input()
PT = PalindromicTree(S, "a")
par, suffix_link, mx_palindromic_suffix = PT.solve()
print(PT.n)
for p, s in zip(par, suffix_link):
    print(p, s)
print(*mx_palindromic_suffix)
