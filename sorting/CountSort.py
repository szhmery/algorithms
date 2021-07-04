def countSort(arr):
    output = [0 for i in range(256)]

    count = [0 for i in range(256)]

    ans = ["" for _ in arr]

    for i in arr:
        count[ord(i)] += 1

    for i in range(256):
        count[i] += count[i - 1]

    for i in range(len(arr)):
        output[count[ord(arr[i])] - 1] = arr[i]
        count[ord(arr[i])] -= 1

    for i in range(len(arr)):
        ans[i] = output[i]
    return ans



# coding=utf-8
# 计数排序
def CountingSort(a, b, k):
    # c=[0]*(k+1) #let c[0...k] be an all 0 array
    # c=[0 for i in range(0,k+1)]
    c = []
    for i in range(k + 1):
        c.append(0)
    for j in range(len(a)):
        c[a[j]] = c[a[j]] + 1
    for i in range(1, k + 1):
        c[i] = c[i] + c[i - 1]
    for j in range(len(a) - 1, -1, -1):
        b[c[a[j]] - 1] = a[j]  # !!!!!减一是关键
        c[a[j]] = c[a[j]] - 1
    print(b)


if __name__ == '__main__':
    arr = "wwwrunoobcom"
    ans = countSort(arr)
    print("字符数组排序 %s" % ("".join(ans)))

    a = [2, 5, 3, 0, 2, 3, 0, 3]
    # b=[0]*len(a)
    b = [None for i in range(len(a))]
    print("脚本之家测试结果：")

    CountingSort(a, b, max(a))
