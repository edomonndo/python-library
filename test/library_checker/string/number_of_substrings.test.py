# verification-helper: PROBLEM https://judge.yosupo.jp/problem/number_of_substrings

from string_.suffix_array import suffix_array, lcp_array

S = "_" + input()
n = len(S)
sa = suffix_array(S)
lcp = lcp_array(S, sa)
print(n * (n - 1) // 2 - sum(lcp))
