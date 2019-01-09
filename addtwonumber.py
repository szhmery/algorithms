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
        print(list1)
        list2 = [str(i) for i in my_generator(l2)]
        print(list2)
        print(int("".join(list1[::-1])))
        print(int("".join(list2[::-1])))
        print(map(int, str(int("".join(list1[::-1]))  + int("".join(list2[::-1])))[::-1]))
        return list(map(int, str(int("".join(list1[::-1]))  + int("".join(list2[::-1])))[::-1]))

def my_generator(linked_list):
    generator_list = linked_list
    while generator_list:
        yield generator_list.val
        generator_list = generator_list.next

# l1=[2,4,3]
# l2=[5,6,4]

l1 = ListNode(2)
l1_2 = ListNode(4)
l1.next = l1_2
l1_2.next = ListNode(3)
l2 = ListNode(5)
l2_2 = ListNode(6)
l2.next = l2_2
l2_2.next = ListNode(4)

s = Solution()
print(s.addTwoNumbers(l1,l2))