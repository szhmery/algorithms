import random

def InsertSort(list):
    Length = list.__len__()
    for i in range(1, Length, 1):
        preIndex = i - 1
        current = list[i]
        while preIndex >= 0 and list[preIndex] > current:
            list[preIndex + 1] = list[preIndex] # if current is less than previous data, move previous data to the next position
            preIndex -= 1
        list[preIndex+1] = current
    return list



if __name__  == "__main__":
    data = list(range(20))
    originalList = random.sample(data,k=20)
    print(originalList)
    resultList = InsertSort(originalList)
    print(resultList)


