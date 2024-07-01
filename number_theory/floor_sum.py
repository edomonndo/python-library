def floor_sum(n: int, m: int, a: int, b: int) -> int:
    res = 0
    if a < 0:
        a2 = a % m
        return floor_sum(n, m, a2, b) - n * (n - 1) * ((a2 - a) // m) // 2
    if b < 0:
        b2 = b % m
        return floor_sum(n, m, a, b2) - n * ((b2 - b) // m)
    if a >= m:
        res += (n - 1) * n * (a // m) // 2
        a %= m
    if b >= m:
        res += n * (b // m)
        b %= m
    y_max = (a * n + b) // m
    x_max = y_max * m - b
    if y_max == 0:
        return res
    res += (n - (x_max + a - 1) // a) * y_max
    res += floor_sum(y_max, a, m, (a - x_max % a) % a)
    return res
