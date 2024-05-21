class StaticRangeModeQuery:

    def __init__(self, A: list[int]):
        # 座標圧縮(同じ値はindexで識別)
        self.inv_A = sorted(set(A))
        d = {a: i for i, a in enumerate(self.inv_A)}
        self.A = [d[a] for a in A]

        self.n = n = len(self.A)
        self.max_value = max(self.A)
        self.size = size = int(n**0.5) + 1
        self.bucket_cnt = (n + size - 1) // size
        self.data = [self.A[i * size : (i + 1) * size] for i in range(self.bucket_cnt)]

        self.idx = [[] for _ in range(self.max_value + 1)]
        self.inv_idx = [-1] * n
        for i, a in enumerate(self.A):
            self.inv_idx[i] = len(self.idx[a])
            self.idx[a].append(i)
        # list[list[(freq, val)]]
        self.bucket_data = self._calc_bucket()

    def _calc_bucket(self) -> list[list[tuple[int, int]]]:
        data = self.data
        res = [[(0, -1)] * (self.bucket_cnt + 1) for _ in range(self.bucket_cnt + 1)]
        freqs = [0] * (self.max_value + 1)
        for i in range(self.bucket_cnt):
            freq, val = -1, -1
            for j in range(i + 1, self.bucket_cnt + 1):
                for x in data[j - 1]:
                    freqs[x] += 1
                    if freqs[x] > freq:
                        freq, val = freqs[x], x
                res[i][j] = (freq, val)
            for j in range(i + 1, self.bucket_cnt + 1):
                for x in data[j - 1]:
                    freqs[x] = 0
        return res

    def query(self, l: int, r: int) -> tuple[int, int]:
        """(最頻値，頻度)を求めます."""
        assert 0 <= l < r <= self.n
        L, R = l, r
        k1, k2 = l // self.size, r // self.size
        l -= k1 * self.size
        r -= k2 * self.size

        freq, val = 0, -1

        if k1 == k2:
            A, idx, inv_idx = self.A, self.idx, self.inv_idx
            for i in range(L, R):
                x = A[i]
                k = inv_idx[i]
                while k + freq < len(idx[x]) and idx[x][k + freq] < R:
                    freq += 1
                    val = x
        else:
            data, idx, inv_idx = self.data, self.idx, self.inv_idx
            freq, val = self.bucket_data[k1 + 1][k2]

            for i in range(l, len(data[k1])):
                x = data[k1][i]
                k = inv_idx[k1 * self.size + i]
                while k + freq < len(idx[x]) and idx[x][k + freq] < R:
                    freq += 1
                    val = x
            for i in range(r):
                x = data[k2][i]
                k = inv_idx[k2 * self.size + i]
                while 0 <= k - freq and L <= idx[x][k - freq]:
                    freq += 1
                    val = x
        val = self.inv_A[val]
        return val, freq
