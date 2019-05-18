class Solution:
    def isValidBracket(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {"{":"}", "[":"]", "(":")"}

        # 如果长度为奇数,直接返回False。不会成对。
        if len(s) % 2 != 0:
            return False
        # 为空算True
        if len(s) == 0:
            return True
        # 先把第一个字符放入队列queue字符中。
        queue = s[0]
        # 如果第一个放进去的是右括号,那么直接返回错误
        if bracket_map.__contains__(queue) != True:
            return False
        # 如果可以成对,把queue中最后一个pop出来。如果不能成对,而且是左括号,存入queue。最后检查queue长度,为空才返回True。否则是False
        for i in range(1,len(s)):
            if len(queue) == 0 and bracket_map.__contains__(s[i]) == True: # 如果这时候queue为空,而且是左括号,要存入队列
                queue = queue + s[i]
                continue
            if bracket_map[queue[-1]] == s[i]:  # 如果当前的字符是队列最后一个括号的对应括号,从queue中pop出成对的括号
                queue = queue[0:len(queue)-1]
                continue
            elif bracket_map.__contains__(s[i]) == True: # 如何此时queue不为空,而且还是左括号,要存入队列
                queue = queue + s[i]
                continue
            else:
                return False

        # 最后检查queue长度,为空才返回True。否则是False
        if len(queue) == 0:
            return True
        else:
            return False

    def isValidBracket2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        top_element = ''
        bracket_map = {"}": "{", "]": "[", ")": "("}
        for char in s:
            if char in bracket_map:  #如果是右括号
                if stack:  # stack不为空,则pop出最上面一个
                    top_element = stack.pop()
                else:  #否则什么也不做
                    '#'
                if bracket_map[char] != top_element: # 如果pop出来的和目前char不能成对,返回False
                    return False
            else:  # 如果是左括号,放入stack
                stack.append(char)
        return not stack

s = Solution()
print("The 1st method:")
print(s.isValidBracket("()"))
print(s.isValidBracket("()[]{}"))
print(s.isValidBracket("(]"))
print(s.isValidBracket("{[)]"))
print(s.isValidBracket("{[]}"))
print(s.isValidBracket("}{"))
print(s.isValidBracket("{{"))
print(s.isValidBracket(""))
print("The 2nd method:")
print(s.isValidBracket2("()"))
print(s.isValidBracket2("()[]{}"))
print(s.isValidBracket2("(]"))
print(s.isValidBracket2("{[)]"))
print(s.isValidBracket2("{[]}"))
print(s.isValidBracket2("}{"))
print(s.isValidBracket2("{{"))
print(s.isValidBracket2(""))