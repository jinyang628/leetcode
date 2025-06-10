class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        remainingGas = idx = i = 0
        while i < len(gas):
            if remainingGas + gas[i] >= cost[i]:
                remainingGas = remainingGas + gas[i] - cost[i]
                i += 1
            elif gas[i] >= cost[i]:
                remainingGas = gas[i] - cost[i]
                idx = i
                i += 1
            else:
                while gas[i] < cost[i]:
                    i += 1
                remainingGas = gas[i] - cost[i]
                idx = i
                i += 1
        return idx