from typing import List


def FindNumbersWithSum(nums: List, s: int) -> List:
    if not nums or len(nums) == 0:
        return
    l = 0
    h = len(nums) - 1
    ans = []
    while l < h:
        if nums[l] + nums[h] == s:
            ans.extend([nums[l], nums[h]])
            break
        elif nums[l] + nums[h] < s:
            l += 1
        else:
            h -= 1
    return ans

def FindContinuousSequence(s: int) -> List:
    if s < 3:
        return
    ans = []
    l = 1
    m = (s + 1) // 2
    h = 2
    cur = l + h
    while l < m:
        if cur == s:
            tmp = [i for i in range(l, h + 1)]
            ans.append(tmp)
            h += 1
            cur += h
        elif cur < s:
            h += 1
            cur += h
        else:
            cur -= l # remove l firstly then move l.
            l += 1

        # while cur > s and l < m:
        #     cur -= l
        #     l += 1
        #     if cur == s:
        #         tmp = [i for i in range(l, h + 1)]
        #         ans.append(tmp)
        #
        # cur += h
        # h += 1
    return ans

print(FindNumbersWithSum([1, 2, 4, 7, 11, 15], 15))
print(FindContinuousSequence( 15))
