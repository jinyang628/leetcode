class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_order = defaultdict(int)
        for a, b in edges:
            in_order[b] += 1
        winner = -1
        for i in range(n):
            if in_order[i]:
                continue
            if winner == -1:
                winner = i
            else:
                return -1
        return winner