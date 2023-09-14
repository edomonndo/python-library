class SparseTable:
    def __init__(self, arr, op):
        bit_length = 0
        n = len(arr)
        while (1 << bit_length) <= n:
            bit_length += 1
        table = [[0] * n for _ in range(bit_length)]
        table[0] = arr[:]
        for i in range(1, bit_length):
            j = 0
            while j + (1 << i) <= n:
                table[i][j] = op(table[i - 1][j], table[i - 1][j + (1 << (i - 1))])
                j += 1
        lookup = [0] * (n + 1)
        for i in range(2, n + 1):
            lookup[i] = lookup[i >> 1] + 1

        self.n = n
        self.op = op
        self.table = table
        self.lookup = lookup

    def query(self, l, r):
        assert 0 <= l and r <= self.n
        assert l < r
        b = self.lookup[r - l]
        return self.op(self.table[b][l], self.table[b][r - (1 << b)])