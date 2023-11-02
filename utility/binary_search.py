def bin_search(ng, ok):
    def is_ok(md):
        pass

    while abs(ok - ng) > 1:
        md = (ok + ng) // 2
        if is_ok(md):
            ok = md
        else:
            ng = md
    return ok
