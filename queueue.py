class queue:
    def __init__(self):
        self.items= []
        # self.front= None
        # self.rare= None
    def is_empty(self):
        return len(self.items)==0
    def enqueue(self, data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
    def get_rare(self):
        if not self.is_empty():
            return self.items[-1]
    def size(self):
        return len(self.items)

q= queue()
q.enqueue(10)
print(q.get_front())
q.enqueue(20)
q.enqueue(30)
print(q.get_front())
print(q.get_rare())