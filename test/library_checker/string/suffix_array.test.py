# verification-helper: PROBLEM https://judge.yosupo.jp/problem/suffixarray

from str.suffix_array import suffix_array

S = input()
sa = suffix_array(S)
print(*sa)
