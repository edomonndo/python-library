# verification-helper: IGNORE


if __name__ == "__main__":
    from pathlib import Path
    import sys

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
    from data_structure.segment_tree import Segtree
    from tree.euler_tour import EulerTour

    N = 6
    G = [[] for _ in range(N)]
    edges = [(0, 1, 1), (0, 5, 16), (1, 2, 2), (1, 4, 8), (2, 3, 4)]
    Vs = [1, 2, 4, 8, 16, 32]
    for u, v, w in edges:
        G[u].append((w, v))
        G[v].append((w, u))
    root = 0
    et = EulerTour(N, G, root, Vs)

    assert et.ET == [0, 1, 2, 3, -3, -2, 4, -4, -1, 5, -5, 0], et.ET
    assert et.into == [0, 1, 2, 3, 6, 9], et.into
    assert et.out == [11, 8, 5, 4, 7, 10], et.out
    assert et.depth == [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (2, 2),
        (1, 1),
        (2, 4),
        (1, 1),
        (0, 0),
        (1, 5),
        (0, 0),
        (0, -1),
    ], et.depth
    assert et.vcost == [1, 2, 4, 8, -8, -4, 16, -16, -2, 32, -32, -1], et.vcost
    assert et.ecost == [0, 1, 2, 4, -4, -2, 8, -8, -1, 16, -16, 0], et.ecost
    assert et.vcost_st == [1, 2, 4, 8, 0, 0, 16, 0, 0, 32, 0, 0], et.vcost_st
    assert et.ecost_st == [0, 1, 2, 4, 0, 0, 8, 0, 0, 16, 0, 0], et.ecost_st

    # Range Sum Query1 頂点vを根とする部分木の頂点の値の和
    SegRSQ1 = Segtree(et.vcost_st, (lambda x, y: x + y), 0)
    v = 1
    l, r = et.into[v], et.out[v]
    assert SegRSQ1.prod(l, r) == 30, SegRSQ1.prod(l, r)

    # Range Sum Query2 頂点vを根とする部分木の辺の値の和
    SegRSQ2 = Segtree(et.ecost_st, (lambda x, y: x + y), 0)
    v = 1
    l, r = et.into[v] + 1, et.out[v]
    assert SegRSQ2.prod(l, r) == 14, SegRSQ2.prod(l, r)

    # Path Query1 根から頂点vまでの頂点の値の和
    SegPQ1 = Segtree(et.vcost, (lambda x, y: x + y), 0)
    v = 4
    assert SegPQ1.prod(0, et.into[v] + 1) == 19, SegPQ1.prod(0, et.into[v] + 1)

    # Path Query2 根から頂点vまでの辺の値の和
    SegPQ2 = Segtree(et.ecost, (lambda x, y: x + y), 0)
    v = 4
    assert SegPQ2.prod(0, et.into[v] + 1) == 9, SegPQ2.prod(0, et.into[v] + 1)

    # 頂点u,vのLCA
    # (depth, v)で返る。最小のdepthに対するvがLCA
    SegLca = Segtree(et.depth, min, (10**9, N))
    u, v = 2, 5
    if u == v:
        pass
    else:
        l, r = et.into[u], et.into[v]
        if l > r:
            l, r = r, l
        assert SegLca.prod(l, r + 1) == (0, 0), SegLca.prod(l, r + 1)
