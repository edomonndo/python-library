# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_reverse_range_sum

from data_structure.binary_search_tree.implicit_treap import ImplicitTreap

n, q = map(int, input().split())
A = [int(x) for x in input().split()]

T = ImplicitTreap(lambda x, y: x + y, 0, lambda f, x: x, lambda f, g: g, 0, A)

ans = []
for _ in range(q):
    t, l, r = map(int, input().split())
    if t == 0:
        T.reverse(l, r)
    else:
        ans.append(T.prod(l, r))
print(*ans, sep="\n")
