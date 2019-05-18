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
        # 通过生成器把l1的数据都取出,转成str,存入list1中
        list1 = [str(i) for i in my_generator(l1)]
        print(list1)
        # 通过生成器把l2的数据都取出,转成str,存入list2中
        list2 = [str(i) for i in my_generator(l2)]
        print(list2)
        # 把list1中的所有值连到一起并反向,之后转为int
        print(int("".join(list1[::-1])))
        # 把list2中的所有值连到一起并反向,之后转为int
        print(int("".join(list2[::-1])))
        # 两个数相加后又转回str,然后map成int,list把map中数又转为list
        return list(map(int, str(int("".join(list1[::-1]))  + int("".join(list2[::-1])))[::-1]))
        #return list(str(int("".join(list1[::-1])) + int("".join(list2[::-1])))[::-1])


#生成器,返回linked list中的数据并返回。
def my_generator(linked_list):
    generator_list = linked_list
    while generator_list:
        yield generator_list.val
        generator_list = generator_list.next

# l1=[2,4,3]
# l2=[5,6,4]

l1 = ListNode(2)  #节点2 做头
l1_2 = ListNode(4)
l1.next = l1_2  #节点4,放在2的后面
l1_2.next = ListNode(3) #节点3,放在4的后面
l2 = ListNode(5)
l2_2 = ListNode(6)
l2.next = l2_2
l2_2.next = ListNode(4)

s = Solution()
print(s.addTwoNumbers(l1,l2))