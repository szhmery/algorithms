

class Solution():
    def isPowerOfTwo(self, num):
        if num < 0:
            return False
        i = 0
        while pow(2,i) < num:
            i += 1
        if pow(2,i) == num:
            return True
        else:
            return False

    def isPowerOfTwo2(self, n):
        return n > 0 and (n & (n-1)) == 0

    def isPowerOfTwo3(self, n):
        return n > 0 and (n & ~-n) == 0

if __name__=="__main__":
    print(Solution().isPowerOfTwo(8))
    print(Solution().isPowerOfTwo2(4))
    print(Solution().isPowerOfTwo3(4))
