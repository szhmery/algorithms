from typing import List

def isPopOrder(push: List, pop: List) -> bool:
    stack = []
    n = len(push)
    if n != len(pop):
        return False
    j = 0
    i = 0
    while i < n:
        while (len(stack) == 0 or pop[i] != stack[-1]):
            if j < n:
                stack.append(push[j])
                j += 1
            else:
                return False
        stack.pop()
        i += 1
    return not stack and j == i == n

push = [1, 2 ,3, 4, 5]
pop = [4, 5, 3, 2, 1]
print(isPopOrder(push, pop))

push = [1, 2 ,3, 4, 5]
pop = [4, 3, 5, 1, 2]
print(isPopOrder(push, pop))