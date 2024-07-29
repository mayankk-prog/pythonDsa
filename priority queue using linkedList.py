class Node:
    def __init__(self, item = None, priority= None, next= None):
        self.item= item
        self.priority= priority
        self.next= next
class priority_Queue:
    def __init__(self):
        self.start= None
        self.item_count= 0
    def push(self, data,priority):
        n= Node(data, priority)
        if not self.start or priority<self.start.priority:
            n.next= self.start
            self.start= n
        else:
            temp= self.start
            while temp.next and temp.next.priority<=priority:
                temp= temp.next
            n.next= temp.next
            temp.next= n
        self.item_count+=1
    def is_empty(self):
        return eslf.start== None
    def pop(self):
        if not self.is_empty():
            data= self.start.item
            self.start= self.start.next
        self.item_count-=1
        return data
    def size(self):
        return self.item_count

p= priority_Queue()
p.push(1, 3)
p.push(2,4)