# verification-helper: PROBLEM https://judge.yosupo.jp/problem/double_ended_priority_queue

from data_structure.SortedMultiset import SortedMultiset

N, Q = map(int, input().split())
S = list(map(int, input().split()))

MultiSet = SortedMultiset(S)

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        MultiSet.add(query[1])
    elif query[0] == 1:
        print(MultiSet.pop(0))
    elif query[0] == 2:
        print(MultiSet.pop(-1))
