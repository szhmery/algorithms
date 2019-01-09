#coding=utf8

class Node(object):
    def __init__(self,x):
        self.data = x
        self.next = None
    def get_next(self):
        return self.next
    def set_next(self, x):
        self.next = x
    def get_data(self):
        return self.data
    def set_data(self, x):
        self.data = x

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def get_size(self):
        return self.size
    def add(self, d):
        new_node = Node(d)
        this_node = self.head
        self.head = new_node
        new_node.next = this_node
        self.size += 1

    def remove(self,d):
        this_node = self.head
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.head = this_node.get_next()
                self.size -= 1
                return  True
            else:
                prev_node = this_node
                this_node = this_node.get_next()

        return False

    def find(self, d):
        this_node = self.head
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
print(myList.find(5))
print(myList.find(8))
print(myList.find(12))
print(myList)
print(myList.remove(8))
print(myList.find(5))
print(myList.find(8))
print(myList.find(12))
print(myList)
print(myList.remove(12))
print(myList.find(5))
print(myList.find(8))
print(myList.find(12))


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1 = [str(i) for i in my_generator(l1)]
        list2 = [str(i) for i in my_generator(l2)]
        return list(map(int, str(int("".join(list1[::-1]))  + int("".join(list2[::-1])))[::-1]))

def my_generator(LinkedList):
    generator_list = LinkedList
    while generator_list:
        yield generator_list.data
        generator_list = generator_list.next

l1 = LinkedList()
l1.add(2)
l1.add(4)
l1.add(3)

l2 = LinkedList()
l2.add(5)
l2.add(6)
l2.add(4)

s = Solution()
s.addTwoNumbers(l1,l2)