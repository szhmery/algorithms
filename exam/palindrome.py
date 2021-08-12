# input: str: hannah, True, han:False
#   1aa1
def isPalindrome(str):
    if not str and len(str):
        return True
    lo, hi = 0, len(str) - 1
    while lo < hi:
        if lo < hi and str[lo] != str[hi]:
            return False
        lo += 1
        hi -= 1
    return True

#时间复杂度：两层 for 循环 O(n²），for 循环里边判断是否为回文 O(n），所以时间复杂度为 O(n³）。
#空间复杂度：O(1），常数个变量。
# brute force
def longestPalindrome1(self, s: str) -> str:
    #判断是否是回文串函数
    def pending_nums(s):
        lenth = len(s)
        for i in range(lenth // 2):
            if s[i] != s[lenth - i - 1]:
                return False
        return True
    lenth = len(s)
    max_len = 0
    result = ""
    #遍历每一个子串
    for i in range(lenth):
        # 这里我做了一个小改进，本来应该从前往后，遍历然后记录，我这里直接从后往前遍历，
        # 找到一个回文串即说明是当前i下的最长子串直接，返回判断，然后break即可
        # 这个方法，让测试用例从93个挺进到了119个(优化了26个)
        for j in range(lenth, i, - 1):
            if pending_nums(s[i : j]):
                if j - i > max_len:
                    max_len = j - i
                    result = s[i : j]
                break
    return result

def longestPalindrome2(self, s: str) -> str:
    res = ''
    for i in range(len(s)):
        s1 = self.find(s, i, i)  # 以当前字符为中心的最长回文子串
        s2 = self.find(s, i, i + 1)  # 以当前字符和下一字符为中心的最长回文子串
        # 如果最大长度有变化则更新res
        if max(len(s1), len(s2)) > len(res):
            res = s2 if len(s1) < len(s2) else s1
    return res

def find(self, s, left, right):
    # 找到当前中心的最大长度子串
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
        return s[left + 1:right]


#abbacc =>abba
#aabcd =>aa
def getLongestPalindrome3(str):
    def helper(str, left, right): # extend from i or i, i + 1
        l = left
        r = right
        while l >= 0 and r < len(str) and str[l] == str[r]:
            l += 1
            r -= 1
        return r - l + 1

    str = list(str)
    if not str or len(str) == 0:
        return
    n = len(str)
    start, end = 0, 0
    for i in range(n):
        length = helper(str, i, i) # 12321 => 5
        length2 = helper(str, i, i + 1) # 1221 => 4
        max_len = max(length, length2)
        if max_len == len(str):
            return str
        if max_len > end - start:
            start = i - (length - 1) // 2
            end = i + length // 2

    return ''.join(str[start: end + 1])
# 12321
# 1 1 12 0
# 2 1 23 0
# 3 5 => 2 5//2
# 4 1 21
# 5 1

print(isPalindrome('1aa1'))
print(isPalindrome('1aa1a'))
print(isPalindrome('hannah'))
print(isPalindrome('hananah'))