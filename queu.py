class Queue():
    def __init__(self):
        self.q=[]
        f=None
        r=None
    
    def isEmpty(self):
        if(self.q==[]):
            return True
        else:
            return False
            
    def enqueue(self,item):
        self.q.append(item)
        if(len(self.q)==1):
            self.f=0
            self.r=0
        else:
            self.r=len(self.q)-1
            
    def dequeue(self):
        if(self.isEmpty()):
            return ('Underflow')
        else:
            i=self.q.pop(0)
        if(len(self.q)==0):
            self.f=None
            self.r=None
    
    def peek(self):
        if(self.isEmpty()):
            return('Underflow')
        else:
            return self.q[0]
    
    def show(self):
        print(self.q)
    
    
s=Queue()
s.enqueue(23)
s.enqueue(14)
s.enqueue(34)
s.enqueue(44)
s.enqueue(2)
s.dequeue()
s.dequeue()
s.show()
print(s.peek())



