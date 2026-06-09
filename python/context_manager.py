from contextlib import contextmanager

@contextmanager
def opened(path, mode='r'):
    f = open(path, mode)
    try: yield f
    finally: f.close()
