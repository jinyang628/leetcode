1class Node:
23    def __init__(self, val: str):
4        self.val = val
5        self.prev = None
6        self.next = None
78class BrowserHistory:
910    def __init__(self, homepage: str):
11        self.curr = Node(homepage)
1213    def visit(self, url: str) -> None:
14        node = Node(url)
15        node.prev = self.curr
16        self.curr.next = node
17        self.curr = node
1819    def back(self, steps: int) -> str:
20        for _ in range(steps):
21            if self.curr.prev:
22                self.curr = self.curr.prev 
23        return self.curr.val
242526    def forward(self, steps: int) -> str:
27        for _ in range(steps):
28            if self.curr.next:
29                self.curr = self.curr.next
30        return self.curr.val
31323334# Your BrowserHistory object will be instantiated and called as such:
35# obj = BrowserHistory(homepage)
36# obj.visit(url)
37# param_2 = obj.back(steps)
38# param_3 = obj.forward(steps)