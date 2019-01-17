class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if list(str(x))[::-1] == list(str(x)):
            return True
        else:
            return False
    def isPalindrome2(self,x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x = int(x/10)

        return x == reverted_number or x == int(reverted_number / 10)

s = Solution()
print("The first method:")
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
print(s.isPalindrome(11))
print(s.isPalindrome(12321))
print("The second method:")
print(s.isPalindrome2(121))
print(s.isPalindrome2(-121))
print(s.isPalindrome2(10))
print(s.isPalindrome2(11))
print(s.isPalindrome2(12321))