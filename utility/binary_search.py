def bin_search(ng, ok, is_ok):
    while abs(ok - ng) > 1:
        md = (ok + ng) // 2
        if is_ok(md):
            ok = md
        else:
            ng = md
    return ok
