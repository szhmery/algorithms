import random

def BubbleSort(list):
    Length = list.__len__()
    for i in range(0, Length, 1):
        for j in range(0, Length-1-i, 1):
            if list[j] > list[j+1]:
                temp = list[j+1]
                list[j+1] = list[j]
                list[j] = temp
    return list

if __name__ == "__main__":

    data = list(range(20))
    originalList = random.sample(data,k=20)
    print(originalList)
    resultList = BubbleSort(originalList)
    print(resultList)
