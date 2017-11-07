def prefSum(a):
    return reduce(lambda c,x,: c + [c[-1] + x], a, [0])[1:]