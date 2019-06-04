#https://leetcode.com/problems/longest-palindromic-substring/
#5. Longest Palindromic Substring

class Solution():
    def longestPalindrome(self,s):
        """
            :type s: str
            :rtype: str
            """
        longestLen = 0
        longestSub = ""
        if len(s) > 1000:
            return False
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if Solution._isPalindrome(self,s[i:j]) == True and len(s[i:j]) > len(longestSub):
                    print(s[i:j])
                    longestSub = s[i:j]

        print("LongestPalindrome: ", longestSub)
        return longestSub

    def _isPalindrome(self,s):
        if s == None:
            return False
        if s == s[::-1]:
            return True
        else:
            return False

    def longestPalindrome2(self,s):

        """
        :type s: str
        :rtype: str
        """
        # Return if string is empty
        if not s: return s

        res = ""
        for i in range(len(s)):
            j = i + 1
            # While j is less than length of string
            # AND res is *not* longer than substring s[i:]
            while j <= len(s) and len(res) <= len(s[i:]): #效率更高一些。剩下的字符串短于目前获得的字符串的话就不用继续了
                # If substring s[i:j] is a palindrome
                # AND substring is longer than res
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(res):
                    res = s[i:j]
                j += 1

        return res

s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome(""))
print(s.longestPalindrome("a"))