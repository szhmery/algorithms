# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 17. Letter Combinations of a Phone Number
class Solution:
    def letterCombinations(self, digits):
        #corner case
        if not digits:
            return []

        letterMap = {"0": "", "1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        string = ''
        self.dfsHelper( 0, digits, letterMap, string, result)
        return result

    def dfsHelper(self, index, digits, letterMap, string, result):
        # base case
        if index == len(digits):
            result.append(string)
            print(string)
            return
        # recursive rule
        values = letterMap.get(digits[index])
        print(values)
        for i in range(len(values)):
            string = string + values[i]
            self.dfsHelper(index + 1, digits, letterMap, string, result)
            # recover
            string = string[:-1]

if __name__ == "__main__":

    result = Solution().letterCombinations("23")
    print("result:")
    print(result)