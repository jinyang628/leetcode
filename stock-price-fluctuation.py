import heapq
class StockPrice:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.curr = -1
        self.track = {} # key is timestamp, value is price 
    def update(self, timestamp: int, price: int) -> None:
        if timestamp > self.curr:
            self.curr = timestamp
        self.track[timestamp] = price
        heapq.heappush(self.minHeap, (price, timestamp))
        heapq.heappush(self.maxHeap, (-price, timestamp))
    def current(self) -> int:
        return self.track[self.curr]
    def maximum(self) -> int:
        while self.maxHeap and (-1 * self.track[self.maxHeap[0][1]]) != self.maxHeap[0][0]:
            curr = heapq.heappop(self.maxHeap)
        return -self.maxHeap[0][0]
    def minimum(self) -> int:
        while self.minHeap and self.track[self.minHeap[0][1]] != self.minHeap[0][0]:
            heapq.heappop(self.minHeap)
        return self.minHeap[0][0]
# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()