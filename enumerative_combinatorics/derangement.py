def derangement(n: int, mod: int) -> list[int]:
    # assert n >= 0
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 0]
    elif mod == 1:
        return [0] * (n + 1)
    res = [0] * (n + 1)
    res[2] = 1
    x, y = 0, 1
    for i in range(3, n + 1):
        x, y = y, (i - 1) * (x + y)
        y %= mod
        res[i] = y
    return res
