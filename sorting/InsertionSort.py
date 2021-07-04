def insertSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


if __name__ == '__main__':
    array = [3, 5, 6, 1, 3, 7, 8, 34, 2, 9, 4]
    insertSort(array)
    print(array)