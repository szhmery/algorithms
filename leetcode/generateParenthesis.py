#https://leetcode.com/problems/generate-parentheses/
#22. Generate Parentheses
class Solution:
    def generateParenthesis(self, n):
        result = []
        self.generateParenthesisResult(result, "", n, n)
        return result

    def generateParenthesisResult(self, result, current, left, right):
        if left == 0 and right == 0:
            result.append(current)
        if left > 0:
            self.generateParenthesisResult(result, current + "(", left - 1, right)
        if left < right:
            self.generateParenthesisResult(result, current + ")", left, right-1)

if __name__== "__main__":
    result = Solution().generateParenthesis(3)
    print(result)