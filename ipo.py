import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        tmp = []
        profits = [(-profits[i], capital[i]) for i in range(len(profits))]
        heapq.heapify(profits)
        count = 0
        while profits:
            if count == k:
                return w
            should_stop = True
            while profits:
                negative_profit, capital_needed = heapq.heappop(profits)
                if capital_needed <= w:
                    w += -negative_profit
                    count += 1
                    should_stop = False
                    break
                tmp.append((negative_profit, capital_needed))
            if should_stop:
                break
            for element in tmp:
                heapq.heappush(profits, element)
            tmp = []
        return w