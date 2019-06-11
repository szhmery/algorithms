#https://leetcode.com/problems/3sum/
#15. 3Sum
class Solution():
    def threeSum(self, nums):
        if not nums or len(nums) < 3:
            return []
        result_lists = []
        temp = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp=[nums[i], nums[j], nums[k]]
                        print(temp)
                        if Solution.isContain(self,result_lists,temp) == False:
                            result_lists.append(temp)
                        temp = []
                    else:
                        continue

        return result_lists

    def isContain(self, existing_lists, new_list):
        if not existing_lists:
            return False
        for i in range(len(existing_lists)):
            print("Print sorted new_list and existing_lists:")
            print(sorted(new_list))
            print(sorted(existing_lists[i]))
            if sorted(new_list) == sorted(existing_lists[i]):
                print("It is existed")
                return True
            else:
                continue
        return False

    def threeSum2(self, nums):

        if not nums or len(nums) < 3:
            return []
        nums = sorted(nums)
        result_lists = []
        if nums[-1] < 0 or nums[0] > 0:
            return []
        for k in range(len(nums)):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k-1]:
                continue
            target = 0 - nums[k]
            i, j = k+1,len(nums)-1
            while i < j:
                if nums[i] + nums[j] == target:
                    temp = [nums[k], nums[i], nums[j]]
                    result_lists.append(temp)
                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    while i < j and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1
        return result_lists

    def threeSum3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
            i += 1
        return result
if __name__=="__main__":
    lists = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum2(lists))
    # lists = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    # print(Solution().threeSum(lists))
    # lists = [-2,10,-14,11,5,-4,2,0,-10,-10,5,7,-11,10,-2,-5,2,12,-5,14,-11,-15,-5,12,0,13,8,7,10,6,-9,-15,1,14,11,-9,-13,-10,6,-8,-5,-11,6,-9,14,11,-7,-6,8,3,-7,5,-5,3,2,10,-6,-12,3,11,1,1,12,10,-8,0,8,-5,6,-8,-6,8,-12,-14,7,9,12,-15,-12,-2,-4,-4,-12,6,7,-3,-6,-14,-8,4,4,9,-10,-7,-4,-3,1,11,-1,-8,-12,9,7,-9,10,-1,-14,-1,-8,11,12,-5,-7]
    # print(Solution().threeSum(lists))
