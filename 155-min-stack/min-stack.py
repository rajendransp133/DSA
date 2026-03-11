class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        self.global_min=2^31

    def push(self, val: int) -> None:
        if(self.min_stack and self.min_stack[-1]>=val):
            self.min_stack.append(val)
            self.global_min=val
        if(len(self.stack)==0):
            self.min_stack.append(val)
            self.global_min=val
        self.stack.append(val)

    def pop(self) -> None:
        if(self.min_stack and self.stack and self.min_stack[-1]==self.stack[-1]):
            self.min_stack.pop()
            if(self.min_stack):
                self.global_min=self.min_stack[-1]
            else:
                self.global_min=2^31
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.global_min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()