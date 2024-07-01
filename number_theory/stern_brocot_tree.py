from fractions import Fraction


def stern_brocot(p: int | Fraction, n: int) -> tuple[int, int, int, int]:
    """
    a/b <= √p <= c/d を満たす a,b,c,d <= n を求める
    """
    la = rb = 0
    lb = ra = 1
    lu = ru = 1
    a = d = 0
    b = c = 1
    while lu or ru:
        ma = la + ra
        mb = lb + rb
        if p * mb**2 < ma**2:
            ra = ma
            rb = mb
            if ma <= n and mb <= n:
                c = ma
                d = mb
            else:
                lu = 0
        else:
            la = ma
            lb = mb
            if ma <= n and mb <= n:
                a = ma
                b = mb
            else:
                ru = 0
    return a, b, c, d
