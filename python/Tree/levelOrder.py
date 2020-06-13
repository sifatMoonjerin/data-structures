


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    
    def insertData(self, data, tempRoot):
        if tempRoot is None:
            self.root = Node(data)
        elif (data > tempRoot.data):
            if tempRoot.right is None:
                tempRoot.right = Node(data)
            else:
                self.insertData(data, tempRoot.right)
        else:
            if tempRoot.left is None:
                tempRoot.left = Node(data)
            else:
                self.insertData(data, tempRoot.left)

    
    def levelOrder(self, tempRoot):
        if tempRoot is None: return
        q.enQ(tempRoot)
        while not q.qEmpty():
            res = q.qFront()
            print(res.data)
            if res.left is not None: q.enQ(res.left)
            if res.right is not None: q.enQ(res.right)
            q.dQ()

################################################################

class QNode:
    def __init__(self, node):
        self.node = node
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.tail = None

    
    def enQ(self, node):
        newNode = QNode(node)
        if self.tail is None: 
            self.front = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
    

    def dQ(self):
        if self.front is None: return
        self.front = self.front.next
        if self.front is None: self.tail = None
    

    def qEmpty(self):
        if self.front is None: return True
        return False


    def qFront(self):
        return self.front.node

########################################################################

q = Queue()
orchid = BST()

orchid.insertData(15, orchid.root)
orchid.insertData(10, orchid.root)
orchid.insertData(20, orchid.root)
orchid.insertData(25, orchid.root)
orchid.insertData(8, orchid.root)
orchid.insertData(12, orchid.root)

orchid.levelOrder(orchid.root)



