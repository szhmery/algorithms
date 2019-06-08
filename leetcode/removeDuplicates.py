#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#26. Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        count = 0
        preNum = None
        for num in nums:
            if num is preNum:
                continue
            preNum = num
            count += 1
        return count


    def removeDuplicates(self, A):
        if not A:
            return 0

        last, i = 0, 1
        while i < len(A):
            if A[last] != A[i]:
                last += 1
                A[last] = A[i]
            i += 1

        return last + 1

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

print(Solution().removeDuplicates([1,1,2]))






