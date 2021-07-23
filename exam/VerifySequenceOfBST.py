from typing import List


def verifySequenceOfBST(sequence: List) -> bool:
    if not sequence or len(sequence) == 0:
        return False
    root_v = sequence[-1]
    if len(sequence) == 1: # complete condition
        return True
    i = 0
    for i in range(len(sequence) - 1):
        if sequence[i] > root_v:
            break
    j = i
    for j in range(i, len(sequence) - 1):
        if sequence[j] < root_v:
            return False
    return verifySequenceOfBST(sequence[0:i]) and verifySequenceOfBST(sequence[i:len(sequence) - 1])


s = [7, 4, 6, 5]
print(verifySequenceOfBST(s))
s = [5, 7, 6, 9, 11, 10, 8]
print(verifySequenceOfBST(s))
