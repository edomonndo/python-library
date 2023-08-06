# verification-helper: IGNORE

if __name__ == "__main__":
    from pathlib import Path
    import sys

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
    from tree.heavy_light_decomposition import HeavyLightDecomposition

    N = 12
    tree = [[1, 6, 10], [2, 5], [3, 4], [], [], [], [7], [8, 9], [], [], [11], []]
    parent = [-1, 0, 1, 2, 2, 1, 0, 6, 7, 7, 0, 10]
    v_bfs_order = [0, 1, 6, 10, 2, 5, 7, 11, 3, 4, 8, 9]
    hld = HeavyLightDecomposition(N, tree, parent, v_bfs_order)

    assert hld.size == [12, 5, 3, 1, 1, 1, 4, 3, 1, 1, 2, 1]
    assert hld.ancestor == [0, 1, 2, 3, 3, 2, 1, 2, 3, 3, 1, 2]
    assert hld.root_in_group == [0, 0, 0, 0, 4, 5, 6, 6, 6, 9, 10, 10]
    assert hld.depth == [0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 1, 1], hld.depth
    assert hld.group == [[0, 1, 2, 3], [6, 7, 8], [10, 11], [5], [4], [9]]
    assert hld.group_id == [0, 0, 0, 0, 4, 3, 1, 1, 1, 5, 2, 2]
    assert hld.depth_in_group == [0, 1, 2, 3, 0, 0, 0, 1, 2, 0, 0, 1]
    assert hld.ET == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert hld.ET1 == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert hld.ET2 == [11, 5, 4, 3, 4, 5, 9, 9, 8, 9, 11, 11]

    assert hld.path(0, 4) == [(0, 2), (4, 4)]
    assert hld.path_e(0, 4) == [(1, 2), (4, 4)]
    assert hld.path_ranges(0, 4) == [(0, 3), (4, 5)]
    assert hld.path_ranges_e(0, 4) == [(1, 3), (4, 5)]
    assert hld.subtree_range(4) == (4, 5)
    assert hld.subtree_range_e(4) == (5, 5)
