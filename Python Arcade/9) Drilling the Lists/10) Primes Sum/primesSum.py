def primesSum(a, b):
    return findPrimes(a,b)

def findPrimes(a,b):
    primeTotal = 0
    if a == 1:
        a = a + 1
    for i in range(a, b+1):
        val = 2
        isChecking = True
        while(isChecking):
            if val*val > i:
                primeTotal += i
                isChecking = False
            elif i % val == 0:
                isChecking = False
            else:
                val = val + 1
    return primeTotal