class StockSpanner:
    def __init__(self):
        # (price, date)
        self.stack = deque([(inf, 0)])
        self.date = 1
    def next(self, price: int) -> int:
        while self.stack[-1][0] <= price:
            self.stack.pop()
        span = self.date - self.stack[-1][1]
        self.stack.append((price, self.date))
        self.date += 1
        return span
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)