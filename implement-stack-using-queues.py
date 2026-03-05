1from collections import deque
2class MyStack:
34    def __init__(self):
5        self.front_to_back_queue = deque([])
6        self.back_to_front_queue = deque([])
78    def push(self, x: int) -> None:
9        self.front_to_back_queue.append(x)
1011    def pop(self) -> int:
12        copy = deque([])
13        for _ in range(len(self.front_to_back_queue) - 1):
14            copy.append(self.front_to_back_queue.popleft())
15        res = self.front_to_back_queue.popleft()
16        self.front_to_back_queue = copy
17        return res
1819    def top(self) -> int:
20        copy = deque([])
21        for _ in range(len(self.front_to_back_queue) - 1):
22            copy.append(self.front_to_back_queue.popleft())
23        res = self.front_to_back_queue.popleft()
24        copy.append(res)
25        self.front_to_back_queue = copy
26        return res
272829    def empty(self) -> bool:
30        return not len(self.front_to_back_queue)
313233# Your MyStack object will be instantiated and called as such:
34# obj = MyStack()
35# obj.push(x)
36# param_2 = obj.pop()
37# param_3 = obj.top()
38# param_4 = obj.empty()