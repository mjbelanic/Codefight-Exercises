def climbingStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    a = 1
    b = 2
    c = 0
    for i in range(3,n+1,1):
        c = a + b
        a = b
        b = c
    return c