from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        def getNeighbors(curr: str) -> list[str]:
            res = []
            for i in range(len(curr)):
                tmp = list(curr)
                curr_slot = curr[i]
                if curr_slot == "0":
                    neighbor_slots = ["9", "1"]
                elif curr_slot == "9":
                    neighbor_slots = ["8", "0"]
                else:
                    neighbor_slots = [str(int(curr_slot) - 1), str(int(curr_slot) + 1)]
                for n in neighbor_slots:
                    tmp[i] = n
                    res.append("".join(tmp))
            return res
        queue = deque([])
        queue.append(("0000", 0))
        visited = set()
        while queue:
            num, turns = queue.popleft()
            if num == target:
                return turns
            if num in visited:
                continue
            if num in deadends:
                continue
            visited.add(num)
            neighbors = getNeighbors(num)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                queue.append((neighbor, turns + 1))
        return -1