class MoState:
    def __init__(self, max_value):
        self.cnt = [0] * (max_value + 1)
        self.res = 0

    def add(self, x):
        "区間の端に x を追加するときの処理"
        self.cnt[x] += 1
        # ToDo
        pass

    def delete(self, x):
        "区間の端から x を削除するときの処理"
        self.cnt[x] -= 1
        # ToDo
        pass


class Mo:
    def __init__(self, arr, state: MoState):
        self.arr = arr
        self.qs = []
        self.n_min = 10**9
        self.n_max = -(10**9)
        self.state = state

    def add_query(self, l, r):
        """[l, r)"""
        self.qs.append((l, r))
        self.n_min = min(self.n_min, l)
        self.n_max = max(self.n_max, r)

    def calc(self):
        max_value = max(self.arr)
        state = self.state

        n_min, n_max = self.n_min, self.n_max
        N = n_max - n_min
        qs = self.qs
        Q = len(qs)
        shift = Q.bit_length()
        mask = (1 << shift) - 1
        block_cnt = max(1, int(min(N, Q**0.5)))
        block_size = (N + block_cnt - 1) // block_cnt
        buckets = [[] for _ in range(block_cnt)]
        for i, (l, r) in enumerate(qs):
            l -= n_min
            r -= n_min
            bi = l // block_size
            x = -r if bi & 1 else r
            x = (x << shift) | i
            buckets[bi].append(x)
        for i in range(block_cnt):
            buckets[i].sort()
        ans = [-1] * Q
        l = r = qs[0][0]
        for b in buckets:
            for ri in b:
                i = ri & mask
                L, R = qs[i]
                "クエリのために区間を伸縮させる"
                while r < R:
                    state.add(self.arr[r])
                    r += 1
                while r > R:
                    r -= 1
                    state.delete(self.arr[r])
                while l < L:
                    state.delete(self.arr[l])
                    l += 1
                while l > L:
                    l -= 1
                    state.add(self.arr[l])
                ans[i] = state.res
        return ans
