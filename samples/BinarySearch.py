# 递归实现：
def binary_seach(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2  # middle 记录中间位置索引
        if item == alist[mid]:  # 如果查找元素与中间位置元素相等 则返回真
            return True
        elif item < alist[mid]:  # 如果查找元素小于中间位置元素，则进行列表切片缩小列表范围
            return binary_seach(alist[:mid], item)
        else:
            return binary_seach(alist[mid + 1:], item)


# 非递归实现：
def binary_seach2(alist, item):
    first = 0  # 起始下标为0
    last = len(alist) - 1  # 列表最后一位的索引
    while first <= last:  # 列表中间位置的索引值
        mid = (first + last) // 2
        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    else:
        return False


if __name__ == '__main__':
    alist = [5, 10, 15, 18, 35, 55, 65, 75, 99]
    print(binary_seach(alist, 200))  # 查找列表中不存在的数据
    print("__________________")
    print(binary_seach(alist, 15))  # 查找列表中存在的数据
    print(binary_seach2(alist, 200))  # 查找列表中不存在的数据
    print("__________________")
    print(binary_seach2(alist, 15))  # 查找列表中存在的数据