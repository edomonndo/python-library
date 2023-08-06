# https://qiita.com/Pro_ktmr/items/4e1e051ea0561772afa3


class HeavyLightDecomposition:
    def __init__(self, n, tree, parent, v_bfs_order):
        self.n = n  # 頂点数
        self.tree = tree  # 子頂点のリスト
        self.parent = parent  # 親頂点のリスト
        self.v_bfs_order = v_bfs_order  # 根からBFS順で辿った時の順番

        # 頂点を根とした部分木の頂点数
        # 部分木の頂点数を重みとする
        size = [1] * n
        for v in v_bfs_order[1:][::-1]:
            size[parent[v]] += size[v]
        self.size = size

        # 頂点から根までの距離(先祖の頂点数)
        ancestor = [0] * n
        for v in v_bfs_order[1:]:
            ancestor[v] = ancestor[parent[v]] + 1
        self.ancestor = ancestor

        # Heavyな辺を辿る
        # H[v] :=　頂点vが次に連結する頂点番号(存在しない場合-1)
        H = [-1] * n
        for v in range(n):
            max_size, max_v = -1, -1
            max_idx = -1
            for idx, u in enumerate(tree[v]):
                if size[u] > max_size:
                    max_size = size[u]
                    max_v = u
                    max_idx = idx
            if max_idx != len(tree[v]) - 1:
                tree[v][-1], tree[v][max_idx] = (
                    tree[v][max_idx],
                    tree[v][-1],
                )
            H[v] = max_v

        root_in_group = [0] * n
        depth = [0] * n
        group = [[0]]
        group_id = [0] * n
        depth_in_group = [0] * n

        c = 1
        for cur in v_bfs_order[1:]:
            par = parent[cur]
            if cur == H[par]:
                root_in_group[cur] = root_in_group[par]
                depth[cur] = depth[par]
                group_id[cur] = group_id[par]
                depth_in_group[cur] = depth_in_group[par] + 1
                group[group_id[cur]].append(cur)
            else:
                root_in_group[cur] = cur
                depth[cur] = depth[par] + 1
                group_id[cur] = c
                group.append([cur])
                c += 1

        self.root_in_group = root_in_group  # 頂点vが含まれる連結成分の先祖頂点
        self.depth = depth  # 最もheavyな連結成分から自身の連結成分への深さ
        self.group = group  # i番目の連結成分
        self.group_id = group_id  # 頂点vが含まれる連結成分のindex
        self.depth_in_group = depth_in_group  # 連結成分内の先祖頂点からの深さ（距離）

        # Euler Tour
        v0 = v_bfs_order[0]
        stack = [~v0, v0]
        ct = -1
        ET = []
        ET1 = [0] * n
        ET2 = [0] * n
        while stack:
            v = stack.pop()
            if v < 0:
                ET2[~v] = ct
                continue
            if v >= 0:
                ET.append(v)
                ct += 1
                if ET1[v] == 0:
                    ET1[v] = ct
            for u in tree[v]:
                for k in range(len(tree[u])):
                    if tree[u][k] == v:
                        del tree[u][k]
                        break
                stack.append(~u)
                stack.append(u)

        self.ET = ET  # 訪れた頂点を行きがけ順で配置
        self.ET1 = ET1  # 頂点vを訪れた順番（行きがけ順）
        self.ET2 = ET2  # 頂点vを訪れた順番（帰りがけ順）

    def path(self, s, t):
        ET1 = self.ET1
        depth, root_in_group = self.depth, self.root_in_group
        parent = self.parent

        L = []
        R = []
        while depth[s] > depth[t]:
            ns = root_in_group[s]
            L.append((ET1[s], ET1[ns]))
            s = parent[ns]

        while depth[t] > depth[s]:
            nt = root_in_group[t]
            R.append((ET1[nt], ET1[t]))
            t = parent[nt]

        while root_in_group[s] != root_in_group[t]:
            ns = root_in_group[s]
            L.append((ET1[s], ET1[ns]))
            s = parent[ns]

            nt = root_in_group[t]
            R.append((ET1[nt], ET1[t]))
            t = parent[nt]

        L.append((ET1[s], ET1[t]))
        return L + R[::-1]

    def path_ranges(self, s, t):
        L = []
        for a, b in self.path(s, t):
            if a > b:
                a, b = b, a
            L.append((a, b + 1))
        return L

    def subtree_range(self, s):
        ET1, ET2 = self.ET1, self.ET2
        a, b = ET1[s], ET2[s]
        return (a, b + 1)

    def path_e(self, s, t):
        ET1 = self.ET1
        depth, root_in_group = self.depth, self.root_in_group
        parent = self.parent

        L = []
        R = []
        while depth[s] > depth[t]:
            ns = root_in_group[s]
            L.append((ET1[s], ET1[ns]))
            s = parent[ns]

        while depth[t] > depth[s]:
            nt = root_in_group[t]
            R.append((ET1[nt], ET1[t]))
            t = parent[nt]

        while root_in_group[s] != root_in_group[t]:
            ns = root_in_group[s]
            L.append((ET1[s], ET1[ns]))
            s = parent[ns]

            nt = root_in_group[t]
            R.append((ET1[nt], ET1[t]))
            t = parent[nt]

        ss, tt = ET1[s], ET1[t]
        if ss < tt:
            L.append((ss + 1, tt))
        elif tt < ss:
            L.append((tt + 1, ss))
        return L + R[::-1]

    def path_ranges_e(self, s, t):
        L = []
        for a, b in self.path_e(s, t):
            if a > b:
                a, b = b, a
            L.append((a, b + 1))
        return L

    def subtree_range_e(self, s):
        ET1, ET2 = self.ET1, self.ET2
        a, b = ET1[s], ET2[s]
        return (a + 1, b + 1)
