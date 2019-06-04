#https://leetcode.com/problems/integer-to-roman/
import math

class Solution():

    # def intToRoman(self,num: int) -> str:
    #
    #     romanDict = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD",
    #                  500: "D",900: "CM", 1000: "M"}
    #
    #     keysets = sorted(romanDict.keys())
    #
    #     list_int = list(str(num))[::-1]
    #     list_num = []
    #     list_roman = []
    #     for i in range(len(list_int)):
    #         nextDigit = int(math.pow(10,i))
    #         num_Digit = num // nextDigit * nextDigit
    #
    #         list_num.append(num_Digit)
    #
    #         if num_Digit in romanDict.keys():
    #             list_roman.append(romanDict[num_Digit])
    #         else:
    #             for i in range():
    #             tmp = ""
    #             count = nextDigit - int(list_int[i])
    #             for j in range(count):
    #                 tmp += romanDict[nextDigit // 10]
    #             tmp += romanDict[nextDigit]
    #             list_roman.append(tmp)
    #         else:
    #             tmp = ""
    #             for j in range(int(list_int[i])):
    #                 tmp += romanDict[nextDigit//10]
    #             list_roman.append(tmp)
    #     return ''.join(list_roman[::-1])

    def intToRoman(self, num):
        numeral_map = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD",
                       500: "D", 900: "CM", 1000: "M"}
        keyset, result = sorted(numeral_map.keys()), ""

        while num > 0:
            for key in reversed(keyset):
                while num // key > 0: #python2.7可以使用num/key,但python3结果会成为一个浮点小数,条件无法满足。
                    num -= key
                    result += numeral_map[key]

        return result


s = Solution()
print(s.intToRoman(3))
print(s.intToRoman(8))
print(s.intToRoman(9))
print(s.intToRoman(58))
print(s.intToRoman(1994))
print(Solution().intToRoman(999))
print(Solution().intToRoman(3999))