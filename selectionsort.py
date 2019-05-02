import random

def SelectionSort(list):
    Length = list.__len__()
    for i in range(0, Length, 1):
        minIndex = i
        for j in range(i+1, Length, 1):
            if list[j] < list[minIndex]:
                minIndex = j
        temp = list[i]
        list[i] = list[minIndex]
        list[minIndex] = temp
    return list

if __name__ == "__main__":

    data = list(range(20))
    originalList = random.sample(data,k=20)
    print(originalList)
    resultList = SelectionSort(originalList)
    print(resultList)
