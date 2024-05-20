---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/unit_test/heavy_light_decomposition.test.py
    title: test/unit_test/heavy_light_decomposition.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class HeavyLightDecomposition:\n    def __init__(self, n, tree, parent, v_bfs_order):\n\
    \        self.n = n  # \u9802\u70B9\u6570\n        self.tree = tree  # \u5B50\u9802\
    \u70B9\u306E\u30EA\u30B9\u30C8\n        self.parent = parent  # \u89AA\u9802\u70B9\
    \u306E\u30EA\u30B9\u30C8\n        self.v_bfs_order = v_bfs_order  # \u6839\u304B\
    \u3089BFS\u9806\u3067\u8FBF\u3063\u305F\u6642\u306E\u9806\u756A\n\n        # \u9802\
    \u70B9\u3092\u6839\u3068\u3057\u305F\u90E8\u5206\u6728\u306E\u9802\u70B9\u6570\
    \n        # \u90E8\u5206\u6728\u306E\u9802\u70B9\u6570\u3092\u91CD\u307F\u3068\
    \u3059\u308B\n        size = [1] * n\n        for v in v_bfs_order[1:][::-1]:\n\
    \            size[parent[v]] += size[v]\n        self.size = size\n\n        #\
    \ \u9802\u70B9\u304B\u3089\u6839\u307E\u3067\u306E\u8DDD\u96E2(\u5148\u7956\u306E\
    \u9802\u70B9\u6570)\n        ancestor = [0] * n\n        for v in v_bfs_order[1:]:\n\
    \            ancestor[v] = ancestor[parent[v]] + 1\n        self.ancestor = ancestor\n\
    \n        # Heavy\u306A\u8FBA\u3092\u8FBF\u308B\n        # H[v] :=\u3000\u9802\
    \u70B9v\u304C\u6B21\u306B\u9023\u7D50\u3059\u308B\u9802\u70B9\u756A\u53F7(\u5B58\
    \u5728\u3057\u306A\u3044\u5834\u5408-1)\n        H = [-1] * n\n        for v in\
    \ range(n):\n            max_size, max_v = -1, -1\n            max_idx = -1\n\
    \            for idx, u in enumerate(tree[v]):\n                if size[u] > max_size:\n\
    \                    max_size = size[u]\n                    max_v = u\n     \
    \               max_idx = idx\n            if max_idx != len(tree[v]) - 1:\n \
    \               tree[v][-1], tree[v][max_idx] = (\n                    tree[v][max_idx],\n\
    \                    tree[v][-1],\n                )\n            H[v] = max_v\n\
    \n        root_in_group = [0] * n\n        depth = [0] * n\n        group = [[0]]\n\
    \        group_id = [0] * n\n        depth_in_group = [0] * n\n\n        c = 1\n\
    \        for cur in v_bfs_order[1:]:\n            par = parent[cur]\n        \
    \    if cur == H[par]:\n                root_in_group[cur] = root_in_group[par]\n\
    \                depth[cur] = depth[par]\n                group_id[cur] = group_id[par]\n\
    \                depth_in_group[cur] = depth_in_group[par] + 1\n             \
    \   group[group_id[cur]].append(cur)\n            else:\n                root_in_group[cur]\
    \ = cur\n                depth[cur] = depth[par] + 1\n                group_id[cur]\
    \ = c\n                group.append([cur])\n                c += 1\n\n       \
    \ self.root_in_group = root_in_group  # \u9802\u70B9v\u304C\u542B\u307E\u308C\u308B\
    \u9023\u7D50\u6210\u5206\u306E\u5148\u7956\u9802\u70B9\n        self.depth = depth\
    \  # \u6700\u3082heavy\u306A\u9023\u7D50\u6210\u5206\u304B\u3089\u81EA\u8EAB\u306E\
    \u9023\u7D50\u6210\u5206\u3078\u306E\u6DF1\u3055\n        self.group = group \
    \ # i\u756A\u76EE\u306E\u9023\u7D50\u6210\u5206\n        self.group_id = group_id\
    \  # \u9802\u70B9v\u304C\u542B\u307E\u308C\u308B\u9023\u7D50\u6210\u5206\u306E\
    index\n        self.depth_in_group = depth_in_group  # \u9023\u7D50\u6210\u5206\
    \u5185\u306E\u5148\u7956\u9802\u70B9\u304B\u3089\u306E\u6DF1\u3055\uFF08\u8DDD\
    \u96E2\uFF09\n\n        # Euler Tour\n        v0 = v_bfs_order[0]\n        stack\
    \ = [~v0, v0]\n        ct = -1\n        ET = []\n        ET1 = [0] * n\n     \
    \   ET2 = [0] * n\n        while stack:\n            v = stack.pop()\n       \
    \     if v < 0:\n                ET2[~v] = ct\n                continue\n    \
    \        if v >= 0:\n                ET.append(v)\n                ct += 1\n \
    \               if ET1[v] == 0:\n                    ET1[v] = ct\n           \
    \ for u in tree[v]:\n                for k in range(len(tree[u])):\n         \
    \           if tree[u][k] == v:\n                        del tree[u][k]\n    \
    \                    break\n                stack.append(~u)\n               \
    \ stack.append(u)\n\n        self.ET = ET  # \u8A2A\u308C\u305F\u9802\u70B9\u3092\
    \u884C\u304D\u304C\u3051\u9806\u3067\u914D\u7F6E\n        self.ET1 = ET1  # \u9802\
    \u70B9v\u3092\u8A2A\u308C\u305F\u9806\u756A\uFF08\u884C\u304D\u304C\u3051\u9806\
    \uFF09\n        self.ET2 = ET2  # \u9802\u70B9v\u3092\u8A2A\u308C\u305F\u9806\u756A\
    \uFF08\u5E30\u308A\u304C\u3051\u9806\uFF09\n\n    def path(self, s, t):\n    \
    \    ET1 = self.ET1\n        depth, root_in_group = self.depth, self.root_in_group\n\
    \        parent = self.parent\n\n        L = []\n        R = []\n        while\
    \ depth[s] > depth[t]:\n            ns = root_in_group[s]\n            L.append((ET1[s],\
    \ ET1[ns]))\n            s = parent[ns]\n\n        while depth[t] > depth[s]:\n\
    \            nt = root_in_group[t]\n            R.append((ET1[nt], ET1[t]))\n\
    \            t = parent[nt]\n\n        while root_in_group[s] != root_in_group[t]:\n\
    \            ns = root_in_group[s]\n            L.append((ET1[s], ET1[ns]))\n\
    \            s = parent[ns]\n\n            nt = root_in_group[t]\n           \
    \ R.append((ET1[nt], ET1[t]))\n            t = parent[nt]\n\n        L.append((ET1[s],\
    \ ET1[t]))\n        return L + R[::-1]\n\n    def path_ranges(self, s, t):\n \
    \       L = []\n        for a, b in self.path(s, t):\n            if a > b:\n\
    \                a, b = b, a\n            L.append((a, b + 1))\n        return\
    \ L\n\n    def subtree_range(self, s):\n        ET1, ET2 = self.ET1, self.ET2\n\
    \        a, b = ET1[s], ET2[s]\n        return (a, b + 1)\n\n    def path_e(self,\
    \ s, t):\n        ET1 = self.ET1\n        depth, root_in_group = self.depth, self.root_in_group\n\
    \        parent = self.parent\n\n        L = []\n        R = []\n        while\
    \ depth[s] > depth[t]:\n            ns = root_in_group[s]\n            L.append((ET1[s],\
    \ ET1[ns]))\n            s = parent[ns]\n\n        while depth[t] > depth[s]:\n\
    \            nt = root_in_group[t]\n            R.append((ET1[nt], ET1[t]))\n\
    \            t = parent[nt]\n\n        while root_in_group[s] != root_in_group[t]:\n\
    \            ns = root_in_group[s]\n            L.append((ET1[s], ET1[ns]))\n\
    \            s = parent[ns]\n\n            nt = root_in_group[t]\n           \
    \ R.append((ET1[nt], ET1[t]))\n            t = parent[nt]\n\n        ss, tt =\
    \ ET1[s], ET1[t]\n        if ss < tt:\n            L.append((ss + 1, tt))\n  \
    \      elif tt < ss:\n            L.append((tt + 1, ss))\n        return L + R[::-1]\n\
    \n    def path_ranges_e(self, s, t):\n        L = []\n        for a, b in self.path_e(s,\
    \ t):\n            if a > b:\n                a, b = b, a\n            L.append((a,\
    \ b + 1))\n        return L\n\n    def subtree_range_e(self, s):\n        ET1,\
    \ ET2 = self.ET1, self.ET2\n        a, b = ET1[s], ET2[s]\n        return (a +\
    \ 1, b + 1)\n"
  dependsOn: []
  isVerificationFile: false
  path: tree/heavy_light_decomposition.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/unit_test/heavy_light_decomposition.test.py
documentation_of: tree/heavy_light_decomposition.py
layout: document
title: "HL\u5206\u89E3"
---

木の高さを圧縮する.

https://qiita.com/Pro_ktmr/items/4e1e051ea0561772afa3


