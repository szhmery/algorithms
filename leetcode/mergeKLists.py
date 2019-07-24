#https://leetcode.com/problems/merge-k-sorted-lists/
#23. Merge k Sorted Lists

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
    def __repr__(self):
        if self:
            return "{}->{}".format(self.val, self.next)


class Solution():
    def mergeKLists(self, lists):

        def merge2Lists(l1, l2):
            curr = dummp = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            curr.next = l1 or l2
            return dummp.next

        if not lists:
            return None
        left, right = 0,len(lists)-1
        while right > 0:
            if left >= right:
                left = 0
            else:
                lists[left] = merge2Lists(lists[left],lists[right])
                left += 1
                right -= 1
        return lists[0]


class Solutions2():
    def mergeKLists(self,lists):
        def merge2Lists(l1,l2):
            curr = dummp = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummp.next
        def mergeKlistsHelper(lists, begin, end):
            if begin > end:
                return None
            if begin == end:
                return lists[begin]
            return merge2Lists(mergeKlistsHelper(lists,begin,(begin+end)/2),
                               mergeKlistsHelper(lists,(begin+end)/2+1,end))

        return mergeKlistsHelper(lists,0,len(lists)-1)

class Solution3():
    def mergeKLists(self, lists):

        def merge2Lists(l1, l2):
            curr = dummp = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            curr.next = l1 or l2
            return dummp.next

        if not lists:
            return None
        for i in range(len(lists)-1):
            lists[0] = merge2Lists(lists[0],lists[i+1])
        return lists[0]

if __name__=="__main__":
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l2 = ListNode(2)
    l2.next = ListNode(4)
    lists = []
    lists.append(l1)
    lists.append(l2)
    print(Solution3().mergeKLists(lists))


