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
            a = list(str(x))[::-1]
            b = "".join(a)
            if (int(b) > 2147483648):
                return 0
            else:
                return int(b)

s = Solution()

a = 123
print(s.reverse(a))
a = 120
print(s.reverse(a))
a = -321
print(s.reverse(a))
a = 1534236469
print(s.reverse(a))