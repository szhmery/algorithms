import random

def CountingSort(list, maxValue):
    bucket = [None]*(maxValue+1)
    sortedIndex = 0
    Length = list.__len__()
    bucketLen = maxValue + 1

    for i in range(0,Length,1):
        if bucket[list[i]] == None:
            bucket[list[i]] = 0
        bucket[list[i]] += 1

    for j in range(0, bucketLen,1):
        while bucket[j] and bucket[j] > 0: #如果数据不是从0开始,那么bucket有些index是空,需要加判断
            list[sortedIndex] = j
            sortedIndex += 1
            bucket[j] -= 1

    return list

if __name__ == "__main__":
    data = list(i+10 for i in range(20))
    originalList = random.sample(data,k=20)
    print(originalList)
    # 如果数据是从10到29,maxValue不能取20,必须取29.不然bucket[29]越界。故取最大的值。但如果所有值都远大于0.该算法效率也不高。
    resultList = CountingSort(originalList,max(originalList))
    print(resultList)
