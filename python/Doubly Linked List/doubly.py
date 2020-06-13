class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def insertAtHead(self, newNode, curNode):
        newNode.next = curNode
        if curNode is not None: curNode.prev = newNode
        self.head = newNode


    def insertAtTail(self, newNode, curNode):
        if self.head is None:
            self.head = newNode
            return
        
        while curNode.next is not None:
            curNode = curNode.next
        
        curNode.next = newNode
        newNode.prev = curNode


    def printForward(self, curNode):
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.next


    def printReverse(self, curNode):
        while curNode.next is not None:
            curNode = curNode.next

        while curNode is not None:
            print(curNode.data)
            curNode = curNode.prev


################################################


linkedList = LinkedList()

for i in range(3):
    newNode = Node(input("Enter data: "))
    #linkedList.insertAtTail(newNode, linkedList.head)
    linkedList.insertAtHead(newNode, linkedList.head)

linkedList.printForward(linkedList.head)
print("######################")
linkedList.printReverse(linkedList.head)