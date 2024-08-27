from typing import NamedTuple, Optional


class MaxFlow:
    class Edge(NamedTuple):
        src: int
        dst: int
        cap: int
        flow: int

    class _Edge:
        def __init__(self, dst: int, cap: int) -> None:
            self.dst = dst
            self.cap = cap
            self.rev: Optional[MaxFlow._Edge] = None

    def __init__(self, n: int) -> None:
        self._n = n
        self._g: list[list[MaxFlow._Edge]] = [[] for _ in range(n)]
        self._edges: list[MaxFlow._Edge] = []

    def add_edge(self, src: int, dst: int, cap: int) -> int:
        assert 0 <= src < self._n
        assert 0 <= dst < self._n
        assert 0 <= cap
        m = len(self._edges)
        e = MaxFlow._Edge(dst, cap)
        re = MaxFlow._Edge(src, 0)
        e.rev = re
        re.rev = e
        self._g[src].append(e)
        self._g[dst].append(re)
        self._edges.append(e)
        return m

    def get_edge(self, i: int) -> Edge:
        assert 0 <= i < len(self._edges)
        e = self._edges[i]
        re = e.rev
        return MaxFlow.Edge(re.dst, e.dst, e.cap + re.cap, re.cap)

    def edges(self) -> list[Edge]:
        return [self.get_edge(i) for i in range(len(self._edges))]

    def change_edge(self, i: int, new_cap: int, new_flow: int) -> None:
        assert 0 <= i < len(self._edges)
        assert 0 <= new_flow <= new_cap
        e = self._edges[i]
        e.cap = new_cap - new_flow
        assert e.rev is not None
        e.rev.cap = new_flow

    def flow(self, s: int, t: int, flow_limit: Optional[int] = None) -> int:
        assert 0 <= s < self._n
        assert 0 <= t < self._n
        assert s != t
        if flow_limit is None:
            flow_limit = sum(e.cap for e in self._g[s])

        current_edge = [0] * self._n
        level = [0] * self._n

        def bfs() -> bool:
            for i in range(self._n):
                level[i] = self._n
            queue = []
            q_front = 0
            queue.append(s)
            level[s] = 0
            while q_front < len(queue):
                v = queue[q_front]
                q_front += 1
                next_level = level[v] + 1
                for e in self._g[v]:
                    if e.cap == 0 or level[e.dst] <= next_level:
                        continue
                    level[e.dst] = next_level
                    if e.dst == t:
                        return True
                    queue.append(e.dst)
            return False

        def dfs(lim: int) -> int:
            st = []
            edge_st: list[MaxFlow._Edge] = []
            st.append(t)
            while st:
                v = st[-1]
                if v == s:
                    flow = min(lim, min(e.cap for e in edge_st))
                    for e in edge_st:
                        e.cap -= flow
                        assert e.rev is not None
                        e.rev.cap += flow
                    return flow
                next_level = level[v] - 1
                while current_edge[v] < len(self._g[v]):
                    e = self._g[v][current_edge[v]]
                    re = e.rev
                    if level[e.dst] != next_level or re.cap == 0:
                        current_edge[v] += 1
                        continue
                    st.append(e.dst)
                    edge_st.append(re)
                    break
                else:
                    st.pop()
                    if edge_st:
                        edge_st.pop()
                    level[v] = self._n
            return 0

        flow = 0
        while flow < flow_limit:
            if not bfs():
                break
            for i in range(self._n):
                current_edge[i] = 0
            while flow < flow_limit:
                f = dfs(flow_limit - flow)
                flow += f
                if f == 0:
                    break
        return flow

    def min_cut(self, s: int) -> list[bool]:
        visited = [False] * self._n
        st = [s]
        visited[s] = True
        while st:
            v = st.pop()
            for e in self._g[v]:
                if e.cap > 0 and not visited[e.dst]:
                    visited[e.dst] = True
                    st.append(e.dst)
        return visited
