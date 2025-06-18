from collections import defaultdict
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        neighbors = defaultdict(list)
        for a, b in roads:
            neighbors[a].append(b)
            neighbors[b].append(a)
        res = 0
        # returns the number of people at this subtree
        def dfs(curr: int, prev: int) -> int:
            nonlocal res
            count = 1
            for neighbor in neighbors[curr]:
                if neighbor == prev: 
                    continue
                count += dfs(neighbor, curr)
            if curr != 0:
                res += math.ceil(count / seats)
            return count
        dfs(0, 0)
        return res