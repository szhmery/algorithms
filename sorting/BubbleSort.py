def bubbleSort(arr):
    if arr is None or len(arr) == 0:
        return
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    array = [3, 5, 6, 1, 3, 7, 8, 34, 2, 9, 4]
    result = bubbleSort(array)
    print(result)
