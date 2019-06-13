# 斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）
# 以兔子繁殖为例子而引入，故又称为“兔子数列”，指的是这样一个数列：1、1、2、3、5、8、13、21、34、……在数学上，
# 斐波纳契数列以如下被以递推的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）

#给出一个数,如果是fibonacci数列就把之前数列都打印出来。如果不是则throw一个错误
class ThorwErr(Exception):
    print("The number is not in fibonacci sequence!")



class Solution():
    def fibonacci_sum(self, num):

        if num <= 0:
            return []
        result = []
        number = 0
        i = 0
        try:
            while number < num:
                number = self.fibonacci(i)
                result.append(number)
                i += 1
                print(number)
            if number == num:
                return result
            else:
                raise ThorwErr()
        except ThorwErr:
            return []

    def fibonacci(self, n):
        if n <= 1:
            return n
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)



if __name__=="__main__":
    res = Solution().fibonacci_sum(3)
    print(res)
    res = Solution().fibonacci_sum(9)
    print(res)