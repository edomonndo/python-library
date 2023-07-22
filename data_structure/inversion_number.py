class BIT:
    # 初期化
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)  # 1-indexのリストで管理

    # 加算
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i  # LSBの計算

    # インデックス0からiまでの総和を計算
    def sum(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i  # LSBの計算

        return total


def inversionNumberByBIT(A, mod=10**9):
    ans = 0
    Bit = BIT(len(A))  # Binary Indexed Tree
    for i, a in enumerate(A):
        ans += i - Bit.sum(a)
        ans %= mod
        Bit.add(a, 1)  # 自分の位置を1にする
    return ans
