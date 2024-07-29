class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self, data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("")
    def size(self):
        if not self.is_empty():
            return len(self)
    def insert(self, index, data):
        raise AttributeError("no attribute")

s= Stack()
s.push(10)
s.push(20)
print(s.peek())
