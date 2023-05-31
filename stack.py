class Stack():
    def __init__(self):
        self.items=[]
        
    def push(self,item):
        self.items.append(item)
        pass
    
    def pop(self):
        self.items.pop()
        pass
    
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None
    
    def size(self):
        if self.items:
            return len(self.items)
        else:
            return None
    
    def isEmpty(self):
        if self.items==[]:
            print("Empty")
        else:
            print("Not Empty");
    
    def show(self):
        print(self.items)
    
s=Stack()
s.push(23)
s.push(13)
s.push(3)
s.push(2)
s.push(56)
s.show()
print(s.size())
s.pop()
s.show()
print(s.size())
print(s.peek())
s.isEmpty()
