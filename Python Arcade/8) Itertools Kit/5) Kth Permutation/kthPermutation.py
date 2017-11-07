from itertools import permutations, islice

def kthPermutation(numbers, k):
    return list(islice(permutations(numbers), k))[k-1]