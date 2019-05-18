import random
import math

def ShellSort(list):
    Length = list.__len__()
    gap = math.floor(Length / 2)
    while gap > 0:
        for i in range(gap,Length,1):
            j = i
            current = list[i]
            while j - gap >= 0 and current < list[j-gap]: # while make sure all of previous j-gap data is less than current
                list[j] = list[j-gap]
                j = j - gap
            list[j] = current
        gap = math.floor(gap / 2)

    return list

if __name__ == "__main__":
    data = list(range(20))
    originalList = random.sample(data,k=20)
    print(originalList)
    resultList = ShellSort(originalList)
    print(resultList)
