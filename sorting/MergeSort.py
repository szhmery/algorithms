# not the best one. allocate result array in every recursion
def merge(left, right):
    '''合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组'''
    # left与right的下标指针
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


def mergeSort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists) // 2
    left = mergeSort(lists[:middle])
    right = mergeSort(lists[middle:])
    return merge(left, right)


# This one is better. Save space.
def mergeSort3(data):
    """
    先将数组不断进行对半分裂直到不可再分(最长子数组长度为1)，然后进行归并，归并的时候每次从两个
    数组中选择最小的元素。
    归并排序是稳定算法，时间复杂度为nlogn
    :param data: 待排序的数组
    """

    def sort3(start, end):
        if start < end:
            # mid = (start + end) >> 1
            mid = start + (end - start) // 2
            sort3(start, mid)
            sort3(mid + 1, end)
            merge3(start, mid, end)

    def merge3(start, mid, end):
        p1, p2 = start, mid + 1
        while p1 <= mid and p2 <= end:
            if data[p1] < data[p2]:
                temp.append(data[p1])
                p1 += 1
            else:
                temp.append(data[p2])
                p2 += 1
        if p1 <= mid:
            temp.extend(data[p1: mid + 1])  # mid + 1 can get the last one
        if p2 <= end:
            temp.extend(data[p2: end + 1])

        # 【需要将辅助数组中的数还原到data中】
        while temp:
            data[start] = temp.pop(0)
            start += 1

    if not data:
        return
    temp = []  # 建立全局辅助数组，避免递归过程不断创建
    sort3(0, len(data) - 1)


if __name__ == '__main__':
    array = [3, 5, 6, 1]
    result = mergeSort(array)
    print(result)

    array = [3, 5, 6, 1]
    mergeSort3(array)
    print(array)

    array = [3, 5, 6, 1]
    mergeSort4(array)
    print(array)
