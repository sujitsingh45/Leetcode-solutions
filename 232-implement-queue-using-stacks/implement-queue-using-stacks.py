class MyQueue:

    def __init__(self):
        self.stackA=[]
        self.stackB=[]
        
        
    def push(self, x: int) -> None:
        
        while len(self.stackA)>0:
            self.stackB.append(self.stackA.pop())
        self.stackA.append(x)
        while len(self.stackB)>0:
            self.stackA.append(self.stackB.pop())    

        

    def pop(self) -> int:
        x=self.stackA[-1] # storing  last element 
        self.stackA.pop()  # deleting last element
        return x
        
          
    def peek(self) -> int:
        
        return self.stackA[-1]   # returning last element 
        

    def empty(self) -> bool:
        return len(self.stackA)==0   
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()