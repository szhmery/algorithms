import random
import math

global Len
def buildMaxHeap(list, size):
    Length = list.__len__()
    for i in range(math.floor(Length/2), -1, -1):
        heapify(list, i, size) # 迭代方式实现堆调整


def heapify(list,i, size):   #堆调整
    left = 2 * i + 1 #i就是parent
    right = 2 * i + 2
    largest = i

    if left < size and list[left] > list[largest]:
        largest = left
    if right < size and list[right] > list[largest]:
        largest = right
    if largest != i:
        swap(list, i, largest) #如果i不是最大的就把最大的放到parent位置
        heapify(list, largest, size)


def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def HeapSort(list):
    size = originalList.__len__()
    buildMaxHeap(list, size)
    for i in range(size-1,0,-1):
        swap(list, 0, i) #把最大堆最第一个,即堆顶parent, list[0]给挪到后面去。
        heapify(list, 0, i)
    return list

if __name__  == "__main__":
    data = list(range(20))
    originalList = random.sample(data,k=20)
    print(originalList)

    resultList = HeapSort(originalList)
    print(resultList)
