def factorize(n: int):
    from subprocess import run

    out = run("factor " + str(n), shell=True, capture_output=True).stdout
    # n: p1 p1 p1 p2 p2 p3 ...
    res = dict()
    for p in out.split()[1:]:
        if p not in res:
            res[p] = 0
        res[p] += 1
    return res
