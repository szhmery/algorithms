def selectionSort(arr):
    if arr is None or len(arr) == 0:
        return
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]


if __name__ == '__main__':
    array = [3, 5, 6, 1, 3, 7, 8, 34, 2, 9, 4]
    selectionSort(array)
    print(array)