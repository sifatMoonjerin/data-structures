#LinkedList Implementation of Stack

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.top = None

    
    def stackPush(self, data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode

    
    def stackPop(self):
        if self.top is None:
            self.stackEmpty()
            return
        
        self.top = self.top.next
        
    
    def stackTop(self):
        if self.top is None:
            self.stackEmpty()
            return
        
        print(self.top.data)


    def isEmpty(self):
        if self.top is None:
            self.stackEmpty()
            return
        print("Stack is not empty")


    def stackEmpty(self):
        print("Empty stack")


    def stackPrint(self):
        if self.top is None:
            self.stackEmpty()
            return
        
        cur = self.top

        while cur is not None:
            print(cur.data, end = ' ')
            cur = cur.next
        
        print("\n##########")
        

linkedList = LinkedList()
linkedList.stackPush(5)
#linkedList.stackPrint()
linkedList.stackPush(4)
#linkedList.stackPrint()
linkedList.stackPop()
#linkedList.stackPrint()
linkedList.stackPush(9)
#linkedList.stackPrint()
linkedList.stackPush(1)
linkedList.stackPrint()
linkedList.stackTop()

