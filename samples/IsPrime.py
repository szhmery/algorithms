import math


def IsPrime(Num):
    if Num == 1:
        return False
    for n in range(2, int(math.sqrt(Num)) + 1):
        if Num % n == 0:
            return False
    return True


oList = []

for i in range(1, 101):
    if IsPrime(i) is True:
        oList.append(i)
else:
    print(oList)
