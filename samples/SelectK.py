def select(array, k):
    if not array or k <= 0:
        return
    ans = []
    array = sorted(array)
    for i in range(k):
        ans.append(array[-i - 1])
    return ans


if __name__ == '__main__':
    result = select([3, 4, 6, 2, 4, 7, 8, 4, 1], 3)
    print(result)
