def getPoints(answers, p):
    questionPoints = lambda i, ans: (i + 1) if ans == True else -p
    res = 0
    for i, ans in enumerate(answers):
        res += questionPoints(i, ans)
    return res