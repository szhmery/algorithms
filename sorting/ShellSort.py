# https://www.cnblogs.com/chengxiao/p/6104371.html
def shellSort(arr):
    n = len(arr)
    gap = int(n / 2)

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = int(gap / 2)


if __name__ == '__main__':
    array = [12, 11, 13, 5, 6, 7]
    shellSort(array)
    print(array)