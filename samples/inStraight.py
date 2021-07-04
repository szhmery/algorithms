from typing import List

#顺子，大小王是万能牌
class Solution:
    # 0 is 大王 or 小王
    # set
    def is_straight(self, nums: List) -> bool:
        exist = set()
        max_num = -1
        min_num = 14
        for num in nums:
            if num == 0:
                continue
            if num in exist:
                return False
            exist.add(num)
            max_num = max(max_num, num)
            min_num = min(min_num, num)
        return max_num - min_num < 5

    # sort
    def is_straight2(self, nums: List) -> bool:
        nums.sort()
        joker = 0
        for i in range(4):
            if nums[i] == 0:
                joker += 1
            elif nums[i] == nums[i + 1]:
                return False
        return nums[4] - nums[joker] < 5


solution = Solution()
nums = [0, 0, 1, 2, 5]
nums = [0, 0, 1, 2, 6]
print(solution.is_straight(nums))
print(solution.is_straight2(nums))
