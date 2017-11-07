class FRange(object):
    def __init__(self, start, stop=None, step=None):
        if stop is None:
            self.i = 0
            self.stop = start
            self.step = 1
        elif step is None:
            self.i = start
            self.stop = stop
            self.step = 1
        else:
            self.i = start
            self.stop = stop
            self.step = step

    def __iter__(self):
        return self

    def next(self):
        if (self.i < self.stop if self.step > 0 else self.i > self.stop):
            r = self.i
            self.i += self.step
            return r
        else:
            raise StopIteration

def rangeFloat(args):
    return list(FRange(*args))