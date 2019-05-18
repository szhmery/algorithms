import random

def QuickSort(list, left, right):
    if left < right:
        partitionIndex = partition(list, left, right)
        QuickSort(list, left, partitionIndex-1)
        QuickSort(list, partitionIndex+1, right)


def partition(list, left, right):
    pivot = left
    index = left + 1
    for i in range(index, right+1, 1):
        if list[i] < list[pivot]:
            swap(list, i, index)
            index += 1 #use index to count how many data swap
    swap(list, pivot, index-1) # because index is begin 1, so list from pivot to index-1 is all of data less than pivot
    return index-1

def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

if __name__  == "__main__":
    data = list(range(20))
    originalList = random.sample(data,k=20)
    print(originalList)
    QuickSort(originalList, 0, originalList.__len__()-1)
    print(originalList)

