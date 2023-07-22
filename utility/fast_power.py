def fast_power(base, power, mod=1000000007):
    """
    Returns the result of a^b i.e. a**b
    We assume that a >= 1 and b >= 0

    Remember two things!
     - Divide power by 2 and multiply base to itself (if the power is even)
     - Decrement power by 1 to make it even and then follow the first step
    """

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


if __name__ == "__main__":
    assert fast_power(2, 1) == 2
    assert fast_power(2, 2) == 4
    assert fast_power(2, 4) == 16
    assert fast_power(2, 100) == 976371285
