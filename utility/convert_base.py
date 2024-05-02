def base_10(num_n, n):
    """10進数 → n進数"""
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10


def base_n(num_10, n):
    """n進数 → 10進数"""
    str_n = ""
    while num_10:
        if num_10 % n >= 10:
            return -1
        str_n += str(num_10 % n)
        num_10 //= n
    return int(str_n[::-1])
