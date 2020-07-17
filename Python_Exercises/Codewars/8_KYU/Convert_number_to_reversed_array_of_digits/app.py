def digitize(n):
    # return list(map(lambda x: int(x),list(str(n)[::-1])))
    return [int(x) for x in str(n)[::-1]]