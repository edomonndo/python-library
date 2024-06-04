from types import GeneratorType


def antirec(func, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return func(*args, **kwargs)
        to = func(*args, **kwargs)
        while True:
            if isinstance(to, GeneratorType):
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to

    return wrappedfunc
