import heapq
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        heap = [] # (negative_diff, favored_city (0,1), a_cost, b_cost)
        for a, b in costs:
            if a < b:
                negative_diff = a - b
                heapq.heappush(heap, (negative_diff, 0, a, b))
            else:
                negative_diff = b - a
                heapq.heappush(heap, (negative_diff, 1, a, b))
        a_costs = []
        b_costs = []
        max_length = len(costs) // 2
        while heap:
            _, favored_city, a_cost, b_cost = heapq.heappop(heap)
            if not favored_city:
                if len(a_costs) < max_length:
                    a_costs.append(a_cost)
                else:
                    b_costs.append(b_cost)
            else:
                if len(b_costs) < max_length:
                    b_costs.append(b_cost)
                else:
                    a_costs.append(a_cost)
        return sum(a_costs) + sum(b_costs)