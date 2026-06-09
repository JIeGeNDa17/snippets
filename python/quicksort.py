def quicksort(a):
    if len(a) <= 1: return a
    p = a[len(a)//2]
    return quicksort([x for x in a if x<p]) + [x for x in a if x==p] + quicksort([x for x in a if x>p])
