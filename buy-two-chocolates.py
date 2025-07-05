class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        heapq.heapify(prices)
        first = heapq.heappop(prices)
        second = heapq.heappop(prices)
        if first + second > money:
            return money
        return money - first - second