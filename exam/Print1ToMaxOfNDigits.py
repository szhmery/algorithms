def print1ToMaxOfDigits(n:int) -> None:
    nums = ['0'] * n
    def helper(nums, length, index):
        if index == length:
            Print(nums)
            return
        for i in range(10):
            nums[index] = str(i)
            helper(nums, length, index + 1)
    def Print(nums):
        is_zero = True
        for i in range(n):
            if is_zero and nums[i] != '0':
                is_zero = False
            if not is_zero:
                print(nums[i], end='')
        print()

    helper(nums, n, 0)

print1ToMaxOfDigits(3)
