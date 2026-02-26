1class SeatManager:
23    def __init__(self, n: int):
4        self.heap = [i for i in range(1, n + 1)]
5        heapq.heapify(self.heap)
67    def reserve(self) -> int:
8        return heapq.heappop(self.heap)
910    def unreserve(self, seatNumber: int) -> None:
11        heapq.heappush(self.heap, seatNumber)
12131415# Your SeatManager object will be instantiated and called as such:
16# obj = SeatManager(n)
17# param_1 = obj.reserve()
18# obj.unreserve(seatNumber)