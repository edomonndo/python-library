def ext_gcd(a: int, b: int) -> int:
    x = v = 1
    y = w = 0
    while b:
        q = a // b
        a, b, x, w, y, v = b, a % b, w, x - q * w, v, y - q * v
    return x, y
