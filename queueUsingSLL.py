class Node:
    def __init__(self, item= None, next= None):
        self.item = item
        self.next = next
class Queue:
    def __init__(self):
        # self.queue = []
        self.front= None
        self.rear= None
        self.item_count= 0
    def is_empty(self):
        return self.item_count == 0
    def enqueue(self, data):
        n=Node(data)
        if self.is_empty():
            self.front= n
            self.rear= n
        else:
            self.rear.next = n
            self.rear= n
        self.item_count+=1
    def dequeue(self):
        if not self.is_empty():
            self.front= self.front.next
        elif self.front== self.rear:
            self.front= None
            self.rear= None
        self.item_count -= 1
    def get_front(self):
        if not self.is_empty():
            return self.front.item
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
    def size(self):
        return self.item_count

q= Queue()
q.enqueue(1)
q.enqueue(2)
print(q.get_front())