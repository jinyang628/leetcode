import heapq
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        heapq.heapify(prices)
        lowest = heapq.heappop(prices)
        second_lowest = heapq.heappop(prices)
        total = lowest + second_lowest
        return money - total if total <= money else money