class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    
    def enqueue(self, data):
        entry = Node(data)
        if self.front is None and self.rear is None:
            self.front = entry
            self.rear = entry
            return
        self.rear.next = entry
        self.rear = entry


    def dequeue(self):
        if self.front is None: return
        if self.front is self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next


    def isEmpty(self):
        if self.front is None:
            print("Empty Queue")
            return True
        return False


    def qFront(self):
        if not self.isEmpty():
            return self.rear.data

    
    def qPrint(self):
        while self.front is not None:
            print(self.front.data)
            self.front = self.front.next


queue = Queue()

queue.qFront()
queue.enqueue(4)
queue.enqueue(7)
queue.dequeue()
queue.enqueue(2)
queue.enqueue(6)
queue.enqueue(9)
queue.dequeue()
queue.enqueue(8)
queue.qPrint()
