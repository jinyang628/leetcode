class MedianFinder:
    def __init__(self):
        self.minHeap = [] # Store the big values
        self.maxHeap = [] # Store the small values
    def addNum(self, num: int) -> None:
        if not self.maxHeap and not self.minHeap:
            heapq.heappush(self.minHeap, num)
        elif self.minHeap[0] >= num:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        if len(self.maxHeap) == len(self.minHeap):
            return
        if len(self.minHeap) - len(self.maxHeap) > 1:
            element = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * element)
        if len(self.maxHeap) - len(self.minHeap) > 1:
            element = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, element)        
    def findMedian(self) -> float:  
        if not self.maxHeap and not self.minHeap:
            return 0.0
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 1:
            if len(self.maxHeap) > len(self.minHeap):
                return -self.maxHeap[0]
            return self.minHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0]) / 2
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()