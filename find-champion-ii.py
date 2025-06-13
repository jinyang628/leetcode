class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_order = defaultdict(int)
        for _, element in edges:
            in_order[element] += 1
        champion = None
        for i in range(n):
            if not in_order[i]:
                if champion is not None:
                    return -1
                champion = i
        return champion