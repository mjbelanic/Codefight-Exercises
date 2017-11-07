class Prizes(object):
    def __init__(self, purchases, n, d):
        self.purchases = purchases
        self.n = n
        self.d = d

    def __iter__(self):
        for idx, elem in enumerate(self.purchases):
            # print idx
            # print elem
            if (idx + 1) % self.n == 0:
                print elem
                if elem % self.d == 0:
                    yield idx + 1


def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))