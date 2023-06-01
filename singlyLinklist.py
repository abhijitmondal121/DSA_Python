class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
    
class Linklist:
    def __init__(self):
        self.head=None
        
    def insertAtBigining(self,data):
        newNode=Node(data)
        newNode.ref=self.head
        self.head=newNode
    
    def insertAtEnd(self,data):
        newNode=Node(data)
        n=self.head
        if n is None:
            self.head=newNode
        else:
            while n.ref is not None:
                n=n.ref
            n.ref=newNode
    
    def insertAfterTarget(self,data,x):
        n=self.head
        while n is not None:
            if n.data==x:
                break
            n=n.ref
        if n is None:
            print("Node is not present... ")
        else:
            newNode=Node(data)
            newNode.ref=n.ref
            n.ref=newNode
            
            
    def insertBeforeRarget(self,data,x):
        if self.head is None:
            print("The Linklist is empty...")
            return
        if self.head.data==x:
            newNode=Node(data)
            newNode.ref=self.head
            self.head=newNode
            return
        
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        
        if n.ref is  None:
            print("Node is not found ")
        
        newNode=Node(data)
        newNode.ref=n.ref
        n.ref=newNode
    
    
    def delAtBegining(self):
        if self.head is None:
            print("Linklist is Empty..")
        else:
            self.head=self.head.ref
    
    def delAtEnd(self):
        if self.head is None:
            print("Linklist is Empty: ")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    def delAtValue(self,x):
        if self.head is None:
            print("Linklist is Empty....")
        if x==self.head.data:
            self.head=self.head.ref
        
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("Element no present...")
        else:
            n.ref=n.ref.ref
        
        
    def printLinklist(self):
        if self.head is None:
            print("Linklist is empty")
        
        n=self.head
        while n is not None:
            print(n.data,"  -->  ",end="")
            n=n.ref
            
            
            
l=Linklist()
l.insertAtEnd(34)
l.insertAtBigining(67)
l.insertAtEnd(32)
l.insertAfterTarget(100,67)
l.insertBeforeRarget(300,32)
l.printLinklist()
print()
# l.delAtBegining()
# l.delAtEnd()
l.delAtValue(34)
l.printLinklist()
            
    