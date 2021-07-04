class Solution:

    def __init__(self, nums):
        self.nums = nums
        self.dict_sum = {}

    def sum_all(self):
        self.dict_sum[0] = self.nums[0]
        for i in range(1, len(self.nums)):
            self.dict_sum[i] = self.dict_sum[i - 1] + self.nums[i]


    def sum2(self, i, j):
        if i < 0 or j > len(self.nums) - 1 or j < i:
            return
        if i == 0:
            return self.dict_sum[j] - self.dict_sum[i - 1]


    def Sum1(self, nums, i, j):
        if nums is None:
            return
        if i < 0 or j > len(nums) - 1 or j < i:
            return

        ans = 0
        for k in range(i, j + 1):
            ans += nums[k]
        return ans