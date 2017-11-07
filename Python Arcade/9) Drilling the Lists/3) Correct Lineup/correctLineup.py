def correctLineup(athletes):
    return [x for t in zip(athletes[1::2], athletes[::2]) for x in t]