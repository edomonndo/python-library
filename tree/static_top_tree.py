from typing import TypeVar, Callable

Path = TypeVar("Path")
Point = TypeVar("Point")


class StaticTopTree:
    def __init__(
        self,
        # 頂点 v のみからなる path cluster を生成する.
        vertex: Callable[[int], Path],
        # path cluster t に virtual な根を生やして point cluster にする.
        add_edge: Callable[[Path], Point],
        # point cluster t の根に頂点 v を代入して path cluster にする.
        add_vertex: Callable[[Path], Point],
        # path cluster p,c (p が根に近い側にある) をマージする.
        compress: Callable[[Path, Path], Path],
        # point cluster x,y をマージする.
        rake: Callable[[Point, Point], Point],
        e_path: Path,
        e_point: Point,
        children: list[list[int]],
    ):
        """
        vertex:0
        add_edge:1
        add_vertex:2
        compress:3
        rake:4
        """
        self.vertex = vertex
        self.add_edge = add_edge
        self.add_vertex = add_vertex
        self.compress = compress
        self.rake = rake

        self.n = n = len(children)
        self.children = children
        self.parent = [-1] * (4 * n)
        self.L = [-1] * (4 * n)
        self.R = [-1] * (4 * n)
        self.add_buff = n
        self.vtype = [-1] * (4 * n)
        self.stt_root = -1
        self.path_cluster_val = [e_path for _ in range(4 * n)]
        self.point_cluster_val = [e_point for _ in range(4 * n)]

        self.__build()

    def __calc_heavy_edge(self) -> None:
        n = self.n
        children = self.children
        st = [0]
        sz = [1] * n
        while st:
            v = st.pop()
            if v >= 0:
                st.append(~v)
                for nv in children[v]:
                    st.append(nv)
            else:
                v = ~v
                max_size = 0
                for i in range(len(children[v])):
                    nv = children[v][i]
                    sz[v] += sz[nv]
                    if sz[nv] > max_size:
                        max_size = sz[nv]
                        children[v][0], children[v][i] = children[v][i], children[v][0]

    def __add_stt_vertex(self, vid: int, lid: int, rid: int, vtype: int) -> int:
        if vid == -1:
            vid = self.add_buff
            self.add_buff += 1
        self.L[vid] = lid
        self.R[vid] = rid
        self.vtype[vid] = vtype

        if lid != -1:
            self.parent[lid] = vid
        if rid != -1:
            self.parent[rid] = lid

        return vid

    def __merge(self, chs: list[int], vtype: int) -> tuple[int, int]:
        if len(chs) == 1:
            return chs[0]

        sz_sum = sum(sz for _, sz in chs)
        left_chs, right_chs = [], []
        for i, sz in chs:
            if sz < sz_sum:
                left_chs.append((i, sz))
            else:
                right_chs.append((i, sz))
            sz_sum -= 2 * sz

        i, si = self.__merge(left_chs, vtype)
        j, sj = self.__merge(right_chs, vtype)
        return (self.__add_stt_vertex(-1, i, j, vtype), si + sj)

    def __compress(self, v: int) -> tuple[int, int]:
        chs = [self.__add_vertex(v)]
        children = self.children
        while children[v]:
            v = children[v][0]
            chs.append(self.__add_vertex(v))

        return self.__merge(chs, 3)

    def __rake(self, v: int) -> tuple[int, int]:
        chs = [self.__add_edge(cv) for cv in self.children[v][1:]]
        if len(chs) == 0:
            return (-1, 0)
        else:
            return self.__merge(chs, 4)

    def __add_edge(self, v: int) -> tuple[int, int]:
        j, sj = self.__compress(v)
        return (self.__add_stt_vertex(-1, j, -1, 1), sj)

    def __add_vertex(self, v) -> tuple[int, int]:
        j, sj = self.__rake(v)
        if j == -1:
            return (self.__add_stt_vertex(v, j, -1, 0), sj + 1)
        else:
            return (self.__add_stt_vertex(v, j, -1, 2), sj + 1)

    def __build(self) -> None:
        self.__calc_heavy_edge()
        i, _ = self.__compress(0)
        self.stt_root = i

        L, R = self.L, self.R
        stack = [~i, i]
        while stack:
            k = stack.pop()
            if k < 0:
                self.update(~k)
                continue
            l, r = L[k], R[k]
            if l != -1:
                stack += [~l, l]
            if r != -1:
                stack += [~r, r]

    def update(self, k: int) -> None:
        t = self.vtype[k]
        if t == 0:
            self.path_cluster_val[k] = self.vertex(k)
        elif t == 1:
            self.point_cluster_val[k] = self.add_edge(self.path_cluster_val[self.L[k]])
        elif t == 2:
            self.path_cluster_val[k] = self.add_vertex(
                self.point_cluster_val[self.L[k]], k
            )
        elif t == 3:
            self.path_cluster_val[k] = self.compress(
                self.path_cluster_val[self.L[k]], self.path_cluster_val[self.R[k]]
            )
        elif t:
            self.point_cluster_val[k] = self.rake(
                self.point_cluster_val[self.L[k]], self.point_cluster_val[self.R[k]]
            )

    def solve(self) -> Path:
        return self.path_cluster_val[self.stt_root]
