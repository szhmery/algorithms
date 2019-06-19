#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#19. Remove Nth Node From End of List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    #打印内置函数,用print就可以把链表打印出来
    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummp = ListNode(-1)
        dummp.next = head
        #用快慢两个链表。先滑动快的n位。然后同时再一起滑动快慢,直到fast结束。这时候slow就处于倒数n的位置。
        #用slow.next = slow.next.next删除倒数n的node
        slow, fast = dummp, dummp

        for i in range(n):
            fast = fast.next
        while fast.next:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next

        return dummp.next

if __name__=="__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print(Solution().removeNthFromEnd(head, 2))

