class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = { "I" :1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        list_roman = list(s)
        list_int = []
        for i in list_roman:
            list_int.append(dict[i]) #把罗马数字转为阿拉伯数字int
        length = len(list_int)
        total = 0
        i = 0
        # 做一个循环,用前面一个数字比较后面一个数字,如果前面的小,那么说明需要用后面一个减前面那个数,
        # 再加入总数。如果前面比后面大,则继续加入总数。直到所有数字轮询完。
        while i < length:
            if i + 1 < length:
                if list_int[i] < list_int[i + 1]:
                    total = total + list_int[i+1]-list_int[i]
                    i += 2  #这个时候i和i+1这两个数都已经被加入总和了。直接跳2个数字
                    continue
                elif list_int[i] >= list_int[i + 1]:
                    total = total + list_int[i]
            elif i == length -1 :
                total = total + list_int[i] #如果经历完前面的,还有最后一个数,那最后一个数不需要比,直接加入总和。
            else:
                break
            i += 1
        return total

s = Solution()
print(s.romanToInt("IX"))
print(s.romanToInt("MCMXCIV"))
print(s.romanToInt("III"))
print(s.romanToInt("IV"))
print(s.romanToInt("LVIII"))
