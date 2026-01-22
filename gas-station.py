1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3        if sum(gas) < sum(cost):
4            return -1
5        curr = idx = last_idx = 0
6        while idx < len(gas):
7            curr += (gas[idx] - cost[idx])
8            if curr < 0:
9                last_idx = idx + 1
10                idx = last_idx
11                curr = 0
12            else:
13                idx += 1
14        return last_idx