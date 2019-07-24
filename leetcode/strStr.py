#https://leetcode.com/problems/implement-strstr/
#28. Implement strStr()
# Time:  O(n * k)
# Space: O(k)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1


if __name__=="__main__":
    print(Solution().strStr("bbad", "ad"))
    print(Solution().strStr("abababcdab", "ababcdx"))