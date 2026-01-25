1class MinStack:
23    def __init__(self):
4        self.stack = [] # (actual value, smallest_so_far)
56    def push(self, val: int) -> None:
7        if not self.stack:
8            self.stack.append((val, val))
9        else:
10            self.stack.append((val, min(val, self.stack[-1][1])))
1112    def pop(self) -> None:
13        self.stack.pop()
1415    def top(self) -> int:
16        return self.stack[-1][0]
171819    def getMin(self) -> int:
20        return self.stack[-1][1]
21222324# Your MinStack object will be instantiated and called as such:
25# obj = MinStack()
26# obj.push(val)
27# obj.pop()
28# param_3 = obj.top()
29# param_4 = obj.getMin()