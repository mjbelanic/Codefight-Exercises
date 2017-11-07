from collections import Counter

def frequencyAnalysis(encryptedText):
    return [i for i, encryptedText in Counter(encryptedText).most_common(1)][0]