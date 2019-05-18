class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        滑动窗口方法,把字符存入,然后检查后面的字符是不是在其中,如果在其中就把substring滑动到在发现重复的后面。
        并计算substring长度,存入最长长度值。直到循环结束。
        """
        longest = 0
        string_list = list(s)
        print(string_list)
        # substring先初始化为空
        char_list = []
        for i in range(len(s)):
            # 当前字符
            current_char = string_list[i]
            # 如果当前字符在 substring中
            if current_char in char_list:
                # 则把substring往后移到发现重复字符之后,重复之前包含重复字符的全部丢弃
                char_list = char_list[char_list.index(current_char) + 1:len(char_list)]
            # 并把这次发现的重复的那个字符存入substring(以后可能不会再有重复的)
            char_list.append(current_char)
            print(char_list)
            # 把最长的susstring长度存入longest
            if len(char_list) > longest:
                longest = len(char_list)
        return longest



str1 = "abcabcbb"
str2 = "bbbbbb"
str3 = "pwwkew"

s = Solution()
print(s.lengthOfLongestSubstring(str1))

print(s.lengthOfLongestSubstring(str2))

print(s.lengthOfLongestSubstring(str3))