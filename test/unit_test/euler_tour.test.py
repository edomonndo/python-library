# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A


if __name__ == "__main__":
    from pathlib import Path
    import sys

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
    from tree.euler_tour import EulerTour

    N = 6
    G = [[] for _ in range(N)]
    edges = [(0, 1, 1), (0, 5, 16), (1, 2, 2), (1, 4, 8), (2, 3, 4)]
    Vs = [1, 2, 4, 8, 16, 32]
    for u, v, w in edges:
        G[u].append((v, w))
        G[v].append((u, w))
    root = 0
    et = EulerTour(G, root, Vs)

    assert et.ET == [0, 5, 0, 1, 4, 1, 2, 3, 2, 1, 0], et.ET
    assert et.into == [0, 3, 6, 7, 4, 1], et.into
    assert et.out == [11, 10, 9, 8, 5, 2], et.out
    assert et.depth == [0, 1, 2, 3, 2, 1, 6], et.depth
    assert et.vcost == [1, 32, -32, 2, 16, -16, 4, 8, -8, -4, -2], et.vcost
    assert et.ecost == [0, 16, -16, 1, 8, -8, 2, 4, -4, -2, -1], et.ecost
    assert et.vcost_st == [1, 32, 0, 2, 16, 0, 4, 8, 0, 0, 0], et.vcost_st
    assert et.ecost_st == [0, 16, 0, 1, 8, 0, 2, 4, 0, 0, 0], et.ecost_st

    # Range Sum Query1 頂点vを根とする部分木の頂点の値の和
    assert et.subtree_verticle_sum(0) == 63, et.subtree_verticle_sum(0)
    assert et.subtree_verticle_sum(1) == 30, et.subtree_verticle_sum(1)
    assert et.subtree_verticle_sum(2) == 12, et.subtree_verticle_sum(2)
    assert et.subtree_verticle_sum(3) == 8, et.subtree_verticle_sum(3)
    assert et.subtree_verticle_sum(4) == 16, et.subtree_verticle_sum(4)
    assert et.subtree_verticle_sum(5) == 32, et.subtree_verticle_sum(5)

    # Range Sum Query2 頂点vを根とする部分木の辺の値の和
    assert et.subtree_edge_sum(0) == 31, et.subtree_edge_sum(0)
    assert et.subtree_edge_sum(1) == 14, et.subtree_edge_sum(1)
    assert et.subtree_edge_sum(2) == 4, et.subtree_edge_sum(2)
    assert et.subtree_edge_sum(3) == 0, et.subtree_edge_sum(3)
    assert et.subtree_edge_sum(4) == 0, et.subtree_edge_sum(4)
    assert et.subtree_edge_sum(5) == 0, et.subtree_edge_sum(5)

    # Path Query1 根から頂点vまでの頂点の値の和
    assert et.path_verticle_sum(0) == 1, et.path_verticle_sum(0)
    assert et.path_verticle_sum(1) == 3, et.path_verticle_sum(1)
    assert et.path_verticle_sum(2) == 7, et.path_verticle_sum(2)
    assert et.path_verticle_sum(3) == 15, et.path_verticle_sum(3)
    assert et.path_verticle_sum(4) == 19, et.path_verticle_sum(4)
    assert et.path_verticle_sum(5) == 33, et.path_verticle_sum(5)

    # Path Query2 根から頂点vまでの辺の値の和
    assert et.path_edge_sum(0) == 0, et.path_edge_sum(0)
    assert et.path_edge_sum(1) == 1, et.path_edge_sum(1)
    assert et.path_edge_sum(2) == 3, et.path_edge_sum(2)
    assert et.path_edge_sum(3) == 7, et.path_edge_sum(3)
    assert et.path_edge_sum(4) == 9, et.path_edge_sum(4)
    assert et.path_edge_sum(5) == 16, et.path_edge_sum(5)

    # 頂点u,vのLCA
    for u in range(6):
        for v in range(6):
            if u == v:
                assert et.lca(u, v) == u, et.lca(u, v)
            elif u == 0 or v == 0:
                assert et.lca(u, v) == 0, et.lca(u, v)
            elif u == 5 or v == 5:
                assert et.lca(u, v) == 0, et.lca(u, v)
            elif u == 1 or v == 1:
                assert et.lca(u, v) == 1, et.lca(u, v)
            elif (u == 2 and v == 3) or (v == 2 and u == 3):
                assert et.lca(u, v) == 2, et.lca(u, v)
            elif (u == 2 and v == 4) or (v == 2 and u == 4):
                assert et.lca(u, v) == 1, et.lca(u, v)
            elif (u == 3 and v == 4) or (v == 3 and u == 4):
                assert et.lca(u, v) == 1, et.lca(u, v)
            else:
                assert False

    # 辺の重みを更新
    ediff = 1
    et.update_parent_edge(2, 2 + ediff)

    assert et.subtree_edge_sum(0) == 31 + ediff, et.subtree_edge_sum(0)
    assert et.subtree_edge_sum(1) == 14 + ediff, et.subtree_edge_sum(1)
    assert et.subtree_edge_sum(2) == 4, et.subtree_edge_sum(2)
    assert et.subtree_edge_sum(3) == 0, et.subtree_edge_sum(3)
    assert et.subtree_edge_sum(4) == 0, et.subtree_edge_sum(4)
    assert et.subtree_edge_sum(5) == 0, et.subtree_edge_sum(5)

    assert et.path_edge_sum(0) == 0, et.path_edge_sum(0)
    assert et.path_edge_sum(1) == 1, et.path_edge_sum(1)
    assert et.path_edge_sum(2) == 3 + ediff, et.path_edge_sum(2)
    assert et.path_edge_sum(3) == 7 + ediff, et.path_edge_sum(3)
    assert et.path_edge_sum(4) == 9, et.path_edge_sum(4)
    assert et.path_edge_sum(5) == 16, et.path_edge_sum(5)

    # 頂点の重みを更新
    vdiff = 1
    et.update_verticle(2, 4 + vdiff)

    assert et.subtree_verticle_sum(0) == 63 + vdiff, et.subtree_verticle_sum(0)
    assert et.subtree_verticle_sum(1) == 30 + vdiff, et.subtree_verticle_sum(1)
    assert et.subtree_verticle_sum(2) == 12 + vdiff, et.subtree_verticle_sum(2)
    assert et.subtree_verticle_sum(3) == 8, et.subtree_verticle_sum(3)
    assert et.subtree_verticle_sum(4) == 16, et.subtree_verticle_sum(4)
    assert et.subtree_verticle_sum(5) == 32, et.subtree_verticle_sum(5)

    assert et.path_verticle_sum(0) == 1, et.path_verticle_sum(0)
    assert et.path_verticle_sum(1) == 3, et.path_verticle_sum(1)
    assert et.path_verticle_sum(2) == 7 + vdiff, et.path_verticle_sum(2)
    assert et.path_verticle_sum(3) == 15 + vdiff, et.path_verticle_sum(3)
    assert et.path_verticle_sum(4) == 19, et.path_verticle_sum(4)
    assert et.path_verticle_sum(5) == 33, et.path_verticle_sum(5)

    print("Hello World")
