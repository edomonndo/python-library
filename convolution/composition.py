from convolution.convolution import *
from convolution.formal_power_series import FPS


def _composition_preprocess(b: list[int], k: int, deg: int) -> list[int]:
    X = [[] for _ in range(k + 1)]
    X[0] = [1]
    for i, x in enumerate(X):
        if i == k:
            break
        X[i + 1] = multiply(x, b)[: deg + 1]
    return X


def _composition_main(
    X: list[list[int]],
    a: list[int],
    sz_y: int,
    xd: int,
    d: int,
    k: int,
    deg: int,
) -> None:
    sz = len(a)
    Z = [1]
    F = [0] * (deg + 1)
    for i in range(k):
        Y = [0] * sz_y
        for j, x_ in enumerate(X):
            if i * d + j >= sz:
                break
            for t, x in enumerate(x_):
                Y[t] += x * a[i * d + j] % MOD
        Y = multiply(Y, Z)[: deg + 1]
        for j, y in enumerate(Y):
            F[j] += y
        Z = multiply(Z, xd)[: deg + 1]
    F.pop()
    return [x % MOD for x in F]


def composition(a: list[int], b: list[int]) -> list[int]:
    deg = min(len(a), len(b))
    k = int(deg**0.5 + 1)
    d = (deg + k) // k

    X = _composition_preprocess(b, k, deg)
    sz_y = len(X[-1])
    X[d + 1 :] = []
    xd = X.pop()
    return _composition_main(X, a, sz_y, xd, d, k, deg)


def composition_multi(a_: list[list[int]], b: list[int], deg: int) -> list[list[int]]:
    k = int(deg**0.5 + 1)
    d = (deg + k) // k

    X = _composition_preprocess(b, k, deg)
    X[d + 1 :] = []
    xd = X.pop()
    sz_y = len(X[-1])
    return [_composition_main(X, a, sz_y, xd, d, k, deg) for a in a_]


def composition_inverse(f: list[int], deg: int = -1) -> list[int]:
    if deg == -1:
        deg = len(f)
    dfdx = FPS.fps_diff(f)
    f = [-x for x in f]
    res = [0]
    m = 1
    while m < deg:
        m <<= 1
        cf0, cf1 = composition_multi([f, dfdx], res, m)
        cf0[1] += 1
        tmp = multiply(cf0, FPS.inv(cf1, m))
        res[m >> 1 :] = tmp[m >> 1 : min(deg, m)]
    return res
