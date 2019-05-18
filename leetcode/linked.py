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

    def reserve(self):
        if self.head == None:
            return None

        nodeResult = None

        nodePre = None
        current = self.head

        while current != None:
            nodeNext = current.next

            if nodeNext == None:
                nodeResult = current

            current.next = nodePre
            nodePre = current
            current = nodeNext

        return nodeResult

    def printlist(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

myList = LinkedList()

myList.add(5)
myList.add(8)
myList.add(12)
print("Before reverse:")
myList.printlist()
NewNode = myList.reserve()
print("After reverse:")
while NewNode != None:
    print(NewNode.data)
    NewNode = NewNode.next

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

