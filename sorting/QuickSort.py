def partition(arr, low, high):
    if low == high:
        return low
    pivot = arr[high]
    i = low
    j = high - 1
    while i < j:
        while i < j and arr[i] <= pivot:
            i += 1
        while i < j and arr[j] > pivot:
            j -= 1
        if i != j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[high] = arr[high], arr[i]
        return i
    return high


# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def quickSort2(lists, i, j):
    if i >= j:
        return lists
    pivot = lists[i]
    low = i
    high = j
    while i < j:
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i] = lists[j]
        while i < j and lists[i] <= pivot:
            i += 1
        lists[j] = lists[i]
    lists[i] = pivot
    quickSort2(lists, low, i - 1)
    quickSort2(lists, i + 1, high)
    return lists


def partition3(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]

    for j in range(low, high):
        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

def quickSort3(arr, low, high):
    if low < high:
        pi = partition3(arr, low, high)

        quickSort3(arr, low, pi - 1)
        quickSort3(arr, pi + 1, high)


if __name__ == '__main__':
    array = [3, 5, 6, 1, 3, 7]
    quickSort(array, 0, len(array) - 1)
    print(array)

    array = [3, 5, 6, 1, 3, 7]
    quickSort2(array, 0, len(array) - 1)
    print(array)

    array = [3, 5, 6, 1, 3, 7]
    quickSort3(array, 0, len(array) - 1)
    print(array)

