# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l2_head = l2    # 用l2_head保存l2的头部
        l1_head = l1    # 用l1_head保存l1的头部
        while l2_head != None and l1.next != None: # 如果此时l2头部的数在l1和l1.next之间则插入到两者之间
            if l1.val <= l2_head.val and l1.next.val >= l2_head.val:
                l2 = l2.next
                l1_next = l1.next
                l1.next = l2_head
                l1 = l1.next # l1对比过之后也要往后挪一个
                l2_head.next = l1_next
                l2_head = l2
                continue
            elif l1.val > l2_head.val: #如果此时l2_head比l1的小,则把l2_head插到l1前面去,并把l1_head更新
                l2 = l2.next
                l2_head.next = l1
                l1_head = l2_head
                l2_head = l2 # l2要记得往后移一个
                continue
            elif l1.next.val < l2_head.val:
                l1 = l1.next
                continue

        if l2_head == None:
            return l1_head
        if l1.next == None:
            l1.next = l2_head
            return l1_head

# l1=[1,2,4]
# l2=[1,3,4]

l1 = ListNode(1)  #节点2 做头
l1_2 = ListNode(2)
l1.next = l1_2  #节点4,放在2的后面
l1_2.next = ListNode(4) #节点3,放在4的后面

l2 = ListNode(1)
l2_2 = ListNode(3)
l2.next = l2_2
l2_2.next = ListNode(4)
s = Solution()

l3 = s.mergeTwoLists(l1,l2)
print("Test case 1:")
while l3 != None:
    print(l3.val)
    l3 = l3.next

# l1=[1,2,4]
# l2=[1,3]
l1 = ListNode(1)  #节点2 做头
l1_2 = ListNode(2)
l1.next = l1_2  #节点4,放在2的后面
l1_2.next = ListNode(4) #节点3,放在4的后面

l2 = ListNode(1)
l2_2 = ListNode(3)
l2.next = l2_2
s = Solution()

l3 = s.mergeTwoLists(l1,l2)
print("Test case 2:")
while l3 != None:
    print(l3.val)
    l3 = l3.next

# l1=[1]
# l2=[1,3,4]
l1 = ListNode(1)  #节点2 做头


l2 = ListNode(1)
l2_2 = ListNode(3)
l2.next = l2_2
l2_2.next = ListNode(4) #节点3,放在4的后面
s = Solution()

l3 = s.mergeTwoLists(l1,l2)
print("Test case 3:")
while l3 != None:
    print(l3.val)
    l3 = l3.next

# l1=[2,2]
# l2=[1,3,4]
l1 = ListNode(2)  #节点2 做头
l1_2 = ListNode(2)
l1.next = l1_2  #节点4,放在2的后面

l2 = ListNode(1)
l2_2 = ListNode(3)
l2.next = l2_2
l2_2.next = ListNode(4) #节点3,放在4的后面
s = Solution()

l3 = s.mergeTwoLists(l1,l2)
print("Test case 4:")
while l3 != None:
    print(l3.val)
    l3 = l3.next

# l1=[4,6]
# l2=[2]
l1 = ListNode(4)  #节点2 做头
l1_2 = ListNode(6)
l1.next = l1_2  #节点4,放在2的后面

l2 = ListNode(2)

s = Solution()

l3 = s.mergeTwoLists(l1,l2)
print("Test case 5:")
while l3 != None:
    print(l3.val)
    l3 = l3.next