class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def insertStart(self,newNode,headNode):
        newNode.next = headNode
        self.head = newNode


    def insertNth(self,newNode,headNode,position):
        if(position == 0):
            self.insertStart(newNode, headNode)
            return
        
        while position is not 1:
            headNode = headNode.next
            position -= 1
            
        newNode.next = headNode.next
        headNode.next = newNode
        

    def insertEnd(self, newNode,lastNode):
        if self.head is None:
            self.head = newNode
            return

        while lastNode.next is not None:
            lastNode = lastNode.next
        
        lastNode.next = newNode
    

    def deleteNth(self,headNode,position):
        if(position == 0):
            self.head = headNode.next
            return

        while position is not 1:
            headNode = headNode.next
            position -= 1

        headNode.next = headNode.next.next


    def reverseIter(self, currentNode):
        prevNode = None
        nextNode = currentNode
        
        while nextNode is not None:
            nextNode = nextNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        
        self.head = prevNode
    

    def reverseRecur(self, curNode):
        if curNode.next is None:
            self.head = curNode
            return
        
        self.reverseRecur(curNode.next)
        curNode.next.next = curNode
        curNode.next = None


    def printList(self):
        if self.head is None:
            print("Empty list")
            return

        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next
        

    def printRecur(self, currentNode):
        if self.head is None:
            print("Empty list")
            return

        if currentNode is None: return
        print(currentNode.data)
        self.printRecur(currentNode.next)
        print(currentNode.data)  #reverse



linkedList = LinkedList()
for i in range(3):
    newNode = Node(input("Enter data: "))
    #linkedList.insertStart(newNode, linkedList.head)
    linkedList.insertEnd(newNode, linkedList.head)
    

#linkedList.printList()
#newNode = Node(input("Enter data: "))
#position = int(input("Enter Position(Starts at 0): "))  
#linkedList.insertNth(newNode, linkedList.head, position)
#linkedList.deleteNth(linkedList.head, position)
#linkedList.reverseIter(linkedList.head)
#print("********")
#linkedList.printRecur(linkedList.head)
linkedList.reverseRecur(linkedList.head)
linkedList.printList()

    