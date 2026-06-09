def flatten(xs):
    for x in xs:
        if isinstance(x, list): yield from flatten(x)
        else: yield x
