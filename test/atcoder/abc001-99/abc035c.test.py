# verification-helper: PROBLEM https://atcoder.jp/contests/abc035/tasks/abc035_c
from atcoder.lazysegtree import LazySegTree


def mapping(f, x):
    return not x if f else x


def composition(g, f):
    return g ^ f


ID = 0

n, q = map(int, input().split())
st = LazySegTree(max, -1, mapping, composition, ID, [0] * n)

for _ in range(q):
    l, r = map(int, input().split())
    st.apply(l - 1, r, 1)

print("".join("1" if st.get(i) else "0" for i in range(n)))
