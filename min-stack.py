class MinStack:
    def __init__(self):
        self.minTrack = [] # monotonically decreasing 
        self.stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minTrack:
            self.minTrack.append(val)
            return
        if val <= self.minTrack[-1]:
            self.minTrack.append(val)
    def pop(self) -> None:
        curr = self.stack.pop()
        if curr == self.minTrack[-1]:
            self.minTrack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minTrack[-1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()