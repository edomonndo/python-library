def fast_power(base, power, mod=10**9 + 7):
    result = 1
    while power > 0:
        # If power is odd
        if power % 2 == 1:
            result = (result * base) % mod

        # Divide the power by 2
        power = power // 2
        # Multiply base to itself
        base = (base * base) % mod

    return result
