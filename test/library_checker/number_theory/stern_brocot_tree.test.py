# verification-helper: PROBLEM https://judge.yosupo.jp/problem/stern_brocot_tree

from number_theory.stern_brocot_tree import SternBrocotTree

t = int(input())
SBT = SternBrocotTree
for _ in range(t):
    s, *qu = input().split()
    if s == "ENCODE_PATH":
        a, b = map(int, qu)
        code = SBT.encode(a, b)
        ans = []
        for is_right, k in code:
            if is_right:
                ans += ["R", str(k)]
            else:
                ans += ["L", str(k)]
        print(len(ans) // 2, *ans)
    elif s == "DECODE_PATH":
        code = []
        size = int(qu[0])
        for i in range(1, size * 2, 2):
            d = qu[i]
            k = int(qu[i + 1])
            code.append((d == "R", k))
        a, b = SBT.decode(code)
        print(a, b)
    elif s == "LCA":
        a, b, c, d = map(int, qu)
        f, g = SBT.lca(a, b, c, d)
        print(f, g)
    elif s == "ANCESTOR":
        k, a, b = map(int, qu)
        f, g = SBT.ancestor(a, b, k, (-1, -1))
        if f == -1:
            print(-1)
        else:
            print(f, g)
    elif s == "RANGE":
        a, b = map(int, qu)
        f, g, h, k = SBT.range(a, b)
        print(f, g, h, k)
