from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        visited = set()
        bank = set(bank) # O(1) access
        queue = deque([])
        queue.append((startGene, 0))
        characters = ["A", "C", "G", "T"]
        while queue:
            gene, dist = queue.popleft()
            if gene == endGene:
                return dist
            visited.add(gene)
            for i in range(len(gene)):
                prefix = gene[:i]
                suffix = gene[i + 1:]
                for char in characters:
                    candidate = prefix + char + suffix
                    if candidate in bank and candidate not in visited:
                        queue.append((candidate, dist + 1))
        return -1