#https://leetcode.com/problems/string-to-integer-atoi/
#8. String to Integer (atoi)
import math
class Solution():
    def AtoI(self, str: str) -> int:
        numStr = ''
        if len(str) == 0:
            return 0
        # for i in range(1,len(str)):
        minus_flag = False
        #把前面是空白的和+-号提出来,如果是字母则直接返回0
        while len(str):
            try:
                if str[0] == " ":
                    str = str[1:]
                elif str[0] == "+":
                    str = str[1:]
                    break
                elif str[0] == "-":
                    minus_flag = True
                    str = str[1:]
                    break
                elif int(str[0]) >= 0:
                    break
            except ValueError:
                return 0
        i = 0
        for i in range(len(str)):
            try:
                if int(str[i]) > 0:
                    continue
            except ValueError:
                print("Not a numnber.")
                i -= 1
                break

        stop = i + 1
        numStr = str[0:stop]
        if len(numStr) == 0:
            return 0
        #最大和最小值在2的32次-1方和负2的32次方之间
        max_int = int(math.pow(2,31))
        if minus_flag == True:
            if int(numStr) > max_int:
                return 0 - max_int
            else:
                return 0 - int(numStr)

        if minus_flag == False:
            if int(numStr) > max_int-1:
                return max_int-1
            else:
                return int(numStr)





s = Solution()
print(s.AtoI("345aa"))
print(s.AtoI("42"))
print(s.AtoI("-91283472332"))
print(s.AtoI(""))
print(s.AtoI("0000000000012345678"))






