# verification-helper: PROBLEM https://atcoder.jp/contests/abc242/tasks/abc242_g


from data_structure.mo import Mo


class MoState:
    def __init__(self, max_value):
        self.cnt = [0] * (max_value + 1)
        self.res = 0

    def add(self, x):
        "区間の端に x を追加するときの処理"
        self.cnt[x] += 1
        # ToDo
        if self.cnt[x] & 1 == 0:
            self.res += 1

    def delete(self, x):
        "区間の端から x を削除するときの処理"
        self.cnt[x] -= 1
        # ToDo
        if self.cnt[x] & 1:
            self.res -= 1


N = int(input())
A = [int(x) for x in input().split()]
Q = int(input())
state = MoState(max(A))
mo = Mo(A, state)
for _ in range(Q):
    l, r = map(int, input().split())
    mo.add_query(l - 1, r)

ans = mo.calc()
print(*ans, sep="\n")
