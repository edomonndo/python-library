# verification-helper: PROBLEM https://judge.yosupo.jp/problem/predecessor_problem

from data_structure.basic.wordsize_tree_set import WordsizeTreeSet

n, q = map(int, input().split())
s = input()
T = WordsizeTreeSet(n, [i for i, c in enumerate(s) if c == "1"])
ans = []
for _ in range(q):
    c, k = map(int, input().split())
    if c == 0:
        T.add(k)
    elif c == 1:
        T.discard(k)
    elif c == 2:
        ans.append("1" if k in T else "0")
    elif c == 3:
        ans.append(str(T.ge(k)))
    else:
        ans.append(str(T.le(k)))

for k in ans:
    print(k)
