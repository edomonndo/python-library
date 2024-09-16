# verification-helper: PROBLEM https://judge.yosupo.jp/problem/palindromes_in_deque

from str.palindromic_tree_deque import DequePalindromicTree

q = int(input())
PT = DequePalindromicTree(q, "a", 26)
for _ in range(q):
    t, *qu = input().split()
    if t == "0":
        PT.appendleft(qu[0])
    elif t == "1":
        PT.append(qu[0])
    elif t == "2":
        PT.popleft()
    elif t == "3":
        PT.pop()
    print(
        PT.distinct(),
        PT.max_prefix_size(),
        PT.max_suffix_size(),
    )
