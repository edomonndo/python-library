MOD = 998244353


def fast_power(base, power):
    result = 1
    while power > 0:
        # If power is odd
        if power % 2 == 1:
            result = (result * base) % MOD

        # Divide the power by 2
        power = power // 2
        # Multiply base to itself
        base = (base * base) % MOD

    return result
