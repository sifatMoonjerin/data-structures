#Implementation of Binary Search Tree


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    
    def insertData(self, data, tempRoot):
        if self.root is None:
            newNode = Node(data)
            self.root = newNode
            return
        else:
            if tempRoot is None:
                tempRoot = Node(data)
            elif(data > tempRoot.data):
                tempRoot.right = self.insertData(data, tempRoot.right)
            else:
                tempRoot.left = self.insertData(data, tempRoot.left) 
            return tempRoot

    
    def searchData(self, data, tempRoot):
        if tempRoot is None: return False
        elif(data == tempRoot.data): 
            return True
        elif(data > tempRoot.data): return self.searchData(data, tempRoot.right)
        else: return self.searchData(data, tempRoot.left)


    def findMin(self, tempRoot):
        if tempRoot is None: return
        elif tempRoot.left is None:
            return tempRoot.data
        else:
            return self.findMin(tempRoot.left)


    def inOrder(self, tempRoot):
        if tempRoot is None: return
        self.inOrder(tempRoot.left)
        print(tempRoot.data, end = ' ')
        self.inOrder(tempRoot.right)

    
    def deleteData(self, data, tempRoot):
        if tempRoot is None: return tempRoot
        elif data < tempRoot.data:
            tempRoot.left = self.deleteData(data, tempRoot.left)
        elif data > tempRoot.data:
            tempRoot.right = self.deleteData(data, tempRoot.right)
        else:
            if tempRoot.left is None and tempRoot.right is None:
                tempRoot = None
            elif tempRoot.left is None:
                tempRoot = tempRoot.right
            elif tempRoot.right is None:
                tempRoot = tempRoot.left
            else:
                tempRoot.data = self.findMin(tempRoot.right)
                tempRoot.right = self.deleteData(tempRoot.data, tempRoot.right)
        return tempRoot



                
###########################################################################


orchid = BST()
orchid.insertData(15, orchid.root)
orchid.insertData(10, orchid.root)
orchid.insertData(20, orchid.root)
orchid.insertData(25, orchid.root)
orchid.insertData(8, orchid.root)
orchid.insertData(12, orchid.root)
orchid.insertData(11, orchid.root)
orchid.insertData(9, orchid.root)
orchid.insertData(2, orchid.root)

orchid.inOrder(orchid.root)
orchid.deleteData(10, orchid.root)
print()
orchid.inOrder(orchid.root)



#for i in range(10):
#    num = input("Enter number: ")
#   result = orchid.searchData(int(num), orchid.root)
#    if result: print("Number is present")
#    else: print("Number is absent")



