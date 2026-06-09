import time, functools

def timer(fn):
    @functools.wraps(fn)
    def w(*a, **k):
        s = time.perf_counter(); r = fn(*a, **k)
        print(f'{fn.__name__}: {time.perf_counter()-s:.4f}s'); return r
    return w
