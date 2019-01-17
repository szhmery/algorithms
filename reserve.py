import sys

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            a = list(str(abs(x)))[::-1]
            b = "".join(a)
            if (0-int(b) < -2147483648):
                return 0
            else:
                return (0-int(b))
        else:
            # a = list(str(x))[::-1]
            a = list(str(x))
            a.reverse() # reverse() 和[::-1]作用相同
            print(a)
            b = "".join(a)
            if (int(b) > 2147483648):
                return 0
            else:
                return int(b)
    def reverse2(self,x):
        rev = 0
        flag = 0
        if x < 0:
            x=abs(x)
            flag = 1
        while x != 0:
            pop = x % 10  # 取出最后位的一个数
            x = int(x/10) # 取出最后位一个数后剩下的数
            if rev > 2147483648 /10 or (rev == 2147483648/10 and pop >7 ):
                return 0
            # if rev < 2147483648 / 10 or (rev == 2147483648 / 10 and pop < -8):
            #     return 0
            rev = rev * 10 + pop # 把数反转过来,高位变低位,低位变高位
        if flag == 1:
            return 0-rev
        return rev
s = Solution()

print("The first method:")
print(s.reverse(123))
print(s.reverse(120))
print(s.reverse(-321))
print(s.reverse(1534236469))

print("The second method:")
print(s.reverse2(123))
print(s.reverse2(120))
print(s.reverse2(-321))
print(s.reverse2(1534236469))