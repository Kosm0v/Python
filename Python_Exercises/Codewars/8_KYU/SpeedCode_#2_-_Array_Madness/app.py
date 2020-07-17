def array_madness(a,b):
    a = map(lambda a:a**2,a)
    b = map(lambda b:b**3,b)
    return sum(list(a))>sum(list(b))