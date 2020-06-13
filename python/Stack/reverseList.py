stack = []

class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    
    def insert(self, data):
        curNode = Node(data)
        curNode.next = self.head
        self.head = curNode


    def reverse(self):
        curNode = self.head
        while curNode is not None:
            stack.append(curNode)
            curNode = curNode.next

        newNode = stack.pop()
        self.head = newNode
        while len(stack) is not 0:
            newNode.next = stack.pop()
            newNode = newNode.next
            newNode.next = None
            
            
    def printList(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end = " ")
            cur = cur.next
        print("\n")



linkedList = LinkedList()

for i in range(5):
    linkedList.insert(5-i)

linkedList.printList()
linkedList.reverse()
linkedList.printList()

