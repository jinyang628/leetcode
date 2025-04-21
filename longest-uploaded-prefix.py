class LUPrefix:
    def __init__(self, n: int):
        self.stack = [i for i in range(n + 1, 0, -1)]
        self.seen = set()
    def upload(self, video: int) -> None:
        if video == self.stack[-1]:
            self.stack.pop()
            while self.stack[-1] in self.seen:
                self.stack.pop()
        else:
            self.seen.add(video)
    def longest(self) -> int:
        return self.stack[-1] - 1
# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()