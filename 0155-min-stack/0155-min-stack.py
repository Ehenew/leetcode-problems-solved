class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return []
        

    def getMin(self) -> int:
        min_ = 0
        for i in range(len(self.stack)):
            min_ = min(min_, self.stack[i])
        
        return min_


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()