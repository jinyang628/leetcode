class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        currGas = startingIdx = i = 0
        while i < len(gas):
            currGas += gas[i] - cost[i]
            if currGas < 0:
                currGas = 0
                startingIdx = i + 1
            i += 1
        return startingIdx