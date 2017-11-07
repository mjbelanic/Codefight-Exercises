from itertools import product, imap, ifilter

def crackingPassword(digits, k, d):
    
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted(ifilter(lambda n: int(n) % d == 0, imap(createNumber, product(digits, repeat=k))))