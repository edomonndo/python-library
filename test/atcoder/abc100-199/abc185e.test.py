# verification-helper: PROBLEM https://atcoder.jp/contests/abc185/tasks/abc185_e

from dynamic_programming.edit_distance import edit_distance

n, m = map(int, input().split())
S = [int(x) for x in input().split()]
T = [int(x) for x in input().split()]
print(edit_distance(S, T, 1, 1, 1))
