# verification-helper: PROBLEM https://judge.yosupo.jp/problem/montmort_number_mod

from enumerative_combinatorics.derangement import derangement

n, m = map(int, input().split())
print(*derangement(n, m)[1:])
