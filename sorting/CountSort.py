def countSort(arr):
    count = [0 for _ in range(256)]

    ans = ["" for _ in arr]
    mx, mn = 0, 255
    for i in arr:
        idx = ord(i)
        if idx > mx:
            mx = idx
        if idx < mn:
            mn = idx
        count[idx] += 1
    idx = 0
    for i in range(mn, mx + 1):
        if count[i] == 0:
            continue
        for _ in range(count[i]):
            ans[idx] = chr(i)
            idx += 1
    return ans


# coding=utf-8
# 计数排序
def CountingSortNumber(nums):
    ans = []

    mx = max(nums)
    mn = min(nums)
    count = [0] * (mx + 1)
    for num in nums:
        count[num] += 1
    idx = 0
    for i in range(mn, mx + 1):
        if count[i] == 0:
            continue
        for _ in range(count[i]):
            ans.append(i)
            idx += 1
    return ans


if __name__ == '__main__':
    # arr = "wwwrunoobcom"
    arr = "eeecccddaabacb"
    ans = countSort(arr)
    print("字符数组排序 %s" % ("".join(ans)))

    a = [2, 5, 3, 0, 2, 3, 0, 3]
    print(CountingSortNumber(a))
    a = [1000, 1005, 1013, 1010, 1012, 1009, 1000, 1003]
    print(CountingSortNumber(a))
