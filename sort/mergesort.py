import random
import math

def MergeSort(list):
    Length = list.__len__()
    if Length < 2:
        return list
    middle = math.floor(Length/2)
    left = list[0:middle]
    right = list[middle:Length]
    return merge(MergeSort(left),MergeSort(right))

def merge(left, right):
    result = []
    while left and left.__len__() > 0 and right and right.__len__() > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0)) # pop is shift in C
        else:
            result.append(right.pop(0))
    while left and left.__len__():
        result.append(left.pop(0))
    while right and right.__len__():
        result.append(right.pop(0))
    return result

if __name__ == "__main__":
    data = list(range(20))
    originalList = random.sample(data,k=20)
    print(originalList)
    resultList = MergeSort(originalList)
    print(resultList)