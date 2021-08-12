# [4, -6, 6, 10] 14
# i=0: 4
# i=1: 4
# i=2: 4+6
# i=3: 10 + 4
def MaxSum(array):
    if not array or len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    dp = [-float('inf')] * len(array)
    dp[0] = array[0]
    dp[1] = max(array[0], array[1])
    max_count = array[0]
    for i in range(2, len(array)):
        dp[i] = max(dp[i - 1], dp[i - 2] + array[i], array[i])
        max_count = max(max_count, dp[i])
    return max(max_count, dp[-1])


print(MaxSum([4, -6, 6, 10]))
print(MaxSum([4]))
print(MaxSum([4, -6]))
print(MaxSum([4, -6, 6]))
print(MaxSum([]))
print(MaxSum([1, 1, 1, 1]))
print(MaxSum([-1, -1, -1, -1]))
print(MaxSum([-1, 1000, 1001, 1]))
print(MaxSum([-1, -2, -4, -5, 4]))
print(MaxSum([-1, -2, -4, -5, -6, 5]))
