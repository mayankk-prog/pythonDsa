class Deque:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def insert_front(self, data):
        self.items.insert(0, data)
    def insert_rear(self, data):
        self.items.append(data)
    def delete_front(self):
        if not self.is_empty():
            self.items.pop(0)
    def delete_rear(self):
        if not self.is_empty():
            self.items.pop(-1)
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
    def get_front(self):
        if not self.is_empty():
            return self.items[-1]
    def size(self):
        return len(self.items)

d= Deque()
d.insert_front(1)
d.insert_rear(2)
print(d.get_front())
