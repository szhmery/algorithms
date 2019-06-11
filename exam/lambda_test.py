
list1 = [1,2,3]
list2 = [4,5,6]

data = zip(list1, list2)
print(data)

data = sorted(data)
print(data)
list1, list2 = map(lambda t: list(t), zip(*data))
print(list1)
print(list2)