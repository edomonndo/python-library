class MoState:
    def __init__(self,max_value):
        self.cnt=[0]*(max_value+1)
        self.res=0
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

class Mo():
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.qs = []

    def add_query(self, l, r):
        self.qs.append((l, r))

    def _init_states(self):
        max_value=max(self.arr)
        self.state=MoState(max_value)
        self.l = 0
        self.r = 0

    def _one_process(self, l, r):
        "クエリのために区間を伸縮させる"
        while l < self.l:
            self.l -= 1
            self.state.add(self.arr[self.l])
        while self.r < r:
            self.r += 1
            self.state.add(self.arr[self.r - 1])
        while self.l < l:
            self.state.delete(self.arr[self.l])
            self.l += 1
        while r < self.r:
            self.state.delete(self.arr[self.r - 1])
            self.r -= 1

    def calc(self):
        self._init_states()

        qs = self.qs
        qsize = len(qs)
        self.b = block_size = int((qsize-1)**0.5)+1
        t = (self.n + block_size - 1) // block_size
        self.buckets = [[] for b in range(t)]
        for i,(l,r) in enumerate(qs):
            self.buckets[l // self.b].append((r, l, i))
       
        ans = [-1] * qsize
        for i,b in enumerate(self.buckets):
            b.sort(reverse=i&1)
            for r,l,j in b:
                self._one_process(l, r)
                ans[j] = self.state.res
        return ans