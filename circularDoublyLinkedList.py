class Node:
    def __init__(self, item= None, prev= None, next= None):
        self.item = item
        self.prev= prev
        self.next= next
class Cdll:
    def __init__(self, start= None):
        self.start= start
    def is_empty(self):
        return self.start== None
    def isnert_at_last(self, data):
        n= Node(data)
        if self.is_empty():
            n.next= n
            n.prev= n
        else:
            n.next= self.start
            n.prev= self.start.prev
            self.start.prev.next= n
            self.start.prev= n
        self.start= n
    def insert_at_last(self, data):
        n= Node(data)
        if self.is_empty():
            n.next= n
            n.prev= n
            self.start= n
        else:
            n.next= self.start
            n.prev= self.start.prev
            n.prev.next= n
            self.start.prev= n
    def search(self, data):
        temp= self.start
        if temp==None:
            return None
        if temp.item== data:
            return temp
        else:
            temp= temp.next
        while temp!= self.start:
            if temp.item== data:
                return temp
            temp= temp.next
        return None
    def insert_after(self, temp, data):
        if temp is not None:
            n= Node(data)
            n.next= temp.next
            n.prev= temp
            temp.next.prev= n
            temp.next= n
    def print_list(self):
        temp= self.start
        if temp is not None:
            print(temp.item, end=' ')
            temp= temp.next
            while temp is not self.start:
                print(temp, end=' ')
                temp= temp.next
    def delete_first(self):
        if self.start is not None:
            if self.start.next== self.start:
                self.start= None
            else:
                self.start.prev.next= self.start.next
                self.start.next.prev= self.start.prev   
                self.start= self.start.next
    def delete_last(self):
        if self.start is not None
            if self.start.next== self.start:
                self.start= None
            else:
                self.start.prev.prev.next= self.start
                self.start.prev= self.start.prev.prev
    def delete_item(self, data):
        if self.start is not None:
            temp= self.start
            if temp.item== data:
                self.delete_first()
            else:
                temp=temp.next
                while temp is not self.start
                if temp.item== data:
                    temp.prev.next= temp.next
                    temp.next.prev= temp.prev
    def __iter__(self):
        return CdllIterator(self.start)
class CdllIterator:
    def __init__(self, start):
        self.current= start
        self.start= start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current== self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data= self.current.item
        self.current= self.current.next
        return data

mylist= Cdll()
mylist.insert_last(11)
mylist.insert_after(mylist.search(10), 20)

for x in mylist:
    print(x, end=' ')
print()