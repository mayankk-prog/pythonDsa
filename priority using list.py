class priority_queue:
    def __init__(self):
         self.items= []
    def push(self,data, priority):
        index= 0
        while index < len(self.items) and data > self.items[index][1]<= priority:
            index+=1
        self.items.insert(index, (data, priority))
    def is_empty(self):
        return len(self.items) == 0
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop(0)[0]
    def size(self):
        return len(self.items)

p = priority_queue
p.push("amit", 4)
