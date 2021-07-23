import random
import heapq
# use heapq, heap sort
def leastKNumbers(array, k):
    ans = []
    heapq.heapify(array)
    for i in range(k):
        ans.append(heapq.heappop(array))
    return ans

# time complexity O(n) quick sort
def leastKNumbers2(array, k):
    if not array or k <= 0:
        return
    ans = []
    index = partition(array, 0, len(array) - 1)
    start = 0
    end = len(array) - 1

    while index != k:
        if index > k:
            end = index - 1
            index = partition(array, start, end)
        else:
            start = index + 1
            index = partition(array, start, end)
    for i in range(index):
        ans.append(array[i])
    return ans

def partition(nums, low, high):
    if low == high:
        return
    p = random.randint(low, high)
    pivot = nums[p]
    nums[high], nums[p] = nums[p], nums[high]
    i = 0
    j = high - 1
    while i < j:
        while i < j and nums[i] <= pivot:
            i += 1
        while i < j and nums[j] > pivot:
            j -= 1
        if i != j:
            nums[i], nums[j] = nums[j], nums[i]
    if nums[i] > pivot:
        nums[high], nums[i] = nums[i], nums[high]
        return i
    return high

def selectKnumbers(array, k):
    if not array or k <= 0:
        return
    ans = []
    array = sorted(array)
    for i in range(k):
        ans.append(array[-i - 1])
    return ans


if __name__ == '__main__':
    result = largestKNumbers([3, 4, 6, 2, 4, 7, 8, 4, 1], 3)
    print(result)
    result = leastKNumbers2([3, 4, 6, 2, 4, 7, 8, 4, 1], 3)
    print(result)
    result = selectKnumbers([3, 4, 6, 2, 4, 7, 8, 4, 1], 3)
    print(result)
