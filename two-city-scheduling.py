1class Solution:
2    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
3        for idx, cost in enumerate(costs):
4            costs[idx] = [cost[0], cost[1], cost[1] - cost[0]]
5        costs.sort(key=lambda x: x[2])
6        res = 0
7        left, right = 0, len(costs) -1
8        while left <= right:
9            if left != right:
10                res += costs[left][1]
11                res += costs[right][0]
12            else:
13                res += min(costs[left][0], costs[left][1])
14            left += 1
15            right -= 1
16        return res