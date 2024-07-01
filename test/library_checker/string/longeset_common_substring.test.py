# verification-helper: PROBLEM https://judge.yosupo.jp/problem/longest_common_substring

from str.longest_common_substring import find_lcs_idx

S = input()
T = input()
print(*find_lcs_idx(S, T))
