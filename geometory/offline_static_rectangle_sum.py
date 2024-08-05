from bisect import bisect_left
from data_structure.fenwick_tree.fenwick_tree import FenwickTree


def solve(
    points: list[tuple[int, int, int]], queries: list[tuple[int, int]]
) -> list[int]:
    n, q = len(points), len(queries)

    # y座標でソート&座圧
    points.sort(key=lambda p: p[1])
    toY = []
    for i in range(n):
        x, y, w = points[i]
        if len(toY) == 0 or toY[-1] != y:
            toY.append(y)
        points[i] = (x, len(toY) - 1, w)

    # イベントソート
    event = []
    for qi, (x1, y1, x2, y2) in enumerate(queries):
        y1_ = bisect_left(toY, y1)
        y2_ = bisect_left(toY, y2)
        event += [(x1, y1_, y2_, ~qi), (x2, y1_, y2_, qi)]

    # x座標でソート
    points.sort(key=lambda p: p[0])
    event.sort(key=lambda e: e[0])

    # 平面走査
    res = [0] * q
    fw = FenwickTree(len(toY))
    pi, qi = 0, 0
    while qi < q * 2:
        if pi == n or event[qi][0] <= points[pi][0]:
            x, y1, y2, i = event[qi]
            s = fw.sum(y1, y2)
            if i < 0:
                res[~i] -= s
            else:
                res[i] += s
            qi += 1
        else:
            fw.add(points[pi][1], points[pi][2])
            pi += 1
    return res
