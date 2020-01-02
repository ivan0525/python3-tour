def aplusb(a, b):
    # write your code here
    if a == 0:
        return b
    if b == 0:
        return a
    newA = a ^ b
    newB = (a & b) << 1
    return aplusb(newA, newB)


print(aplusb(1, 2))
