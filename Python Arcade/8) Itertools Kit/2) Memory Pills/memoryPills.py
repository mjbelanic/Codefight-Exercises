from itertools import cycle, chain, dropwhile

def memoryPills(pills):
    gen = chain(dropwhile(lambda x: len(x)%2 > 0,pills),cycle([""]))
    next(gen)
    return [next(gen) for _ in range(3)]