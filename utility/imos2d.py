def imos2d(H: int, W: int, arr: list[tuple(int, int, int, int)]) -> list[list[int]]:
    res = [[0] * (W + 1) for _ in range(H + 1)]
    for x1, y1, x2, y2 in arr:
        res[x1][y1] += 1
        if x2 + 1 <= H:
            res[x2 + 1][y1] -= 1
        if y2 + 1 <= W:
            res[x1][y2 + 1] -= 1
        if x2 + 1 <= H and y2 + 1 <= W:
            res[x2 + 1][y2 + 1] += 1

    for i in range(H):
        for j in range(W):
            res[i + 1][j + 1] += res[i][j + 1] + res[i + 1][j] - res[i][j]

    return res
