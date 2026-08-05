class MinStack:

    def __init__(self):
        self.stack = []
        #self.mini= float('inf')

    def push(self, val: int) -> None:
        mini = self.getMin()
        if mini == None or mini > val:
                mini = val
        
        self.stack.append([val,mini])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return None
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()