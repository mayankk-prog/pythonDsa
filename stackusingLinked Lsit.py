from linkedList import *
class stack:
    def __init__(self):
        self.myList= SLL()
        self.itemCount=0
    def is_empty(self):
        return self.myList.is_empty()
    def push(self, data):
        self.myList.insert_at_start(data)
        self.itemCount+=1
    def pop(self):
        if not self.is_empty():
            self.myList.delete_first()
            self.itemCount-=1
    def peek(self):
        if not self.is_empty():
            return self.myList.start.item
    def size(self):
        return self.itemCount

s= stack()
s.push(10)
s.push(20)
print(s.peek())
s.pop()
print(s.peek)
    