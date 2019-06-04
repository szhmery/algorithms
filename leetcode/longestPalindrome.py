#https://leetcode.com/problems/longest-palindromic-substring/
#5. Longest Palindromic Substring

class Solution():
    def longestPalindrome(self,s):
        longestLen = 0
        longestSub = []
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):

                if Solution._isPalindrome(self,s[i:j]) == True:
                    print(s[i:j])
                    if len(s[i:j]) > longestLen:
                        longestSub = s[i:j]
                        longestLen = len(s[i:j])
        print("LongestPalindrome: ", longestSub)
        return longestSub

    def _isPalindrome(self,s):
        if s == None:
            return False

        if  s == s[::-1]:
            return True
        else:
            return False

s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))