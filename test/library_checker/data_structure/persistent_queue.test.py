# verification-helper: PROBLEM https://judge.yosupo.jp/problem/persistent_queue
from persistent_data_structure.persistent_queue import PersistentQueue

Q = int(input())
q = PersistentQueue(Q)
for _ in range(Q):
    t, *query = map(int, input().split())
    if t == 0:
        k, x = query
        q.append(t, x)
    else:
        k = query[0]
        print(q.popleft(t))
